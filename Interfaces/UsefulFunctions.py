import re

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
