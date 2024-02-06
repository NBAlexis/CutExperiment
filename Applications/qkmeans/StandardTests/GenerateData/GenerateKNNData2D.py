import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

folderHeader = "../../../../_DataFolder/qkmeans/knn2d/"


def exchangeToComplexArray(ptin):
    ptout = (ptin + 1) / 2
    ptout[:, 0] = ptout[:, 0] * np.pi / 2
    ptout[:, 1] = ptout[:, 1] * np.pi
    r1 = np.cos(ptout[:, 1]) * np.cos(ptout[:, 0])
    r2 = np.sin(ptout[:, 1]) * np.cos(ptout[:, 0])
    r3 = np.cos(ptout[:, 1]) * np.sin(ptout[:, 0])
    r4 = np.sin(-ptout[:, 1]) * np.sin(ptout[:, 0])
    r1 = np.transpose(np.array([r1]))
    r2 = np.transpose(np.array([r2]))
    r3 = np.transpose(np.array([r3]))
    r4 = np.transpose(np.array([r4]))
    return np.hstack((r1, r2, r3, r4))


pts, k = make_blobs(n_samples=1024,  # 500个样本
                    n_features=2,  # 每个样本2个特征
                    centers=4,  # 4个中心
                    cluster_std=0.4,
                    random_state=0  # 控制随机性
                    )

pt2 = None
for i in range(0, 4):
    xs = pts[k == i, 0]
    ys = pts[k == i, 1]
    pt2i = np.hstack((
        np.transpose(np.array([xs[0:64]])),
        np.transpose(np.array([ys[0:64]]))
    ))
    if 0 == i:
        pt2 = pt2i
    else:
        pt2 = np.vstack((pt2, pt2i))

mins = np.min(pt2, axis=0)
maxs = np.max(pt2, axis=0)
pt2 = 2 * (pt2 - mins) / (maxs - mins) - 1
pt2 = pt2 * 0.8

for i in range(0, 4):
    plt.scatter(pt2[(i * 64):((i + 1) * 64), 0], pt2[(i * 64):((i + 1) * 64), 1],
                marker='x',
                s=1,
                color=matplotlib.colors.hsv_to_rgb([i / 4, 1.0, 1.0])
                )
plt.show()

x2 = np.linspace(-0.99, 0.99, 100)
y2 = np.linspace(-0.99, 0.99, 100)
xv, yv = np.meshgrid(x2, y2)
xv = xv.flatten()
yv = yv.flatten()
ptgrid = np.hstack((np.transpose(np.array([xv])), np.transpose(np.array([yv]))))
plt.scatter(ptgrid[:, 0], ptgrid[:, 1],
            marker='x',
            s=1,
            )
plt.show()

pts1 = exchangeToComplexArray(pt2)
pts2 = exchangeToComplexArray(ptgrid)
np.savetxt(folderHeader + "d2points.csv", pt2, delimiter=',')
np.savetxt(folderHeader + "d2testpoints.csv", ptgrid, delimiter=',')
np.savetxt(folderHeader + "d2train.csv", pts1, delimiter=',')
np.savetxt(folderHeader + "d2test.csv", pts2, delimiter=',')

