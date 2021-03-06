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
# testEventttbarj = LoadLHCOlympics("wwaa/ttbar/ttbarj.lhco")
# testEventttbarjj = LoadLHCOlympics("wwaa/ttbar/ttbarjj.lhco")
testEvent1 = LoadLHCOlympics("wwaa/maxsignal/alpha1.lhco")
testEvent2 = LoadLHCOlympics("wwaa/maxsignal/alpha2.lhco")
testEvent3 = LoadLHCOlympics("wwaa/maxsignal/alpha3.lhco")
testEvent4 = LoadLHCOlympics("wwaa/maxsignal/alpha4.lhco")
testEvent5 = LoadLHCOlympics("wwaa/maxsignal/alpha5.lhco")

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)

CutEvents(testEventttbar, jetNumberCut)
CutEvents(testEventttbar, leptonNumberCut)

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
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

"""
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
# testEventttbarjLeptonDot = HistogramWithMinMax(testEventttbarj, Mjj2Filter, [0.0, 1500.0], 40)
# print(testEventttbarjLeptonDot.minMax)
# print(testEventttbarjLeptonDot.listCount)
# testEventttbarjjLeptonDot = HistogramWithMinMax(testEventttbarjj, Mjj2Filter, [0.0, 1500.0], 40)
# print(testEventttbarjjLeptonDot.minMax)
# print(testEventttbarjjLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, Mjj2Filter, [0.0, 1600.0], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
"""

"""
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, Yjj2Filter, [0.0, 10.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, Yjj2Filter, [0.0, 10.0], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
# testEventttbarjLeptonDot = HistogramWithMinMax(testEventttbarj, Yjj2Filter, [0.0, 10.0], 40)
# print(testEventttbarjLeptonDot.minMax)
# print(testEventttbarjLeptonDot.listCount)
# testEventttbarjjLeptonDot = HistogramWithMinMax(testEventttbarjj, Yjj2Filter, [0.0, 10.0], 40)
# print(testEventttbarjjLeptonDot.minMax)
# print(testEventttbarjjLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, Yjj2Filter, [0.0, 10.0], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, Yjj2Filter, [0.0, 10.0], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, Yjj2Filter, [0.0, 10.0], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, Yjj2Filter, [0.0, 10.0], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, Yjj2Filter, [0.0, 10.0], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
"""

# """
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, PhiLLM, [0.0, 1.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, PhiLLM, [0.0, 1.0], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
# testEventttbarjLeptonDot = HistogramWithMinMax(testEventttbarj, PhiLLM, [0.0, 1.0], 40)
# print(testEventttbarjLeptonDot.minMax)
# print(testEventttbarjLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, PhiLLM, [0.0, 1.0], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, PhiLLM, [0.0, 1.0], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, PhiLLM, [0.0, 1.0], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, PhiLLM, [0.0, 1.0], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, PhiLLM, [0.0, 1.0], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
# """

"""
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, SHatWW, [0.0, 2.0e7], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, SHatWW, [0.0, 2.0e7], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
# testEventttbarjLeptonDot = HistogramWithMinMax(testEventttbarj, SHatWW, [0.0, 2.0e7], 40)
# print(testEventttbarjLeptonDot.minMax)
# print(testEventttbarjLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, SHatWW, [0.0, 2.0e7], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, SHatWW, [0.0, 2.0e7], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, SHatWW, [0.0, 2.0e7], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, SHatWW, [0.0, 2.0e7], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, SHatWW, [0.0, 2.0e7], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
"""

"""
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, LeptonDot, [-1.0, 1.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, LeptonDot, [-1.0, 1.0], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, LeptonDot, [-1.0, 1.0], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, LeptonDot, [-1.0, 1.0], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, LeptonDot, [-1.0, 1.0], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, LeptonDot, [-1.0, 1.0], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, LeptonDot, [-1.0, 1.0], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
"""

"""
testEventsmLeptonDot = HistogramWithMinMax(testEventsm, PTLandPTMissing, [0, 3000.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
testEventttbarLeptonDot = HistogramWithMinMax(testEventttbar, PTLandPTMissing, [0, 3000.0], 40)
print(testEventttbarLeptonDot.minMax)
print(testEventttbarLeptonDot.listCount)
testEventAlpha0LeptonDot = HistogramWithMinMax(testEvent1, PTLandPTMissing, [0, 3000.0], 40)
print(testEventAlpha0LeptonDot.minMax)
print(testEventAlpha0LeptonDot.listCount)
testEventAlpha1LeptonDot = HistogramWithMinMax(testEvent2, PTLandPTMissing, [0, 3000.0], 40)
print(testEventAlpha1LeptonDot.minMax)
print(testEventAlpha1LeptonDot.listCount)
testEventAlpha2LeptonDot = HistogramWithMinMax(testEvent3, PTLandPTMissing, [0, 3000.0], 40)
print(testEventAlpha2LeptonDot.minMax)
print(testEventAlpha2LeptonDot.listCount)
testEventAlpha3LeptonDot = HistogramWithMinMax(testEvent4, PTLandPTMissing, [0, 3000.0], 40)
print(testEventAlpha3LeptonDot.minMax)
print(testEventAlpha3LeptonDot.listCount)
testEventAlpha4LeptonDot = HistogramWithMinMax(testEvent5, PTLandPTMissing, [0, 3000.0], 40)
print(testEventAlpha4LeptonDot.minMax)
print(testEventAlpha4LeptonDot.listCount)
"""