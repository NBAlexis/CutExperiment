from random import randint, uniform
import numpy as np


def PrepareArray(dataArray):
    return np.insert(dataArray, 0, np.arange(0, len(dataArray)), 1)


# Expecting N = len(-)
# data[:, 0] is order
# data[:, 1-N] is attribute
# data[:, N+1] is tag
# data[:, N+2] is tree depth
def OneSplit(theArray, length: int):
    if len(theArray) < 3:
        print("Error: length < 3")
        return
    depth = theArray[0, length + 2]
    l = 0
    while 0 == l:
        idx = 1 + randint(0, length - 1)
        minV = np.min(theArray[:, idx])
        maxV = np.max(theArray[:, idx])
        midV = uniform(minV, maxV)
        array1 = theArray[theArray[:, idx] > midV]
        array2 = theArray[theArray[:, idx] <= midV]
        array1[:, length + 2] = depth + 1
        array2[:, length + 2] = depth + 1
        l = len(array1) * len(array2)
        print("retry: {} to {} {} idx:{} v:{} min:{} max:{}".format(len(theArray), len(array1), len(array2), idx, midV, minV, maxV))
        print(theArray)
    print("Split {} to {} {} with idx:{} v:{} depth:{}".format(len(theArray), len(array1), len(array2), idx, midV, depth))
    return [array1, array2]


def Split(dataArray, length: int, maxSplit: int):
    dataArrayPrepared = PrepareArray(dataArray)
    arrayLst = [dataArrayPrepared]
    resArray = None
    step = 1
    while len(arrayLst) > 0 and (maxSplit < 0 or step < maxSplit):
        print("========== {} ===========".format(len(arrayLst)))
        toSplit = randint(0, len(arrayLst) - 1)
        toSplitArray = arrayLst.pop(toSplit)
        splitList = OneSplit(toSplitArray, length)
        if 2 == len(splitList):
            for retArray in splitList:
                if len(retArray) > 2:
                    arrayLst.append(retArray)
                elif len(retArray) == 2:
                    depth = retArray[0, length + 2]
                    retArray[0, length + 2] = depth + 1
                    retArray[1, length + 2] = depth + 1
                    if resArray is None:
                        resArray = retArray
                    else:
                        resArray = np.append(resArray, retArray, 0)
                else:
                    if resArray is None:
                        resArray = retArray
                    else:
                        resArray = np.append(resArray, retArray, 0)
        else:
            print("Error: return of OneSplit is not 2")
        step = step + 1
    for leftArray in arrayLst:
        resArray = np.append(resArray, leftArray, 0)
    orders = np.argsort(resArray[:, 0])
    resArray = resArray[orders]
    return np.delete(resArray, 0, 1)


dataSet = np.loadtxt("a0.csv", delimiter=',')
resSet = Split(dataSet, 18, -1)
np.savetxt('a0-res1.csv', resSet, delimiter=',', fmt='%.8f')


