import os
import sys
import time

from process_multiple_images import process

def measure_one(n_processes, n_threads, fnames):
    result_fname = f'{n_processes:02}_{n_threads:02}.txt'

    if os.path.exists(result_fname):
        print(f'Skipping job with {n_processes} processes and {n_threads} threads, results file exists')
        return

    t0 = time.time()
    process(n_processes, n_threads, fnames)
    dt = time.time() - t0

    print(f'Job with {n_processes} processes and {n_threads} threads/worker and {len(fnames)} jobs: {dt}')

    with open(result_fname, 'wt') as results:
        print(f'{n_processes:02} {n_threads:02} {dt}', file=results)

def measure(n_processes, n_threads, fnames):
    for n1 in n_processes:
        for n2 in n_threads:
            measure_one(n1, n2, fnames)

if __name__ == '__main__':
    measure(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        sys.argv[1:])
