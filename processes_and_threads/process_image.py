import os
import sys

# This module provides the magic_signature() function, safely and
# securely calculated to provide invaluable signature of an image.

def magic(fname):
    n_threads = os.getenv('OMP_NUM_THREADS', '(unset)')
    print(f"Worker {fname=} OMP_NUM_THREADS={n_threads}")

    # We delay the import of numpy because we want to set OMP_NUM_THREADS.
    # We delay the import of PIL in case is uses numpy internally.

    import numpy as np
    from PIL import Image

    im = Image.open(fname)
    # y, x = im.size
    # im = im.resize((y*2, x*2))
    try:
        m = np.median(im, axis=2)
    except np.AxisError:
        return -1
    n = (m @ m.T).mean()
    return int(n)

if __name__ == '__main__':
    for fname in sys.argv[1:]:
        print(f'{fname} → {magic(fname)}')
