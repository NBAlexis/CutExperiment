import numpy as np

pointset1 = "G:\\nTGCIF\\s025-6.csv"
pointset2 = "G:\\nTGCIF\\s025-10.csv"
testMax = -1
saveIdx = "G:\\nTGCIF\\Maps\\s025-6-idx.csv"
saveDist = "G:\\nTGCIF\\Maps\\s025-6-dist.csv"
bSaveDist = True


dataSet1 = np.loadtxt(pointset1, delimiter=',')
dataSet2 = np.loadtxt(pointset2, delimiter=',')
print("file loaded")
testMax = testMax if testMax > 0 else len(dataSet1)
mapList = []
distList = []
for i in range(0, testMax):
    arrayCopy = dataSet2 - dataSet1[i]
    arrayCopy = np.square(arrayCopy)
    sumres = np.sum(arrayCopy, 1)
    minIdx = np.argmin(sumres)
    dist = sumres[minIdx]
    print("{}/{} {}".format(i, testMax, dist))
    # print("p1:", dataSet1[i])
    # print("p2:", dataSet2[minIdx])
    mapList.append(minIdx)
    distList.append(dist)

np.savetxt(saveIdx, np.transpose(np.array(mapList).astype(int)), delimiter=',', fmt='%i')
if bSaveDist:
    np.savetxt(saveDist, np.transpose(np.array(distList)), delimiter=',')
