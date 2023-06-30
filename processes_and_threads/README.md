`process_image.py` processes a single image.
It can be used as a script: `process_image.py foo.jpg`
It is also an importable module. `process_image.magic("foo.jpg")`

`process_multiple_images` uses `process_image` to process a series of images.
It should be called as following:
`process_multiple_images n_processes n_threads filename1.png filename2.png …`

0. `git pull`

1. start a separate terminal window with `htop`: `gnome-terminal -- htop &`

2. call `python process_multiple_images.py 2 2 images/*.png`

You should see `htop` showing 4 threads (2 worked processes × 2 numpy threads).

Play with different numbers of processes and threads.
Which combination is optimum (fastest)?
