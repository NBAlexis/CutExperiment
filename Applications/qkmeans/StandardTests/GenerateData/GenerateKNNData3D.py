import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

# random state = 6,10,16,27
pts, k = make_blobs(n_samples=4096,  # 500个样本
                        n_features=3,  # 每个样本2个特征
                        centers=8,  # 4个中心
                        cluster_std=1.0,
                        random_state=10  # 控制随机性
                        )

pt2 = None
for i in range(0, 8):
    xs = pts[k == i, 0]
    ys = pts[k == i, 1]
    zs = pts[k == i, 2]
    pt2i = np.hstack((
        np.transpose(np.array([xs[0:64]])),
        np.transpose(np.array([ys[0:64]])),
        np.transpose(np.array([zs[0:64]]))
    ))
    if 0 == i:
        pt2 = pt2i
    else:
        pt2 = np.vstack((pt2, pt2i))

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

for i in range(0, 8):
    ax.scatter3D(pt2[(i * 64):((i + 1) * 64), 0], pt2[(i * 64):((i + 1) * 64), 1], pt2[(i * 64):((i + 1) * 64), 2],
        marker='o',
        s=1
        )
plt.title("simple 3D scatter plot: ")
plt.show()

pt3 = pts[2048:4096, :]
kright = k[2048:4096]
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

ax.scatter3D(pt3[:, 0], pt3[:, 1], pt3[:, 2],
        marker='o',
        s=1
        )
plt.title("simple 3D scatter plot: ")
plt.show()

means = np.mean(pt2, axis=0)
stds = np.std(pt2, axis=0)

pt2 = (pt2 - means) / stds
pt3 = (pt3 - means) / stds
pt2 = np.hstack((pt2, np.ones((512, 1))))
pt3 = np.hstack((pt3, np.ones((2048, 1))))

norms2 = np.sqrt(np.sum(pt2 * pt2, axis=1))
norms3 = np.sqrt(np.sum(pt3 * pt3, axis=1))
norms2 = np.transpose(np.array([norms2]))
norms3 = np.transpose(np.array([norms3]))
pt2 = pt2 / norms2
pt3 = pt3 / norms3
print(pt2)


"""
x2 = np.linspace(-4, 4, 11)
y2 = np.linspace(-4, 4, 11)
z2 = np.linspace(-4, 4, 11)
xv, yv, zv = np.meshgrid(x2, y2, z2)
xv = xv.flatten()
yv = yv.flatten()
zv = zv.flatten()

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

ax.scatter3D(xv, yv, zv,
             marker='o',
             s=1
             )
plt.show()



mx = np.mean(x)
my = np.mean(y)
mz = np.mean(z)
sx = np.std(x)
sy = np.std(y)
sz = np.std(z)

x = (x - mx) / sx
y = (y - my) / sy
z = (z - mz) / sz
xv = (xv - mx) / sx
yv = (yv - my) / sy
zv = (zv - mz) / sz

opts1 = np.hstack((
    np.transpose(np.array([x])),
    np.transpose(np.array([y])),
    np.transpose(np.array([z]))
))

pts1 = np.hstack((
    np.transpose(np.array([x])),
    np.transpose(np.array([y])),
    np.transpose(np.array([z])),
    np.ones((len(x), 1))
))

opts2 = np.hstack((
    np.transpose(np.array([xv])),
    np.transpose(np.array([yv])),
    np.transpose(np.array([zv]))
))

pts2 = np.hstack((
    np.transpose(np.array([xv])),
    np.transpose(np.array([yv])),
    np.transpose(np.array([zv])),
    np.ones((len(xv), 1))
))

for i in range(len(pts1)):
    lens = np.sqrt(np.dot(pts1[i], pts1[i]))
    pts1[i] = pts1[i] / lens

for i in range(len(pts2)):
    lens = np.sqrt(np.dot(pts2[i], pts2[i]))
    pts2[i] = pts2[i] / lens

folderHeader = "../../../../_DataFolder/qkmeans/knn3d/"

np.savetxt(folderHeader + "p3gaussian.csv", pts1, delimiter=',')
np.savetxt(folderHeader + "p3grid.csv", pts2, delimiter=',')
np.savetxt(folderHeader + "op3gaussian.csv", opts1, delimiter=',')
np.savetxt(folderHeader + "op3grid.csv", opts2, delimiter=',')
"""