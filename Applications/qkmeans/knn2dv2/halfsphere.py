import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/knn2d")

pts = np.loadtxt("d2points.csv", delimiter=',')
theta = np.linspace(-np.pi, np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# 计算球壳的坐标
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# 由于我们只需要半个球壳，我们只考虑z >= 0的部分
# 我们可以通过将z < 0的部分设为NaN来实现
# z[z < 0] = np.nan

# 创建3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制球壳
ax.plot_surface(x, y, z, color='c', linewidth=0.5, alpha=0.1, edgecolor=(0, 0, 0, 0.1))

theta = pts[:, 0] * np.pi / 2
phi = pts[:, 1] * np.pi
ax.scatter(np.sin(theta[0:64]) * np.cos(phi[0:64]), np.sin(theta[0:64]) * np.sin(phi[0:64]), np.cos(theta[0:64]))
ax.scatter(np.sin(theta[64:128]) * np.cos(phi[64:128]), np.sin(theta[64:128]) * np.sin(phi[64:128]), np.cos(theta[64:128]))
ax.scatter(np.sin(theta[128:192]) * np.cos(phi[128:192]), np.sin(theta[128:192]) * np.sin(phi[128:192]), np.cos(theta[128:192]))
ax.scatter(np.sin(theta[192:256]) * np.cos(phi[192:256]), np.sin(theta[192:256]) * np.sin(phi[192:256]), np.cos(theta[192:256]))

# 设置图形的标签和视角
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.view_init(elev=45, azim=-120)  # 设置视角

# 显示图形
plt.show()