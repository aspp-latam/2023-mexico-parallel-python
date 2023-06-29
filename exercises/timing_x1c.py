import numpy as np
from matplotlib import pyplot
import seaborn as sns

sns.set_context('talk')

results_x1c = np.array([
    1, 7.02,
    2, 4.07,
    3, 2.79,
    4, 2.17,
    5, 3.27,
    6, 2.79,
    7, 2.43,
    8, 2.24,
    9, 2.68,
    10, 2.44,
    11, 2.71,
    12, 3.05,
]).reshape(-1, 2)

fig, axes = pyplot.subplots()
pyplot.tight_layout()
axes.plot(results_x1c[:, 0], results_x1c[:, 1], '-*')
axes.set_xlabel('# threads')
axes.set_ylabel('time / s')
sns.despine(fig)
fig.show()
