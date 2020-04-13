import os

from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

testEventsm0 = LoadLHCOlympics("wa/features/bgsm2.lhco")
testEventsm = LoadLHCOlympics("wa/features/bgsm.lhco")
testEventsm.AddEventSet(testEventsm0)

testEventm2 = LoadLHCOlympics("wa/features/fm2.lhco")


"""
print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())
print(testEventt0.GetEventCount())
print(testEventt1.GetEventCount())
print(testEventt2.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
"""

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)

# testYjjSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, Mjj2Filter, [0, 2000], 50)

# testYjjSM = HistogramWithMinMax(testEventsm, Yjj2Filter, [0, 10], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, Yjj2Filter, [0, 10], 50)

# testYjjSM = HistogramWithMinMax(testEventsm, RadiusA, [0, 2], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, RadiusA, [0, 2], 50)

# testYjjSM = HistogramWithMinMax(testEventsm, Megamma, [0, 1000], 50)
# testYjjM2 = HistogramWithMinMax(testEventm2, Megamma, [0, 1000], 50)

testYjjSM = HistogramWithMinMax(testEventsm, PhiLeptonMissing, [0.9, 1], 50)
testYjjM2 = HistogramWithMinMax(testEventm2, PhiLeptonMissing, [0.9, 1], 50)
