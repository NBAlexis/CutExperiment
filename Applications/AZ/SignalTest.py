import os

from Applications.AZ.ZGammaCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../")
testEventsm = LoadLHCOlympics("_DataFolder/za/features/azsm14.lhco")
testEventsm2 = LoadLHCOlympics("_DataFolder/za/features/azsm2.lhco")
testEventsm3 = LoadLHCOlympics("_DataFolder/za/features/azsm3.lhco")
testEventsm4 = LoadLHCOlympics("_DataFolder/za/features/azsm4.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventsm.AddEventSet(testEventsm4)
testEventm2 = LoadLHCOlympics("_DataFolder/za/features/azsignalm3.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")

print(LeptonPZ(testEventm2.events[0]))

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

particleNumberCut = ParticleNumberZA()

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventm2, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

invllCut = EllInvMass(10, 91.1876)

CutEvents(testEventsm, invllCut)
CutEvents(testEventm2, invllCut)
CutEvents(testEventt5, invllCut)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

ellDotCut = DotEllCut(0.7)

CutEvents(testEventsm, ellDotCut)
CutEvents(testEventm2, ellDotCut)
CutEvents(testEventt5, ellDotCut)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

mzaCut = SHatZACut(300, -1)

CutEvents(testEventsm, mzaCut)
CutEvents(testEventm2, mzaCut)
CutEvents(testEventt5, mzaCut)

print(testEventsm.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())


testTlSM = HistogramWithMinMax(testEventsm, LeptonPZ, [-1, 1], 50)
testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZ, [-1, 1], 50)
testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZ, [-1, 1], 50)
print(testTlSM.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
