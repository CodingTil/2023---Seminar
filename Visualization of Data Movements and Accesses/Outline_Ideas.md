1. Abstract
2. Introduction
3. Motivation / Background
	 - Increasing Gap between Processor and Memory Speeds
		 - https://repository.kaust.edu.sa/bitstream/handle/10754/667780/Technical%20Reportfile1.pdf?sequence=1 Figure 2.2
	 - (Prices of Processing Units and Memory/Storage Units)
	 - --> Increasing requirements for both Computation and Memory (ChatGPT, Simulations, James Webb, etc. --> find data on this)
	 - Data Transfers are expensive (find data!) --> Bottleneck of HPC
	 - --> Need to Minimize Data Transfers and Increase Data Reuse
	 - KEYWORD: **Data Locality**
1. Goal / Problem Statement
	- visualizing performance data, exploring data reuse with data-centric analysis, or obtaining performance insights through simulation
	- Minimize Data Transfers by coalescing (combining) computations on the same data --> Increase data reuse (decrease cache misses, etc...)
	- (Define what we are trying to achieve, so later on I can explain how each approach tackles it)
	- --> Explain that we use Visualizations to optimize the programs by hand
	- --> Must obtain suitable data first!
	- - Increasing Processor-Memory Speed Gap and increasing requirements result in an heavy increase in the affect of data movement costs and their resulting bottlenecks. While this can be solved by improving hardware capabilities (through breakthroughs in research), we can already try to optimize programs to mitigate these issues (by improving data locality) - Increasing complexity of programs makes it difficult to create a mental data movement model of that program, making it very difficult for experts to optimize it, and impossible for domain researchers (people in medicine etc.) - Goal: We need to make it accessible to everyone to easily optimize a program - To do this, we automatically gather data (refer to section 5), and then visualize it in a understandable manner (section 6) so people know where issues are and what issues to fix
1. Approaches / Techniques / Methods _explain each in detail, then briefly go over the concrete examples in next section_ DATA GATHERING METHODS!
	1. Dynamic Analysis -  Profiling, Tracing & Hardware Counters
		 - + Hard Data
		 - - Very Coarse Time granularity (https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6069452)
		 - Perhaps http://www.cs.umd.edu/~bhatele/pubs/pdf/2012/sc2012a.pdf
		 - https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4290697
		 - https://www.cs.umd.edu/~bhatele/pubs/pdf/2018/tvcg2018.pdf
		 - https://web.archive.org/web/20180921144846id_/http://inside.mines.edu:80/~bwu/CSCI_580_18FALL/a47-liu.pdf
		 - https://dl.acm.org/doi/abs/10.1145/2503210.2503297
		 - https://scholarship.rice.edu/bitstream/handle/1911/96369/TR08-06.pdf?sequence=1
		 - https://dl.acm.org/doi/10.1145/2588788
	3. Simulation _maybe merge with dynamic analysis_
		 - https://hpac.cs.umu.se/people/iakymchuk/pub/AICES-2011-07-01.pdf _this maybe is static analysis_
		 - https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6069452
		 - (https://link.springer.com/chapter/10.1007/978-3-319-56702-0_1)
	1. Static Analysis + 
		- Briefly explain [Boosting](References#Methods#Boosting Performance Optimization with Interactive  Data Movement Visualization)
		- Explain how it works (2 granularity approach) --> Focus on Data gathering
		- Briefly go into the visualization
2. Concrete Examples + Comparisons/Results
	- [Boosting](References#Methods#Boosting Performance Optimization with Interactive  Data Movement Visualization) is very good, as it combines visualizing performance data, exploring data reuse with data-centric analysis, or obtaining performance insights through simulation, at basically 0 cost. But not hardware specific, and requires parameter tweaking to work. Furthermore a limitation is, that it does not work well with dynamic programs (at least at the global view)
	- Further techniques that rely on execution (getting hardware counters) can verify currently made optimizations and can help to detect opportunities for further optimization based on specific hardware (architectures)
3. Conclusion
4. Outlook
 - Automatic Optimization (using heuristics), no visualizations, directly in compiler
 - ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations
 - https://arxiv.org/pdf/2112.11879.pdf

-> Lead up to [PDF](reference_pdfs/Boosting_Performance_Optimization_with_Interactive_Data_Movement_Visualization.pdf) (seems to be the best, see [References](References))