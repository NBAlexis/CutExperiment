import os
import numpy as np

#################################################################

k = 50
saveStart = 1
saveEnd = 10
energy = "15000"
readfileName = "FT0"


#################################################################

os.chdir("../../")

for n in range(0, 11):
    allList = []
    filehead = "_DataFolder/kmeans/{0}-{1}-{2}".format(readfileName, energy, n)
    for i in range(0, saveEnd - saveStart + 1):
        oneLine = np.loadtxt("{0}-{1}-{2}.csv".format(filehead, k, i + saveStart), delimiter=',')
        allList.append(oneLine.tolist())
    print(n, " finished")
    allArray = np.array(allList)
    np.savetxt("_DataFolder/kmeans/kmeans/E{0}/{1}/{1}-{0}-{2}-{3}-all.csv".format(energy, readfileName, k, n), allArray.astype(int), delimiter=',', fmt='%i')
