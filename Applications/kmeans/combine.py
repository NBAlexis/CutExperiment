import os
import numpy as np

#################################################################

k = 10
saveStart = 1
saveEnd = 100
readfileName = "FT0-15000"


#################################################################

os.chdir("../../")

allList = []
for i in range(0, saveEnd - saveStart + 1):
    oneLine = np.loadtxt("_DataFolder/kmeans/{0}-{1}-{2}.csv".format(readfileName, k, i + saveStart), delimiter=',')
    allList.append(oneLine.tolist())
    print(i, " finished")

allArray = np.array(allList)
np.savetxt("_DataFolder/kmeans/{0}-{1}-all.csv".format(readfileName, k), allArray.astype(int), delimiter=',', fmt='%i')
