1. Abstract
2. Introduction
3. Motivation / Background
	 - Increasing Gap between Processor and Memory Speeds
	 - (Prices of Processing Units and Memory/Storage Units)
	 - --> Increasing requirements for both Computation and Memory (ChatGPT, Simulations, James Webb, etc. --> find data on this)
	 - Data Transfers are expensive (find data!) --> Bottleneck of HPC
	 - --> Need to Minimize Data Transfers and Increase Data Reuse
4. Goal / Problem Statement
	- visualizing performance data, exploring data reuse with data-centric analysis, or obtaining performance insights through simulation
	- Minimize Data Transfers by coalescing (combining) computations on the same data --> Increase data reuse (decrease cache misses, etc...)
	- (Define what we are trying to achieve, so later on I can explain how each approach tackles it)
	- --> Explain that we use Visualizations to optimize the programs by hand
	- --> Must obtain suitable data first!
6. Approaches / Techniques / Methods
	1. Execution -  Profiling & Hardware Counters
	2. Simulation
	3. Static Analysis [Boosting](References#Methods#Boosting Performance Optimization with Interactive  Data Movement Visualization)
		- Briefly explain SDFG
		- Explain how it works (2 granularity approach) --> Focus on Data gathering
		- Briefly go into the visualization
7. Comparisons/Results
	- [Boosting](References#Methods#Boosting Performance Optimization with Interactive  Data Movement Visualization) is very good, as it combines visualizing performance data, exploring data reuse with data-centric analysis, or obtaining performance insights through simulation, at basically 0 cost. But not hardware specific, and requires parameter tweaking to work. Furthermore a limitation is, that it does not work well with dynamic programs (at least at the global view)
	- Further techniques that rely on execution (getting hardware counters) can verify currently made optimizations and can help to detect opportunities for further optimization based on specific hardware (architectures)
1. Conclusion
2. Outlook
 - Automatic Optimization (using heuristics), no visualizations, directly in compiler
 - ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations

-> Lead up to [PDF](reference_pdfs/Boosting_Performance_Optimization_with_Interactive_Data_Movement_Visualization.pdf) (seems to be the best, see [References](References))