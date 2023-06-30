import os
import sys
from multiprocessing import Pool as ProcessPool

import process_image

def process(n_processes, n_threads, fnames):
    print(f"Controller with {n_processes} processes and {n_threads} threads / worker")

    # The environment that is set in the parent is inherited by child workers,
    # but here process_image import numpy, so we need to set the variable
    # before process_image is imported.
    os.environ['OMP_NUM_THREADS'] = str(n_threads)

    with ProcessPool(n_processes) as p:
        signatures = p.map(process_image.magic, fnames)
    for fname, signature in zip(fnames, signatures):
        print(f'{fname} → {signature}')

if __name__ == '__main__':
    n_processes = int(sys.argv[1])
    n_threads = int(sys.argv[2])
    fnames = sys.argv[3:]

    process(n_processes, n_threads, fnames)
