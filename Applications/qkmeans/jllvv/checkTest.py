import os

import numpy as np
import matplotlib.pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

res = np.loadtxt("wf/test-16384-l5.csv", delimiter=',')
thresh = 0.15
ft0 = [-0.2 + 0.04 * i for i in range(0, 11)]
testcs = []
testcounts = [13940, 13570, 12953, 12686, 12637, 12180, 12297, 12671, 13067, 13612, 14383]
restcounts = []
nstart = 0
for c in testcounts:
    s = res[nstart:nstart+c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    restcounts.append(sAbove)
    nstart = nstart + c
restcounts = np.array(restcounts)

plt.plot(ft0, restcounts)
plt.show()
