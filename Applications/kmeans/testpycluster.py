import numpy as np
from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils.metric import type_metric, distance_metric
from pyclustering.samples.definitions import FCPS_SAMPLES
from sklearn.datasets import make_blobs

# 使用sklearn的数据集
dpts, _ = make_blobs(n_samples=(2048),  # 500个样本
                     n_features=2,  # 每个样本2个特征
                     centers=4,  # 4个中心
                     cluster_std=0.4,
                     random_state=0  # 控制随机性
                     )

# 使用单个qubit的simple encoder
dptszscore = (dpts - np.mean(dpts, axis=0)) / (2 * np.std(dpts, axis=0))  # 2倍zscore
dptssimpleencode = np.transpose(np.vstack((
    np.cos(dptszscore[:, 0] * np.pi / 2) * np.exp(-1j * dptszscore[:, 1] * np.pi / 2),
    np.sin(dptszscore[:, 0] * np.pi / 2) * np.exp(1j * dptszscore[:, 1] * np.pi / 2))))

metricdata = np.abs(np.dot(np.conjugate(dptssimpleencode), np.transpose(dptssimpleencode)))


# 由于PyClustering的核K均值需要距离度量，我们使用核矩阵作为距离度量
# 创建一个用户定义的距离度量，该度量返回核矩阵中相应位置的值
def kernel_distance(a, b):
    print(a)
    return metricdata[int(a[0])][int(b[0])]


metric = distance_metric(type_metric.USER_DEFINED, func=kernel_distance)

# 使用kmeans++初始化中心
# initial_centers = kmeans_plusplus_initializer(dptszscore, 4).initialize()
# print(initial_centers)

# 为了使28行能正确执行，把矢量的内容换成index
indexarray = np.array([[n, dptssimpleencode[n][0], dptssimpleencode[n][1]] for n in range(len(dpts))])
print(indexarray)
kmeans_instance = kmeans(indexarray, indexarray[0:4, :], metric=metric)
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()

# 可视化结果
# kmeans_visualizer.show_clusters(dpts, clusters, initial_centers)
