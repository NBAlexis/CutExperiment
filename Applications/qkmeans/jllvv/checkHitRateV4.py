import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/jllvv/")
h = np.loadtxt("wfv7/hitv7-16384-l10-5000-01.csv", delimiter=',')
validationcounts = [30000, 30000, 13472, 16245, 12272, 30000, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697]

plt.hist(h[0:60000+13472], bins=50, histtype='step')
plt.hist(h[60000+13472:], bins=50, histtype='step')
plt.show()

print(np.mean(h))
print(np.mean(h[:60000+13472]))
print(np.mean(h[60000+13472:]))

"""
0.13162318595742448
0.05842603305
0.17100931574699343
"""