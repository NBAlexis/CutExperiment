import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

numberOfK = 64
numberOfPoint = 4096

pts, k = make_blobs(n_samples=(2*numberOfPoint),  # 500个样本
                    n_features=2,  # 每个样本2个特征
                    centers=numberOfK,  # 4个中心
                    cluster_std=0.3,
                    random_state=11  # 控制随机性
                    )

for i in range(0, numberOfK):
    plt.scatter(pts[k == i, 0], pts[k == i, 1],
                marker='o',
                s=1
                )
plt.show()


folderHeader = "../../../_DataFolder/qkmeans/standard/"


np.savetxt(folderHeader + "p2dk{}traing.csv".format(numberOfK), pts[0:numberOfPoint], delimiter=',')
np.savetxt(folderHeader + "k2dk{}traing.csv".format(numberOfK), k[0:numberOfPoint], delimiter=',', fmt='%d')
np.savetxt(folderHeader + "p2dk{}test.csv".format(numberOfK), pts[numberOfPoint:(2*numberOfPoint)], delimiter=',')
np.savetxt(folderHeader + "k2dk{}test.csv".format(numberOfK), k[numberOfPoint:(2*numberOfPoint)], delimiter=',', fmt='%d')