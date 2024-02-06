import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

pts, _ = make_blobs(n_samples=2048,  # 500个样本
                    n_features=3,  # 每个样本2个特征
                    centers=8,  # 4个中心
                    cluster_std=1.0,
                    random_state=8  # 控制随机性
                    )

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

ax.scatter3D(pts[:, 0], pts[:, 1], pts[:, 2],
                marker='o',
                s=1
                )
plt.title("simple 3D scatter plot")
plt.show()

pts = pts / 10
pts = np.hstack((pts, np.ones((2048, 1)) * 10.0))
pts = pts / np.transpose(np.array([np.sum(pts * pts, axis=1)]))

x2 = np.linspace(-1, 1, 11)
y2 = np.linspace(-1, 1, 11)
z2 = np.linspace(-1, 1, 11)
xv, yv, zv = np.meshgrid(x2, y2, z2)
xv = xv.flatten()
yv = yv.flatten()
zv = zv.flatten()
ptgrid = np.hstack((
    np.transpose(np.array([xv])),
    np.transpose(np.array([yv])),
    np.transpose(np.array([zv])),
    np.ones((11**3, 1)) * 10.0
))
ptgrid = ptgrid / np.transpose(np.array([np.sum(ptgrid * ptgrid, axis=1)]))

def randomPhaseApproximation(v):
    v = v / np.sqrt(np.dot(v, v))
    dotresall = []
    for k in range(300):
        u = np.random.uniform(0, 2*np.pi, len(v))
        u = np.exp(1j * u) / np.sqrt(len(v))
        dotres2 = np.dot(v, u)
        dotresall.append(np.abs(dotres2))
    dotresall = np.array(dotresall)
    return np.max(dotresall)

scales = []
for i in range(len(ptgrid)):
    testv = np.transpose(np.array([ptgrid[i]]))
    dotres = np.dot(pts, testv)
    dotres = dotres.flatten()
    rpa = randomPhaseApproximation(dotres)
    scales.append(rpa)

scales = np.array(scales)
scales = scales / np.max(scales)
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

ax.scatter3D(xv, yv, zv,
                marker='o',
                c=scales,
                s=2
                )
plt.title("simple 3D scatter plot")
plt.show()


