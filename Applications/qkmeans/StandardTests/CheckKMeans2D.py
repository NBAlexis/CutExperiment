import matplotlib.colors
import numpy as np
from matplotlib import pyplot as plt

folderHeader = "../../../_DataFolder/qkmeans/knn2d/"

pts = np.loadtxt(folderHeader + "p2dk4test.csv", delimiter=',')
ks = np.loadtxt(folderHeader + "k2dtestres-16.csv", delimiter=',')
kshould = np.loadtxt(folderHeader + "k2dk4test.csv", delimiter=',')
pttraing = np.loadtxt(folderHeader + "p2dk4traing.csv", delimiter=',')
ktraing = np.loadtxt(folderHeader + "k2dk4traing.csv", delimiter=',')

totalk = 4

"""
x = [i for i in range(0, 64)]
y = [i for i in range(0, 64)]
cc = [matplotlib.colors.hsv_to_rgb([i / 64, 1.0, 1.0]) for i in range(0, 64)]
plt.scatter(x, y, c=cc)
plt.show()
"""

for i in range(0, totalk):
    plt.scatter(pts[ks == i, 0], pts[ks == i, 1],
                marker='x',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / totalk, 1.0, 1.0])
                )
plt.show()

for i in range(0, totalk):
    plt.scatter(pts[kshould == i, 0], pts[kshould == i, 1],
                marker='x',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / totalk, 1.0, 1.0])
                )
plt.show()
