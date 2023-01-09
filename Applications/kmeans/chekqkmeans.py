import os

import numpy as np
from matplotlib import pyplot as plt

ite = 87
smallsize = 0.1
largesize = 20.0
ptcount = 29356
kcount = 64
filename = "FT0-1500-0"

os.chdir("../../")
points = np.loadtxt("_DataFolder/kmeans/cs/csq/{0}.csv".format(filename), delimiter=',')
points = points[0:ptcount]

centers = np.loadtxt("_DataFolder/kmeans/qkmeans/{0}_c_{1}.csv".format(filename, ite), delimiter=',')
ks = np.loadtxt("_DataFolder/kmeans/qkmeans/{0}_k_{1}.csv".format(filename, ite), delimiter=',').astype(int)
ms = np.loadtxt("_DataFolder/kmeans/qkmeans/{0}_m_{1}.csv".format(filename, ite), delimiter=',').astype(int)


plt.scatter(points[:, 0], points[:, 1], s=smallsize, c=ks)
plt.scatter(centers[:, 0], centers[:, 1], s=largesize, edgecolors='k', c=range(0, kcount))
plt.show()
plt.scatter(points[:, 1], points[:, 4], s=smallsize, c=ks)
plt.scatter(centers[:, 1], centers[:, 4], s=largesize, edgecolors='k', c=range(0, kcount))
plt.show()
plt.scatter(points[:, 2], points[:, 5], s=smallsize, c=ks)
plt.scatter(centers[:, 2], centers[:, 5], s=largesize, edgecolors='k', c=range(0, kcount))
plt.show()
plt.scatter(points[:, 3], points[:, 6], s=smallsize, c=ks)
plt.scatter(centers[:, 3], centers[:, 6], s=largesize, edgecolors='k', c=range(0, kcount))
plt.show()
plt.hist(ms, 50)
plt.show()
print(np.mean(ms))


"""
for i in range(0, kcount):
    pttype0 = points[ks == i, :]
    pttype0x = pttype0[:, 1]
    pttype0y = pttype0[:, 4]
    plt.hist2d(pttype0x, pttype0y, [50, 50])
    plt.show()
"""