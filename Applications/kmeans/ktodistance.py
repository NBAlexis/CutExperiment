import os
import numpy as np

#################################################################
from Applications.kmeans.kmeansfunctions import HistoryMean, CalculateDistanceD, CalculateCenterListD
from CutAndExport.Histogram import HistogramWithMinMaxList

k = 10
readfileName = "FT0-15000"
historyCheck = [0, 1, 600000, 600001]

#################################################################
os.chdir("../../")
dim = 12
data = np.loadtxt("_DataFolder/kmeans/{0}.csv".format(readfileName), delimiter=',')
kmeansData = np.loadtxt("_DataFolder/kmeans/{0}-{1}-all.csv".format(readfileName, k), delimiter=',')




distanceAll = []
for i in range(0, len(kmeansData)):
    data[:, dim] = kmeansData[i, :]
    centersAll = CalculateCenterListD(data, dim, k)
    distanceAll.append(CalculateDistanceD(data, dim, centersAll))

distanceAllArray = np.array(distanceAll)

allMean = np.mean(distanceAllArray, axis=0)
np.savetxt("_DataFolder/kmeans/{0}-{1}-meandist.csv".format(readfileName, k), allMean, delimiter=',', fmt='%f')

smDistance = allMean[0:600000]
npDistance = allMean[600000:630000]

historyList = []
for idx in historyCheck:
    oneLine = distanceAllArray[:, idx]
    historyList.append(HistoryMean(oneLine))

historyArray = np.array(historyList)
np.savetxt("_DataFolder/kmeans/{0}-{1}-hist.csv".format(readfileName, k), historyArray, delimiter=',', fmt='%f')

print(np.max(smDistance))
print(np.max(npDistance))
res1 = HistogramWithMinMaxList(smDistance, [2000, 20000], 50)
print(res1.listCount)
res2 = HistogramWithMinMaxList(npDistance, [2000, 20000], 50)
print(res2.listCount)
