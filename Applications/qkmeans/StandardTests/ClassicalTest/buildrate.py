import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

folderHeader = "../../../../_DataFolder/qkmeans/buildratetest/"

res = np.loadtxt(folderHeader + 'br1.csv', delimiter=',')
res = np.transpose(res)
res = res.reshape((9, 1000))
left = 0.5
thresh = 0.8
p99count = []

for i in range(0, 9):
    dataset = res[i, :]
    res1 = np.histogram(dataset, bins=50,  range=[left, 1])[0].tolist()
    res1.append(res1[len(res1) - 1])
    print(res1)
    plt.hist(dataset, bins=50)
    plt.show()
    dataset = dataset[dataset > thresh]
    p99count.append(len(dataset))

res = np.loadtxt(folderHeader + 'br2.csv', delimiter=',')
res = np.transpose(res)
res = res.reshape((3, 1000))

for i in range(0, 3):
    dataset = res[i, :]
    res1 = np.histogram(dataset, bins=50,  range=[left, 1])[0].tolist()
    res1.append(res1[len(res1) - 1])
    print(res1)
    plt.hist(dataset, bins=50)
    plt.show()
    dataset = dataset[dataset > thresh]
    p99count.append(len(dataset))

print(p99count)


