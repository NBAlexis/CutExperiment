import matplotlib.pyplot as plt
import numpy as np

x, y, z = np.random.multivariate_normal([0, 0, 0], [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 2048).T

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

ax.scatter3D(x, y, z,
             marker='o',
             s=1
             )
plt.show()

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

folderHeader = "../../../_DataFolder/qkmeans/buildratetest/"

np.savetxt(folderHeader + "p3gaussian.csv", pts1, delimiter=',')
np.savetxt(folderHeader + "p3grid.csv", pts2, delimiter=',')
np.savetxt(folderHeader + "op3gaussian.csv", opts1, delimiter=',')
np.savetxt(folderHeader + "op3grid.csv", opts2, delimiter=',')
