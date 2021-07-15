import numpy as np

saveNames = ["G:\\ifres\\original\\a0-hist1-", "G:\\ifres\\original\\a0-hist2-", "G:\\ifres\\original\\a0-hist3-", "G:\\ifres\\original\\a0-hist4-", "G:\\ifres\\original\\a0-hist5-"]
Loop = 100
fileNames = []
saveMean = False

for saveName in saveNames:
    for i in range(0, Loop):
        fileNames.append(saveName + str(i) + ".csv")

toSave = None


# """
# history
for i in range(0, len(fileNames)):
    print("adding {} / {}".format(i, len(fileNames)))
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
    np.savetxt("G:\\ifres\\comb\\a0-mean.csv", meanArray, delimiter=',')

np.savetxt("G:\\ifres\\comb\\a0-hist1-0-99.csv", toSave.astype(int), delimiter=',', fmt='%i')

# """

# """
# mean


# “”“