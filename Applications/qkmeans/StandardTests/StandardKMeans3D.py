import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

numberOfK = 8
numberOfPoint = 2048

pts, k = make_blobs(n_samples=2*numberOfPoint,  # 500个样本
                    n_features=3,  # 每个样本2个特征
                    centers=numberOfK,  # 4个中心
                    cluster_std=1.0,
                    random_state=8  # 控制随机性
                    )

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating plot
for i in range(0, numberOfK):
    ax.scatter3D(pts[k == i, 0], pts[k == i, 1], pts[k == i, 2],
                marker='o',
                s=1
                )
plt.title("simple 3D scatter plot")

# show plot
plt.show()


folderHeader = "../../../_DataFolder/qkmeans/standard/"

means = np.mean(pts, axis=0)
stds = np.std(pts, axis=0)
pts2 = (pts - means) / stds
pts2 = np.hstack((pts2, np.ones((2*numberOfPoint, 1))))
for i in range(len(pts2)):
    lens = np.sqrt(np.dot(pts2[i], pts2[i]))
    pts2[i] = pts2[i] / lens

np.savetxt(folderHeader + "op3dk{}traing.csv".format(numberOfK), pts[0:numberOfPoint], delimiter=',')
np.savetxt(folderHeader + "op3dk{}test.csv".format(numberOfK), pts[numberOfPoint:(2*numberOfPoint)], delimiter=',')
np.savetxt(folderHeader + "p3dk{}traing.csv".format(numberOfK), pts2[0:numberOfPoint], delimiter=',')
np.savetxt(folderHeader + "p3dk{}test.csv".format(numberOfK), pts2[numberOfPoint:(2*numberOfPoint)], delimiter=',')
np.savetxt(folderHeader + "k3dk{}traing.csv".format(numberOfK), k[0:numberOfPoint], delimiter=',', fmt='%d')
np.savetxt(folderHeader + "k3dk{}test.csv".format(numberOfK), k[numberOfPoint:(2*numberOfPoint)], delimiter=',', fmt='%d')
