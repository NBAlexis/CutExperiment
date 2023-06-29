import numpy as np
from matplotlib import pyplot as plt

from Applications.PCAAD.pcaadfunctions import ManualPCAData, ManualPCATransform2, ManualPCATransform

"""
critiron:

1500: 1.5
15000: 0.5
"""

energy = 15000
ft = 0
# critiron0 = 1.5
critiron1 = 3.0
critiron2 = 3.0
critiron3 = 3.0
critiron4 = 3.0
datasm = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(energy), delimiter=',')
datasm = datasm[:, 0:12]

means, stds, features = ManualPCAData(datasm, 4)

reslst = []

for i in range(0, 21):
    data2 = np.loadtxt("../../_DataFolder/kmeans/cs/E{1}/FT{2}/FT{2}-{1}-{0}.csv".format(i, energy, ft), delimiter=',')
    data2 = data2[:, 0:12]
    # data3 = np.copy(data2)
    # res = ManualPCATransform(data3, means, stds, features)
    # res0 = np.copy(res[:, 0])
    res = ManualPCATransform2(data2, means, stds, features)
    res1 = res[:, 0]
    res2 = res[:, 1]
    res3 = res[:, 2]
    res4 = res[:, 3]
    # reslst.append(len(res1[np.all(np.array([res0 > critiron0, res1 > critiron1, res2 > critiron2, res3 > critiron3]), axis=0)]))
    reslst.append(len(res1[np.all(np.array([res1 > critiron1, res2 > critiron2, res3 > critiron3, res4 > critiron4]), axis=0)]))

print(reslst)
plt.plot(reslst)
plt.show()






