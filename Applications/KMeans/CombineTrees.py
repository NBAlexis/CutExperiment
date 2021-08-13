import numpy as np

saveNames = ["G:\\ifres\\newcomb\\a3-n4-hist-"]
LoopStart = 0
Loop = 5
fileNames = []
saveMean = True

for saveName in saveNames:
    for i in range(LoopStart, Loop):
        fileNames.append(saveName + str(i) + ".csv")

toSave = None


# """
# history
for i in range(0, len(fileNames)):
    print("adding {} : {} / {}".format(fileNames[i], i, len(fileNames)))
    dataSet = np.loadtxt(fileNames[i], delimiter=',')
    if toSave is None:
        toSave = dataSet
    else:
        toSave = np.append(toSave, dataSet[:, 1:dataSet.shape[1]], 1)

if saveMean:
    typeOfPoints = toSave[:, 0].astype(float)
    depthOfPoints = toSave[:, 1:toSave.shape[1]].astype(float)
    depthMean = np.mean(depthOfPoints, 1)
    meanArray = np.transpose(np.array([typeOfPoints.tolist(), depthMean.tolist()]))
    np.savetxt("G:\\ifres\\newcomb\\a3-n4-mean.csv", meanArray, delimiter=',')

np.savetxt("G:\\ifres\\newcomb\\a3-n4-hist.csv", toSave.astype(int), delimiter=',', fmt='%i')

# """

# """
# mean


# “”“