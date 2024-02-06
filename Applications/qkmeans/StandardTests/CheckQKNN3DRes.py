import matplotlib.colors
import numpy as np
from matplotlib import pyplot as plt

folderHeader = "../../../_DataFolder/qkmeans/knn3d/"

pts = np.loadtxt(folderHeader + "op3dk8test.csv", delimiter=',')
ks = np.loadtxt(folderHeader + "k3dtestres-32.csv", delimiter=',')
kshould = np.loadtxt(folderHeader + "k3dk8test.csv", delimiter=',')

totalk = 8

"""
x = [i for i in range(0, 64)]
y = [i for i in range(0, 64)]
cc = [matplotlib.colors.hsv_to_rgb([i / 64, 1.0, 1.0]) for i in range(0, 64)]
plt.scatter(x, y, c=cc)
plt.show()
"""

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating plot
for i in range(0, totalk):
    ax.scatter3D(pts[ks == i, 0], pts[ks == i, 1], pts[ks == i, 2],
                marker='o',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / totalk, 1.0, 1.0])
                )
plt.title("simple 3D scatter plot")

# show plot
plt.show()

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

for i in range(0, totalk):
    ax.scatter3D(pts[kshould == i, 0], pts[kshould == i, 1], pts[kshould == i, 2],
                marker='o',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / totalk, 1.0, 1.0])
                )
plt.title("simple 3D scatter plot")

# show plot
plt.show()
