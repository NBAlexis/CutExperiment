import numpy as np
from matplotlib import pyplot as plt

from Applications.PCAAD.pcaadfunctions import ManualPCAData, ManualPCATransform2

"""
critiron:

1500: 1.5
15000: 0.5
"""

energy = 15000
ft = 0
critiron1 = 3.0
critiron2 = 3.0
critiron3 = 3.0
datasm = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(energy), delimiter=',')
datasm = datasm[:, 0:12]

means, stds, features = ManualPCAData(datasm, 3)

reslst = []

for i in range(0, 21):
    data2 = np.loadtxt("../../_DataFolder/kmeans/cs/E{1}/FT{2}/FT{2}-{1}-{0}.csv".format(i, energy, ft), delimiter=',')
    data2 = data2[:, 0:12]
    res = ManualPCATransform2(data2, means, stds, features)
    res1 = res[:, 0]
    res2 = res[:, 1]
    res3 = res[:, 2]
    reslst.append(len(res1[np.all(np.array([res1 > critiron1, res2 > critiron2, res3 > critiron3]), axis=0)]))

print(reslst)
plt.plot(reslst)
plt.show()






