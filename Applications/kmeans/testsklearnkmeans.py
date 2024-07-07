import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import pairwise_kernels
from tslearn.clustering import KernelKMeans

k = 4
X, y = make_blobs(n_samples=2048,  # 500个样本
                  n_features=2,  # 每个样本2个特征
                  centers=k,  # 4个中心
                  cluster_std=0.4,
                  random_state=0  # 控制随机性
                  )

print(y)

# 数据预处理，例如使用 MinMaxScaler 进行标准化
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 计算核矩阵
# 使用单个qubit的simple encoder
dptszscore = (X - np.mean(X, axis=0)) / (4 * np.std(X, axis=0))  # 4倍zscore
dptssimpleencode = np.transpose(np.vstack((
    np.cos(dptszscore[:, 0] * np.pi / 2) * np.exp(-1j * dptszscore[:, 1] * np.pi / 2),
    np.sin(dptszscore[:, 0] * np.pi / 2) * np.exp(1j * dptszscore[:, 1] * np.pi / 2))))

kernel_matrix = np.abs(np.dot(np.conjugate(dptssimpleencode), np.transpose(dptssimpleencode)))
pwk = pairwise_kernels(kernel_matrix, metric="precomputed")

tskmeans = KernelKMeans(n_clusters=k, kernel=pwk, random_state=0)
tskmeans.fit(X)

for i in range(k):
    ptsshow = X[i == tskmeans.labels_]
    plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)

plt.show()

