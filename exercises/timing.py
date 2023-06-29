import os
import timeit
import numpy as np

n = 6_000
print(f"OMP_NUM_THREADS={os.getenv('OMP_NUM_THREADS')} {n=}")

x = np.random.random(size=(n, n))

res = timeit.timeit('y = x @ x', number=1, globals={'x':x})
print(f'time: {res:.2f} s')
