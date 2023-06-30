import sys
import collections
import numpy as np

dts = collections.defaultdict(dict)

for fname in sys.argv[1:]:
    values = open(fname).read().split()
    n1 = int(values[0])
    n2 = int(values[1])
    dt = float(values[2])

    dts[n1][n2] = dt

print(dts)
N1 = max(dts)
N2 = max(max(v) for v in dts.values())

print(N1, N2)

x = np.empty((N1 + 1, N2 + 1))
for n1, values in dts.items():
    for n2, v in values.items():
        x[n1, n2] = v

x[:, 0] = np.nan
x[0, :] = np.nan

print(x)

from matplotlib import pyplot

fig, axes = pyplot.subplots()
im = axes.imshow(x, origin='lower')
axes.set_ylabel('# processes')
axes.set_xlabel('# threads')
axes.spines[['right', 'top']].set_visible(False)
axes.set_title('time')
fig.colorbar(im, ax=axes, label='s')

fig_small, axes = pyplot.subplots()
im = axes.imshow(x[:5, :5], origin='lower')
axes.set_ylabel('# processes')
axes.set_xlabel('# threads')
axes.spines[['right', 'top']].set_visible(False)
axes.set_title('time')
fig_small.colorbar(im, ax=axes, label='s')

workers = np.arange(N1 + 1)[:, None] * np.arange(N2 + 1)
speedup = x[1,1] / x

speedup[:, 0] = np.nan
speedup[0, :] = np.nan

figs, axes = pyplot.subplots()
im = axes.imshow(speedup, origin='lower')
axes.set_ylabel('# processes')
axes.set_xlabel('# threads')
axes.spines[['right', 'top']].set_visible(False)
axes.set_title('speedup')
figs.colorbar(im, ax=axes, label='s')

fig.savefig('time.svg')
fig_small.savefig('time_inset.svg')
figs.savefig('speedup.svg')

pyplot.show()
