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

testEvent = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha1.lhe")
testEvent2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha1.lhco")
# testEvent2 = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha2.lhe")
# testEvent3 = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha3.lhe")
# testEvent4 = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha4.lhe")
# testEvent5 = LoadLesHouchesEvent("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha5.lhe")



print(testEvent.events[1234].DebugPrint())
print(testEvent2.events[1234].DebugPrint())
"""
newSet = EventSet()
lstS1 = []
lstRealS = []
particleCount = 0
lstDelta = []
for i in range(len(testEvent.events)):
    lstDelta.append(math.sqrt(SHatWWReal(testEvent.events[i])))

for i in range(len(testEvent.events)):
    if testEvent2.events[i].GetLeptonCount() == 2 and testEvent2.events[i].GetJetCount() > 1:
        lstUV = SHatWWUV(testEvent2.events[i])
        particleCount = particleCount + 1
        if lstUV[0] * lstUV[1] > 0:
            calcS = SHatWW(testEvent2.events[i])
            realS = SHatWWReal(testEvent.events[i])
            if abs(calcS - realS) < 1.0e7:
                lstDelta.append(calcS - realS)
            if 1.0e8 > calcS > 0 and 1.0e8 > realS > 0:
                newSet.AddEvent(testEvent2.events[i])
                lstS1.append(calcS)
                lstRealS.append(realS)

# print(particleCount)
# print(len(lstDelta))
# print(len(lstS1))

import matplotlib.pyplot as plt
# plt.hist2d(lstS1, lstRealS, [20, 20])
# plt.show()

plt.hist(lstDelta, 50)
plt.show()

# CorrelationData(testEvent, SHatWW, SHatWWReal, 20, 20, [0, 2.0e7], [0, 2.0e7])
# testMjj = HistogramWithMinMax(testEvent, SHatWWReal, [0, 5.0e7], 50)
# testMjj = HistogramWithMinMax(testEvent, SHatWW, [-1.0e8, 1.0e8], 50)
# print(testMjj.minMax)
# print(testMjj.listCount)
"""
