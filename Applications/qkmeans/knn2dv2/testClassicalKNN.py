import os

import matplotlib.pyplot as plt
import numpy as np

os.chdir("../../../_DataFolder/qkmeans/knn2d")

pts = np.loadtxt("d2points.csv", delimiter=',')
pts2 = np.loadtxt("d2train.csv", delimiter=',')
testpts = np.loadtxt("d2testpoints.csv", delimiter=',')
testpts2 = np.loadtxt("d2test.csv", delimiter=',')

pts2 = np.hstack((np.transpose(np.array([pts2[:, 0] + pts2[:, 1] * 1j])), np.transpose(np.array([pts2[:, 2] + pts2[:, 3] * 1j]))))
testpts2 = np.hstack((np.transpose(np.array([testpts2[:, 0] + testpts2[:, 1] * 1j])), np.transpose(np.array([testpts2[:, 2] + testpts2[:, 3] * 1j]))))


clusters = []
for i in range(len(testpts2)):
    d1 = np.abs(np.dot(np.conjugate(pts2[0:64]), np.transpose(testpts2[i])))
    d2 = np.abs(np.dot(np.conjugate(pts2[64:128]), np.transpose(testpts2[i])))
    d3 = np.abs(np.dot(np.conjugate(pts2[128:192]), np.transpose(testpts2[i])))
    d4 = np.abs(np.dot(np.conjugate(pts2[192:256]), np.transpose(testpts2[i])))
    clusters.append(np.argmax(np.array([np.sum(d1 * d1), np.sum(d2 * d2), np.sum(d3 * d3), np.sum(d4 * d4)])))

clusters = np.array(clusters)


plt.scatter(testpts[clusters==0, 0], testpts[clusters==0, 1], c="darkred")
plt.scatter(testpts[clusters==1, 0], testpts[clusters==1, 1], c="darkgreen")
plt.scatter(testpts[clusters==2, 0], testpts[clusters==2, 1], c="darkblue")
plt.scatter(testpts[clusters==3, 0], testpts[clusters==3, 1], c="orange")

plt.scatter(pts[0:64, 0], pts[0:64, 1], c="red")
plt.scatter(pts[64:128, 0], pts[64:128, 1], c="green")
plt.scatter(pts[128:192, 0], pts[128:192, 1], c="blue")
plt.scatter(pts[192:256, 0], pts[192:256, 1], c="yellow")

plt.show()
np.savetxt("../knn2dv2/d2test-aeexact.csv", clusters, delimiter=',')

"""
pts = np.loadtxt("d2points.csv", delimiter=',')
testpts = np.loadtxt("d2testpoints.csv", delimiter=',')

clusters = []
for i in range(len(testpts)):
    d = testpts[i] - pts
    d = np.sum(d * d, axis=1)
    clusters.append(np.argmin(d) // 64)

clusters = np.array(clusters)


plt.scatter(testpts[clusters==0, 0], testpts[clusters==0, 1], c="darkred")
plt.scatter(testpts[clusters==1, 0], testpts[clusters==1, 1], c="darkgreen")
plt.scatter(testpts[clusters==2, 0], testpts[clusters==2, 1], c="darkblue")
plt.scatter(testpts[clusters==3, 0], testpts[clusters==3, 1], c="orange")

plt.scatter(pts[0:64, 0], pts[0:64, 1], c="red")
plt.scatter(pts[64:128, 0], pts[64:128, 1], c="green")
plt.scatter(pts[128:192, 0], pts[128:192, 1], c="blue")
plt.scatter(pts[192:256, 0], pts[192:256, 1], c="yellow")

plt.show()
np.savetxt("../knn2dv2/d2testknn.csv", clusters, delimiter=',')
"""

"""
res2 = np.loadtxt("d2test-ae.csv", delimiter=',')
res2 = np.argmin(res2, axis=1)
plt.scatter(testpts[res2==0, 0], testpts[res2==0, 1], c="darkred")
plt.scatter(testpts[res2==1, 0], testpts[res2==1, 1], c="darkgreen")
plt.scatter(testpts[res2==2, 0], testpts[res2==2, 1], c="darkblue")
plt.scatter(testpts[res2==3, 0], testpts[res2==3, 1], c="orange")

plt.scatter(pts[0:64, 0], pts[0:64, 1], c="red")
plt.scatter(pts[64:128, 0], pts[64:128, 1], c="green")
plt.scatter(pts[128:192, 0], pts[128:192, 1], c="blue")
plt.scatter(pts[192:256, 0], pts[192:256, 1], c="yellow")

plt.show()
"""

# plt.scatter(testpts[:, 0], testpts[:, 1])
# plt.show()

# print(pts)
# import numpy as np

# 假设这是我们的数组
# arr = np.array([12, 15, 3, 7, 14, 2, 8, 1])

# 要找的k个最小元素的个数
# k = 3

# 使用np.argpartition对数组进行分区
# 第k个最小元素将位于索引k-1的位置
# 我们取分区后的前k个元素，这些元素是数组中最小的k个元素
# 注意：这k个元素并不是排序的
# indices = np.argpartition(arr, k)[:k]

# 如果你还需要这k个元素的排序索引
# sorted_indices = indices[np.argsort(arr[indices])]

# print("最小的k个元素的索引（可能未排序）:", indices)
# print("最小的k个元素的索引（排序后）:", sorted_indices)
