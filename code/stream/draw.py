# load stream.csv into a dataframe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('stream.csv')

# types:
# name: string
# ncpus: int
# bytes/word: int
# COPY: float
# SCALE: float
# ADD: float
# TRIAD: float
# Clock: float
# FP-OP/clock: float (peak)
# shared_memory: bool (Y/N)
# distributed_memory: bool (Y/N)
# Uniprocessor: bool (Y/N)
# result_type: "S" (standard) / "T" (tuned) / "E" (experimental)
# obsolete: bool (Y/N)
# type: "P" (PC) / "M" (MAC) / "N" (other) / "C" (cluster)
# date: datetime (from format YYYY.MM.DD)
# link: string

df['name'] = df['name'].astype('string')
df['ncpus'] = df['ncpus'].astype('int')
df['bytes/word'] = df['bytes/word'].astype('int')
df['COPY'] = df['COPY'].astype('float')
df['SCALE'] = df['SCALE'].astype('float')
df['ADD'] = df['ADD'].astype('float')
df['TRIAD'] = df['TRIAD'].astype('float')
df['Clock'] = df['Clock'].astype('float')
df['FP-OP/clock'] = df['FP-OP/clock'].astype('float')
df['shared_memory'] = df['shared_memory'].apply(lambda x: True if x == 'Y' else False).astype('bool')
df['distributed_memory'] = df['distributed_memory'].apply(lambda x: True if x == 'Y' else False).astype('bool')
df['Uniprocessor'] = df['Uniprocessor'].apply(lambda x: True if x == 'Y' else False).astype('bool')
df['result_type'] = df['result_type'].astype('string')
df['obsolete'] = df['obsolete'].apply(lambda x: True if x == 'Y' else False).astype('bool')
df['type'] = df['type'].astype('string')
df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')
df = df.drop(columns=['link'])


# calculate machine balance
operations = ['COPY', 'SCALE', 'ADD', 'TRIAD']
df['MOP/clock'] = df[operations].div(df['bytes/word'], axis=0).div(df['Clock'], axis=0).max(axis=1)
df['FLOP/s'] = df['FP-OP/clock'] * df['Clock'] * df['ncpus']
df['MOP/s'] = df['MOP/clock'] * df['Clock']
df['machine_balance'] = df['FLOP/s'] / df['MOP/s']

# remove obsolete entries
df = df[df['obsolete'] == False]
df = df.drop(columns=['obsolete'])

# remove entries with missing values
df = df.dropna()

# remove entries where result type is not standard
df = df[df['result_type'] == 'S']
df = df.drop(columns=['result_type'])

# remove outliers (using z-score) vased on FLOP/s and MOP/s
#df = df[(np.abs(stats.zscore(df['FLOP/s'])) < 3)]
#df = df[(np.abs(stats.zscore(df['MOP/s'])) < 3)]

print(df.sort_values(by=['date'], ascending=False).head(10).to_string())

# plot machine balance (as scatterplot) (with regression line). On x axis is datetime ("date"), on y axis is machine balance ("machine_balance")
reg = LinearRegression().fit(df['date'].astype(int).values.reshape(-1, 1), df['machine_balance'])

df['predicted_machine_balance'] = reg.predict(df['date'].astype(int).values.reshape(-1, 1))

fig, ax = plt.subplots()
sns.scatterplot(x='date', y='machine_balance', data=df, color='green', s=20, ax=ax)
sns.lineplot(x='date', y='predicted_machine_balance', data=df, color='green', ax=ax)

plt.title('Machine balance')
ax.set_xlabel('Date')
plt.savefig('machine_balance.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()


# plot, in a single figure, one scatterplot with regression line for the FLOP/s, and another for the MOP/s. On x axis is datetime ("date"), on y axis is FLOP/s or MOP/s
df['log_FLOPs'] = np.log10(df['FLOP/s'])
df['log_MOPs'] = np.log10(df['MOP/s'])

reg_FLOPs = LinearRegression().fit(df['date'].astype(int).values.reshape(-1, 1), df['log_FLOPs'])
reg_MOPs = LinearRegression().fit(df['date'].astype(int).values.reshape(-1, 1), df['log_MOPs'])

date_samples = np.linspace(df['date'].astype(int).min(), df['date'].astype(int).max(), 100).reshape(-1, 1)
predicted_log_FLOPs = reg_FLOPs.predict(date_samples)
predicted_log_MOPs = reg_MOPs.predict(date_samples)

predicted_FLOPs = 10 ** predicted_log_FLOPs
predicted_MOPs = 10 ** predicted_log_MOPs

date_samples = pd.to_datetime(date_samples, unit='ns')

fig, ax = plt.subplots(figsize=(12,5))
ax.plot(date_samples, predicted_FLOPs, color='b', label='FLOP/s')
ax.plot(date_samples, predicted_MOPs, color='r', label='MOP/s', linestyle='dashed')

sns.scatterplot(data=df, x='date', y='FLOP/s', color='b', ax=ax, alpha=0.4, s=10)
sns.scatterplot(data=df, x='date', y='MOP/s', color='r', ax=ax, alpha=0.4, s=10, marker='X')

ax.set_xlabel('Date')
ax.set_ylabel('FLOP/s and MOP/s')
ax.set_yscale('log')

plt.title('FLOP/s and MOP/s vs Date')
plt.legend()
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.1, hspace=0.1)
plt.savefig('FLOPs_MOPs_vs_Date.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
