import os
import timeit
import numpy as np

threads = os.getenv('OMP_NUM_THREADS', '(unset)')
n = 6_000

print(f"We are executed with OMP_NUM_THREADS={threads} for {n=}")

x = np.random.random(size=(n, n))

# Why do we do the timings internally, instead of using 'time python timing.py'?
# We want to measure only the last part. The setup that is done above (generation
# of random numbers) is quite slow, and we want to exclude it from the time
# measurement. Hence, we use timeit.

res = timeit.timeit('y = x @ x', number=1, globals={'x':x})
print(f'time used for matrix multiplication: {res:.2f} s')
