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
testEventj3 = LoadLHCOlympics("_DataFolder/za/backgrounds/jjjll.lhco")
testEventj32 = LoadLHCOlympics("_DataFolder/za/backgrounds/jjjll2.lhco")
testEventj3.AddEventSet(testEventj32)
testEventm2 = LoadLHCOlympics("_DataFolder/za/features/azsignalm2.lhco")
testEventm3 = LoadLHCOlympics("_DataFolder/za/features/azsignalm3.lhco")
testEventm4 = LoadLHCOlympics("_DataFolder/za/features/azsignalm4.lhco")
testEventm5 = LoadLHCOlympics("_DataFolder/za/features/azsignalm5.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")
testEventt6 = LoadLHCOlympics("_DataFolder/za/features/azsignalt6.lhco")
testEventt7 = LoadLHCOlympics("_DataFolder/za/features/azsignalt7.lhco")
testEventt8 = LoadLHCOlympics("_DataFolder/za/features/azsignalt8.lhco")
testEventt9 = LoadLHCOlympics("_DataFolder/za/features/azsignalt9.lhco")

particleNumberCut = ParticleNumberZA()
vbsCut = StandardVBFCut(True, 150.0, 1.2)
invllCut = EllInvMass(20, 91.1876)

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
CutEvents(testEventm2, particleNumberCut)
CutEvents(testEventm3, particleNumberCut)
CutEvents(testEventm4, particleNumberCut)
CutEvents(testEventm5, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)
CutEvents(testEventt6, particleNumberCut)
CutEvents(testEventt7, particleNumberCut)
CutEvents(testEventt8, particleNumberCut)
CutEvents(testEventt9, particleNumberCut)

print("============== after partical number ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())

CutEvents(testEventsm, vbsCut)
CutEvents(testEventj3, vbsCut)
CutEvents(testEventm2, vbsCut)
CutEvents(testEventm3, vbsCut)
CutEvents(testEventm4, vbsCut)
CutEvents(testEventm5, vbsCut)
CutEvents(testEventt5, vbsCut)
CutEvents(testEventt6, vbsCut)
CutEvents(testEventt7, vbsCut)
CutEvents(testEventt8, vbsCut)
CutEvents(testEventt9, vbsCut)

print("============== after vbf ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())



CutEvents(testEventsm, invllCut)
CutEvents(testEventj3, invllCut)
CutEvents(testEventm2, invllCut)
CutEvents(testEventm3, invllCut)
CutEvents(testEventm4, invllCut)
CutEvents(testEventm5, invllCut)
CutEvents(testEventt5, invllCut)
CutEvents(testEventt6, invllCut)
CutEvents(testEventt7, invllCut)
CutEvents(testEventt8, invllCut)
CutEvents(testEventt9, invllCut)

print("============== after inv ll ===============")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())

ellDotCut = DotEllCut(0.7)
mzaCut = SHatZACut(300, -1)