import os

from CutAndExport.CorrelationFunctions import CorrelationData
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

testEvent = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wa/features2/ft5.lhe")
testEvent2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wa/features2/ft5.lhco")

# print(testEvent.events[1234].DebugPrint())
# print(testEvent2.events[1234].DebugPrint())
# print(SHatAW(testEvent2.events[1234]))
# print(SHatAWRealDebug(testEvent.events[1234]))

# newSet = EventSet()
lstS1 = []
lstRealS = []
particleCount0 = 0
particleCount = 0
lstDelta = []
validLeptonPt = 100.0
particleCount1 = 0
particleCount2 = 0

result_f = open("t5shat.csv", 'a')
for i in range(len(testEvent.events)):
    # requirements
    bValid = (1 == testEvent2.events[i].GetLeptonCount())
    bValid = bValid and testEvent2.events[i].GetJetCount() > 1
    bValid = bValid and testEvent2.events[i].GetPhotonCount() > 0
    if bValid:
        phiLM = PhiLeptonMissing(testEvent2.events[i])
        bValid = (phiLM >= 0.95)
    if bValid:
        particleCount0 = particleCount0 + 1
        leptonIdx = -1
        for j in range(len(testEvent2.events[i].particles)):
            if 1 == testEvent2.events[i].particles[j].particleType or 2 == testEvent2.events[i].particles[j].particleType:
                leptonIdx = j
        pLepton = testEvent2.events[i].particles[leptonIdx].momentum
        if pLepton.values[1] < validLeptonPt and pLepton.values[2] < validLeptonPt:
            bValid = False
    if bValid:
        particleCount = particleCount + 1
        calcS = SHatAW(testEvent2.events[i])
        realS = SHatAWReal(testEvent.events[i])
        if abs(calcS - realS) < 1.0e7:
            particleCount2 = particleCount2 + 1
            lstDelta.append(calcS - realS)
        if 3.0e7 > calcS > 0 and 3.0e7 > realS > 0:
            # newSet.AddEvent(testEvent2.events[i])
            particleCount1 = particleCount1 + 1
            # lstS1.append(calcS)
            # lstRealS.append(realS)
            result_f.write("{}, {}\n".format(realS, calcS))

result_f.close()
print(particleCount0)
print(particleCount)
print(particleCount1)
print(particleCount2)

retArray = [[0 for i in range(40)] for j in range(40)]
histArray = [0 for i in range(50)]
sep1 = 2.0e7 / 40
sep2 = 2.0e7 / 50
"""
for i in range(particleCount1):
    v1 = lstS1[i]
    v2 = lstRealS[i]
    idxX = math.floor(v1 / sep1)
    if idxX >= 40:
        idxX = 39
    if idxX < 0:
        idxX = 0
    idxY = math.floor(v2 / sep1)
    if idxY >= 40:
        idxY = 39
    if idxY < 0:
        idxY = 0
    retArray[idxX][idxY] = retArray[idxX][idxY] + 1
"""
for i in range(particleCount2):
    v3 = lstDelta[i]
    idxZ = math.floor((v3 + 1.0e7) / sep2)
    if idxZ >= 40:
        idxZ = 39
    if idxZ < 0:
        idxZ = 0
    histArray[idxZ] = histArray[idxZ] + 1

# print(retArray)
print(histArray)
# import matplotlib.pyplot as plt
# plt.hist2d(lstS1, lstRealS, [20, 20])
# plt.show()

# plt.hist(lstDelta, 50)
# plt.show()

# CorrelationData(testEvent, SHatWW, SHatWWReal, 20, 20, [0, 2.0e7], [0, 2.0e7])
# testMjj = HistogramWithMinMax(testEvent, SHatWWReal, [0, 5.0e7], 50)
# testMjj = HistogramWithMinMax(testEvent, SHatWW, [-1.0e8, 1.0e8], 50)
# print(testMjj.minMax)
# print(testMjj.listCount)
