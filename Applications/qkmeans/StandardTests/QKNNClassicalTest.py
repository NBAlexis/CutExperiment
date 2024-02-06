import matplotlib.colors
import numpy as np
from matplotlib import pyplot as plt

folderHeader = "../../../_DataFolder/qkmeans/knn3d/"

totalk = 8
pttraing = np.loadtxt(folderHeader + "p3dk8traing.csv", delimiter=',')
ktraing = np.loadtxt(folderHeader + "k3dk8traing.csv", delimiter=',')
pts = np.loadtxt(folderHeader + "p3dk8test.csv", delimiter=',')
opts = np.loadtxt(folderHeader + "op3dk8test.csv", delimiter=',')

ktest = []

for i in range(0, len(pts)):
    dotsres = np.dot(np.array([pts[i]]), np.transpose(pttraing))
    dotsres = dotsres[0]
    dotsres = np.abs(dotsres * dotsres)
    if 0 == i:
        plt.hist(dotsres, bins=50)
        plt.show()
    nearest = np.argmax(dotsres)
    ktest.append(ktraing[nearest])
    # print("========")
    # print(pts[i])
    # print(pttraing[nearest])

ktest = np.array(ktest)

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating plot
for i in range(0, totalk):
    ax.scatter3D(opts[ktest == i, 0], opts[ktest == i, 1], opts[ktest == i, 2],
                marker='o',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / totalk, 1.0, 1.0])
                )
plt.title("simple 3D scatter plot")

# show plot
plt.show()

