import math
import re

from CutAndExport.Histogram import HistogramResult
from DataStructure.EventSet import EventSet
from Interfaces.LHCOlympics import LoadLHCOlympics, SaveToLHCO


def ReadCSVFile(fileName: str, startIdx: int, endIdx: int) -> list:
    dataSample = []
    with open(fileName) as f:
        for lines in f.readlines():
            strList = lines.split(',')
            if len(strList) > endIdx:
                numberList = []
                for j in range(startIdx, endIdx + 1):
                    numberList = numberList + [float(strList[j])]
                dataSample = dataSample + [numberList]
    return dataSample


def SaveCSVFile(fileName: str, content: list, startIdx: int, endIdx: int):
    with open(fileName, 'w') as f:
        for line in content:
            if len(line) > endIdx:
                for i in range(startIdx, endIdx + 1):
                    if i == endIdx:
                        f.write(str(line[i]) + "\n")
                    else:
                        f.write(str(line[i]) + ", ")


def SaveCSVFileA(fileName: str, content: list, startIdx: int, endIdx: int):
    with open(fileName, 'a') as f:
        for line in content:
            if len(line) > endIdx:
                for i in range(startIdx, endIdx + 1):
                    if i == endIdx:
                        f.write(str(line[i]) + "\n")
                    else:
                        f.write(str(line[i]) + ", ")


def CombineEventsLHCO(fileNames: list, targetFileName: str):
    eventAll = EventSet()
    for fileName in fileNames:
        eventToAdd = LoadLHCOlympics(fileName)
        print("Adding {} ({} events)...".format(fileName, eventToAdd.GetEventCount()))
        eventAll.AddEventSet(eventToAdd)
    SaveToLHCO(targetFileName, eventAll)
    eventVerify = LoadLHCOlympics(targetFileName)
    print("Verify: {} ({} events)...".format(targetFileName, eventVerify.GetEventCount()))


def PrintLogTxt(fileName: str):
    lineNumber = 0
    lstA = []
    lstB = []
    with open(fileName) as f:
        for lines in f.readlines():
            lineNumber = lineNumber + 1
            if 1 == lineNumber:
                continue
            linesrep = re.sub("[\\s]+", " ", lines)
            contentList = linesrep.split(' ')
            if 3 <= len(contentList):
                lstA.append(float(contentList[1]))
                lstB.append(float(contentList[2]))
    print(lstA)
    print(lstB)


def HistogramStrict(valueList: list, minValue: float, maxValue: float, groupCount: int = 100):
    import matplotlib.pyplot as plt
    separate = (maxValue - minValue) / groupCount
    listCount = [0 for i in range(groupCount)]
    for v in valueList:
        lstIdx = 0 if separate < 1.0e-22 else math.floor((v - minValue) / separate)
        if 0 <= lstIdx < groupCount:
            listCount[lstIdx] += 1
    plt.hist(valueList, groupCount)
    plt.show()
    return HistogramResult(groupCount, [minValue, maxValue], listCount)


def BannerReaderCS(fileName: str, debuginfo: bool = False) -> float:
    with open(fileName) as f:
        bannertext = f.read()
        searchtext = re.search("""Integrated weight\s\(pb\)[\s]*\:[\s]*([\.\d+e\-]+)[\s]*""", bannertext)
        cs = float(searchtext.group(1))
        if debuginfo:
            print(cs)
        return cs


def BannerReader(fileName: str, paramName: str) -> [float, float]:
    with open(fileName) as f:
        bannertext = f.read()
        searchtext = re.search("""Integrated weight\s\(pb\)[\s]*\:[\s]*([\.\d+e\-]+)[\s]*""", bannertext)
        cs = float(searchtext.group(1))
        searchtext = re.search("""[\d]+[\s]+([\.\d+e\-]+)[\s]+\#[\s]+""" + paramName, bannertext)
        paramv = float(searchtext.group(1))
        return cs, paramv


def ScanReader(fileName: str) -> [list, list]:
    lineNumber = 0
    lstA = []
    lstB = []
    with open(fileName) as f:
        for lines in f.readlines():
            lineNumber = lineNumber + 1
            if 1 == lineNumber:
                continue
            linesrep = re.sub("[\\s]+", " ", lines)
            contentList = linesrep.split(' ')
            if 3 <= len(contentList):
                lstA.append(float(contentList[1]))
                lstB.append(float(contentList[2]))
    return lstA, lstB


def PrintMathematica(cont):
    contStr = str(cont)
    contStr = contStr.replace("e", "*^")
    contStr = contStr.replace("[", "{")
    contStr = contStr.replace("]", "}")
    print(contStr)


def coefx(l, a, b, c, s, x):
    ax2bx = a * x * x + b * x
    return math.sqrt(2 * l * ((ax2bx + c) * math.log(1 + ax2bx / c) - ax2bx)) - s


def dcoefx(l, a, b, c, x):
    xbax = x * (b + a * x)
    inlog = 1 + xbax / c
    return math.sqrt(l) * (b + 2 * a * x) * math.log(inlog) / math.sqrt(2 * (c + xbax) * math.log(inlog) - 2 * xbax)


def findroot(l, a, b, c, s, xstart, eps=1e-8):
    x = xstart
    iterationstep = 0
    delta = -coefx(l, a, b, c, s, x) / dcoefx(l, a, b, c, x)
    while abs(delta) > eps and iterationstep < 10000:
        iterationstep = iterationstep + 1
        x = x + delta
        delta = -coefx(l, a, b, c, s, x) / dcoefx(l, a, b, c, x)
    return x + delta
