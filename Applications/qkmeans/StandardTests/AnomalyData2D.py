import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

x1, y1 = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 2048).T
ptgaussian = np.hstack((np.transpose(np.array([x1])), np.transpose(np.array([y1]))))

plt.scatter(x1, y1, s=1)
plt.show()

pts, _ = make_blobs(n_samples=(2048),  # 500个样本
                    n_features=2,  # 每个样本2个特征
                    centers=16,  # 4个中心
                    cluster_std=0.5,
                    random_state=11  # 控制随机性
                    )
pts = pts / 2.5
plt.scatter(pts[:, 0], pts[:, 1], s=1)
plt.show()

x2 = np.linspace(-5, 5, 101)
y2 = np.linspace(-5, 5, 101)
xv, yv = np.meshgrid(x2, y2)
xv = xv.flatten()
yv = yv.flatten()
ptgrid = np.hstack((np.transpose(np.array([xv])), np.transpose(np.array([yv]))))

plt.scatter(xv, yv, s=1)
plt.show()

folderHeader = "../../../_DataFolder/qkmeans/buildratetest/"

np.savetxt(folderHeader + "p2gaussian.csv", ptgaussian, delimiter=',')
np.savetxt(folderHeader + "p2grid.csv", ptgrid, delimiter=',')
np.savetxt(folderHeader + "p2multi.csv", pts, delimiter=',')

