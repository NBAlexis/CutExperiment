import random
import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType


def ChooseEventWithStratege(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        secondPhotonIndex = -1
        secondPhotonEnergy = 0
        thirdPhotonIndex = -1
        thirdPhotonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Photon:
                PhotonEnergy = theParticle.momentum.Momentum()
                if PhotonEnergy > largestPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = largestPhotonIndex
                    secondPhotonEnergy = largestPhotonEnergy
                    largestPhotonIndex = theParticle.index - 1
                    largestPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > secondPhotonEnergy:
                    thirdPhotonIndex = secondPhotonIndex
                    thirdPhotonEnergy = secondPhotonEnergy
                    secondPhotonIndex = theParticle.index - 1
                    secondPhotonEnergy = PhotonEnergy
                elif PhotonEnergy > thirdPhotonEnergy:
                    thirdPhotonIndex = theParticle.index - 1
                    thirdPhotonEnergy = PhotonEnergy
        if largestPhotonIndex >= 0 and secondPhotonIndex >= 0 and thirdPhotonIndex >= 0:
            toAdd = theEvent.particles[largestPhotonIndex].momentum.values
            toAdd = toAdd + theEvent.particles[secondPhotonIndex].momentum.values
            toAdd = toAdd + theEvent.particles[thirdPhotonIndex].momentum.values
            toAdd = toAdd + [tag]
            result.append(toAdd)
        idx = idx + 1
    return result


def SaveCSVFile(fileName: str, content: list):
    with open(fileName, 'w') as f:
        for line in content:
            for i in range(0, 13):
                if i == 12:
                    f.write(str(line[i]) + "\n")
                else:
                    f.write(str(line[i]) + ", ")


def InitialClassify(dataList, dimension: int, typeCount: int):
    dataList[:, dimension] = np.random.randint(0, typeCount, len(dataList))


def SplitLargestClass(dataList, dimension: int, largestClass: int, missingClasses):
    oldClasses = dataList[:, dimension]
    newClasses = np.copy(oldClasses)
    newClasses[newClasses == largestClass] = -1
    newClasses[newClasses >= 0] = 0
    splitClasses = np.random.randint(0, len(missingClasses), len(dataList))
    splitClasses = missingClasses[splitClasses]
    newClasses = -newClasses * splitClasses + (1 + newClasses) * oldClasses
    dataList[:, dimension] = newClasses


def RandomCenterPoints(dataList, dimension: int, typeCount: int):
    minValue = np.min(dataList, axis=1)[0:dimension]
    maxValue = np.max(dataList, axis=1)[0:dimension]
    centerPoints = []
    for i in range(0, typeCount):
        onePoint = []
        for j in range(0, dimension):
            onePoint.append(random.uniform(minValue[j], maxValue[j]))
        centerPoints.append(onePoint)
    return np.array(centerPoints)


def CalculateCenter(dataList, dimension: int, classIndex: int):
    points = dataList[dataList[:, dimension] == classIndex]
    if 0 == len(points):
        return 0, None
    return len(points), np.mean(points, axis=0)[0:dimension]


def CalculateCenterList(dataList, dimension: int, typeCount: int):
    result = []
    newSplit = []
    maximalCount = 0
    maximalClass = -1
    for ii in range(0, typeCount):
        countOfK, centerForK = CalculateCenter(dataList, dimension, ii)
        if centerForK is None:
            newSplit.append(ii)
        else:
            result.append(centerForK.tolist())
        if countOfK > maximalCount:
            maximalCount = countOfK
            maximalClass = ii
    if len(newSplit) > 0:
        while len(newSplit) > 0:
            newSplit.append(maximalClass)
            SplitLargestClass(dataList, dimension, maximalClass, np.array(newSplit))
            result = []
            newSplit = []
            maximalCount = 0
            maximalClass = -1
            for ii in range(0, typeCount):
                countOfK, centerForK = CalculateCenter(dataList, dimension, ii)
                if centerForK is None:
                    newSplit.append(ii)
                else:
                    result.append(centerForK.tolist())
                if countOfK > maximalCount:
                    maximalCount = countOfK
                    maximalClass = ii
    return np.array(result)


def Reclassify(dataList, centers, dimension: int, typeCount: int) -> int:
    changedCount = 0
    for i in range(0, len(dataList)):
        classIndexOfThisPoint = 0
        v = dataList[i, 0:dimension]
        delta = centers[0] - v
        distance0 = np.sqrt(np.dot(delta, delta))
        for classIndex in range(1, typeCount):
            deltaThisPoint = centers[classIndex] - v
            distanceThisPoint = np.sqrt(np.dot(deltaThisPoint, deltaThisPoint))
            if distanceThisPoint < distance0:
                distance0 = distanceThisPoint
                classIndexOfThisPoint = classIndex
        if classIndexOfThisPoint != dataList[i, dimension]:
            dataList[i, dimension] = classIndexOfThisPoint
            changedCount = changedCount + 1
    return changedCount


def KMeans(dataList, dimension: int, typeCount: int, stopWhenNoChange: int = 0) -> bool:
    # centers0 = RandomCenterPoints(dataList, dimension, typeCount)
    InitialClassify(dataList, dimension, typeCount)
    centers0 = CalculateCenterList(dataList, dimension, typeCount)
    changedCount = Reclassify(dataList, centers0, dimension, typeCount)
    while changedCount > stopWhenNoChange:
        centers0 = CalculateCenterList(dataList, dimension, typeCount)
        if centers0 is None:
            return False
        changedCount = Reclassify(dataList, centers0, dimension, typeCount)
        print(changedCount)
    return True


def CalculateDistance(dataList, dimension: int, typeCount: int):
    centers0 = CalculateCenterList(dataList, dimension, typeCount)
    distanceList = []
    for p in range(0, len(dataList)):
        center = centers0[int(np.round(dataList[p, dimension]))]
        delta = center - dataList[p, 0:dimension]
        distanceList.append(np.sqrt(np.dot(delta, delta)))
    return distanceList


def CalculateCenterD(dataList, dimension: int, classIndex: int):
    points = dataList[dataList[:, dimension] == classIndex]
    return np.mean(points, axis=0)[0:dimension]


def CalculateCenterListD(dataList, dimension: int, typeCount: int):
    result = []
    for ii in range(0, typeCount):
        centerForK = CalculateCenterD(dataList, dimension, ii)
        result.append(centerForK.tolist())
    return np.array(result)


def CalculateDistanceD(dataList, dimension: int, centers):
    distanceList = []
    for p in range(0, len(dataList)):
        center = centers[int(np.round(dataList[p, dimension]))]
        delta = center - dataList[p, 0:dimension]
        distanceList.append(np.sqrt(np.dot(delta, delta)))
    return distanceList


def HistoryMean(lst):
    ret = [lst[0]]
    for ii in range(1, len(lst)):
        ret.append(np.mean(lst[0:ii + 1]))
    return ret


