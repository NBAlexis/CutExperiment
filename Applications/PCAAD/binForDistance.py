import numpy as np

from Applications.PCAAD.pcaadfunctions import ManualPCAData, ManualPCATransform2
from CutAndExport.Histogram import HistogramWithMinMaxList

energy = 1500
data1 = np.loadtxt("../../_DataFolder/kmeans/cs/SM/SM-{0}.csv".format(energy), delimiter=',')
data1 = data1[:, 0:12]
data2 = np.loadtxt("../../_DataFolder/kmeans/cs/FT0/FT0-{0}.csv".format(energy), delimiter=',')
data2 = data2[:, 0:12]

means, stds, features = ManualPCAData(np.copy(data1), 4)
distance3sm = ManualPCATransform2(data1, means, stds, features)
distance3np = ManualPCATransform2(data2, means, stds, features)

res1 = HistogramWithMinMaxList(distance3sm[:, 0].tolist(), [0, 8], 40)
print(res1.listCount)
res2 = HistogramWithMinMaxList(distance3np[:, 0].tolist(), [0, 8], 40)
print(res2.listCount)

res1 = HistogramWithMinMaxList(distance3sm[:, 1].tolist(), [0, 8], 40)
print(res1.listCount)
res2 = HistogramWithMinMaxList(distance3np[:, 1].tolist(), [0, 8], 40)
print(res2.listCount)

res1 = HistogramWithMinMaxList(distance3sm[:, 2].tolist(), [0, 8], 40)
print(res1.listCount)
res2 = HistogramWithMinMaxList(distance3np[:, 2].tolist(), [0, 8], 40)
print(res2.listCount)

res1 = HistogramWithMinMaxList(distance3sm[:, 3].tolist(), [0, 8], 40)
print(res1.listCount)
res2 = HistogramWithMinMaxList(distance3np[:, 3].tolist(), [0, 8], 40)
print(res2.listCount)





