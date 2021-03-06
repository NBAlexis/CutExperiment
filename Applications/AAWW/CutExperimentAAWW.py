import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("../../_DataFolder")

testEventsm = LoadLHCOlympics("wwaa/aaww_smbg.lhco")
testEventttbar = LoadLHCOlympics("wwaa/ttbar/ttbar.lhco")
testEventttbar.AddEventSet(LoadLHCOlympics("wwaa/ttbar/ttbar2.lhco"))
testEventttbarj = LoadLHCOlympics("wwaa/ttbar/ttbarj.lhco")
testEventttbarjj = LoadLHCOlympics("wwaa/ttbar/ttbarjj.lhco")
testEventttbarjjj = LoadLHCOlympics("wwaa/ttbar/ttbarjjj.lhco")
testEvent1 = LoadLHCOlympics("wwaa/maxsignal/alpha1.lhco")
testEvent2 = LoadLHCOlympics("wwaa/maxsignal/alpha2.lhco")
testEvent3 = LoadLHCOlympics("wwaa/maxsignal/alpha3.lhco")
testEvent4 = LoadLHCOlympics("wwaa/maxsignal/alpha4.lhco")
testEvent5 = LoadLHCOlympics("wwaa/maxsignal/alpha5.lhco")

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

#jetNumberCut = JetNumberCut(2, [2, 3, 4])
jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)
vbfCut = StandardVBFCut(True, 150.0, 1.2)
phillmCut = PhiLLMCut(1, 0.3)
shatCut = SHatCutWWTest(1, 1.5e6)
leptonCut = LeptonPMDotCut(0, False, -0.0)
molCut = MolCut(1, False, 600)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)

CutEvents(testEventttbar, jetNumberCut)
CutEvents(testEventttbar, leptonNumberCut)

CutEvents(testEventttbarj, jetNumberCut)
CutEvents(testEventttbarj, leptonNumberCut)

CutEvents(testEventttbarjj, jetNumberCut)
CutEvents(testEventttbarjj, leptonNumberCut)

CutEvents(testEventttbarjjj, jetNumberCut)
CutEvents(testEventttbarjjj, leptonNumberCut)

CutEvents(testEvent1, jetNumberCut)
CutEvents(testEvent1, leptonNumberCut)

CutEvents(testEvent2, jetNumberCut)
CutEvents(testEvent2, leptonNumberCut)

CutEvents(testEvent3, jetNumberCut)
CutEvents(testEvent3, leptonNumberCut)

CutEvents(testEvent4, jetNumberCut)
CutEvents(testEvent4, leptonNumberCut)

CutEvents(testEvent5, jetNumberCut)
CutEvents(testEvent5, leptonNumberCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

print("============ after vbf ===============")

CutEvents(testEventsm, vbfCut)
CutEvents(testEventttbar, vbfCut)
CutEvents(testEventttbarj, vbfCut)
CutEvents(testEventttbarjj, vbfCut)
CutEvents(testEventttbarjjj, vbfCut)
CutEvents(testEvent1, vbfCut)
CutEvents(testEvent2, vbfCut)
CutEvents(testEvent3, vbfCut)
CutEvents(testEvent4, vbfCut)
CutEvents(testEvent5, vbfCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

print("============ after phillm ===============")

CutEvents(testEventsm, phillmCut)
CutEvents(testEventttbar, phillmCut)
CutEvents(testEventttbarj, phillmCut)
CutEvents(testEventttbarjj, phillmCut)
CutEvents(testEventttbarjjj, phillmCut)
CutEvents(testEvent1, phillmCut)
CutEvents(testEvent2, phillmCut)
CutEvents(testEvent3, phillmCut)
CutEvents(testEvent4, phillmCut)
CutEvents(testEvent5, phillmCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

print("============ after leptondot ===============")

CutEvents(testEventsm, leptonCut)
CutEvents(testEventttbar, leptonCut)
CutEvents(testEventttbarj, leptonCut)
CutEvents(testEventttbarjj, leptonCut)
CutEvents(testEventttbarjjj, leptonCut)
CutEvents(testEvent1, leptonCut)
CutEvents(testEvent2, leptonCut)
CutEvents(testEvent3, leptonCut)
CutEvents(testEvent4, leptonCut)
CutEvents(testEvent5, leptonCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

print("============ after shat ===============")

CutEvents(testEventsm, shatCut)
CutEvents(testEventttbar, shatCut)
CutEvents(testEventttbarj, shatCut)
CutEvents(testEventttbarjj, shatCut)
CutEvents(testEventttbarjjj, shatCut)
CutEvents(testEvent1, shatCut)
CutEvents(testEvent2, shatCut)
CutEvents(testEvent3, shatCut)
CutEvents(testEvent4, shatCut)
CutEvents(testEvent5, shatCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

print("============ after mo1 ===============")

CutEvents(testEventsm, molCut)
CutEvents(testEventttbar, molCut)
CutEvents(testEventttbarj, molCut)
CutEvents(testEventttbarjj, molCut)
CutEvents(testEventttbarjjj, molCut)
CutEvents(testEvent1, molCut)
CutEvents(testEvent2, molCut)
CutEvents(testEvent3, molCut)
CutEvents(testEvent4, molCut)
CutEvents(testEvent5, molCut)

print(testEventsm.GetEventCount())
print(testEventttbar.GetEventCount())
print(testEventttbarj.GetEventCount())
print(testEventttbarjj.GetEventCount())
print(testEventttbarjjj.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
