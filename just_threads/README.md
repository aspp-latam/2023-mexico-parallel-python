This folder contains two scripts:

`timing.py` which does some heavy computations, letting numpy its
built-in threading support to parallelize.

OMP_NUM_THREADS can be used to override the number of threads used, e.g.:
OMP_NUM_THREADS=5 python timing.py

`timing_plot.py` can be used to plot a graph of execution speedup vs. the number of threads.

Run `timing.py` with different values of `OMP_NUM_THREADS`,
fill in the `results` array in `timing_plot.py`.

What does the result tell us about the optimum number of threads?
What is the architecture of the processor?
