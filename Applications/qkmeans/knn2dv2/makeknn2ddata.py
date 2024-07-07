import os

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

os.chdir("../../../_DataFolder/qkmeans/knn2dv2")

"""
good examples:
0
6
9
"""
feature = 16
pointnum = 2048
randomstate = 9

def sortlst(pt, asigny, allk):
    ret = None
    for i in range(allk):
        if 0 == i:
            ret = pt[asigny == i]
        else:
            ret = np.vstack((ret, pt[asigny == i]))
    return ret

def norm1(pt):
    ptmean = np.means(pt, axis=0)
    ptstd = np.std(pt, axis=0)
    return (pt - ptmean) / ptstd


def norm2(pt):
    ptsl = np.min(pt, axis=0)
    ptsr = np.max(pt, axis=0)
    ret = 2 * (pts - ptsl) / (ptsr - ptsl) - 1
    ret = ret * 0.9
    ret = (ret + 1) / 2
    return ret


def valid1():
    ret = np.array([[[-1.99 + 0.02 * x, -1.99 + 0.02 * y] for x in range(200)] for y in range(200)])
    return np.reshape(ret, (40000, 2))


def valid2():
    ret = np.array([[[0.0025 + 0.005 * x, 0.0025 + 0.005 * y] for x in range(200)] for y in range(200)])
    return np.reshape(ret, (40000, 2))


def tocomplex1(pt):
    pt2 = np.hstack((pt, np.ones((pointnum, 1))))
    ptsnorm = np.sqrt(np.sum(pt2 * pt2, axis=1))
    pt2 = np.transpose(np.transpose(pt2) / ptsnorm)
    return np.hstack((pt2, np.zeros((pointnum, 1))))


def tocomplex2(pt):
    theta = pt[:, 0] * np.pi / 2
    phi = pt[:, 1] * np.pi
    r1 = np.cos(phi) * np.cos(theta)
    r2 = np.sin(phi) * np.cos(theta)
    r3 = np.cos(phi) * np.sin(theta)
    r4 = np.sin(-phi) * np.sin(theta)
    return np.transpose(np.array([r1, r2, r3, r4]))


pts, y = make_blobs(n_samples=(pointnum),  # 500个样本
                    n_features=2,  # 每个样本2个特征
                    centers=feature,  # 4个中心
                    cluster_std=0.4,
                    random_state=randomstate  # 控制随机性
                    )

pts = sortlst(pts, y, feature)
pts = norm2(pts)

everyk = pointnum // feature
for k in range(feature):
    ptsshow = pts[k*everyk:(k+1)*everyk]
    print(len(ptsshow))
    plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)

plt.show()

"""
cond1 = (y >= 0)
cond2 = (y <= 3)
cond3 = np.all((cond1, cond2), axis=0)
ptsshow = pts[cond3]
plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)

cond1 = (y >= 4)
cond2 = (y <= 7)
cond3 = np.all((cond1, cond2), axis=0)
ptsshow = pts[cond3]
plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)

cond1 = (y >= 8)
cond2 = (y <= 11)
cond3 = np.all((cond1, cond2), axis=0)
ptsshow = pts[cond3]
plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)

cond1 = (y >= 12)
cond2 = (y <= 15)
cond3 = np.all((cond1, cond2), axis=0)
ptsshow = pts[cond3]
plt.scatter(ptsshow[:, 0], ptsshow[:, 1], s=1)
plt.show()
"""

np.savetxt("points.csv", pts, delimiter=',')
np.savetxt("training.csv", tocomplex2(pts), delimiter=',')

validationpoints = valid2()
plt.scatter(validationpoints[:, 0], validationpoints[:, 1], s=0.1)
plt.show()

np.savetxt("validationpoints.csv", validationpoints, delimiter=',')
np.savetxt("validation.csv", tocomplex2(validationpoints), delimiter=',')
