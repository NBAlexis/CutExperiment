import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

testEventsm = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/bgsm.lhco")
testEvent1 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
testEvent2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha1.lhco")
testEvent3 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha2.lhco")
testEvent4 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha3.lhco")
testEvent5 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/newmaxsignal/alpha4.lhco")

print(testEventsm.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

jetNumberCut = JetNumberCut(1, [2])
leptonNumberCut = LeptonPMCut(False, 1, 1)

mw=80.379
mz=91.1876
cw=0.972901
sw=0.23122
vev=246
e2=0.0934761 # sqrt{ 4 pi alpha} for alpha = 1/134
# shatCutAlpha1 = SHatCutWW(1000.0 * math.sqrt(32 * math.pi * mw * mw / 0.12))
# shatCutAlpha2 = SHatCutWW(1000.0 * math.sqrt(128 * math.pi * mw * mw / 0.2))
# shatCutAlpha3 = SHatCutWW(1.0e6 * math.sqrt(16 * math.pi / 2.9))
# shatCutAlpha4 = SHatCutWW(1.0e6 * math.sqrt(64 * math.pi / 5.9))
# shatCutAlpha5 = SHatCutWW(1.0e6 * math.sqrt(48 * math.pi / 2.3))

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)

CutEvents(testEvent1, jetNumberCut)
CutEvents(testEvent1, leptonNumberCut)
# CutEvents(testEvent1, shatCutAlpha1)

CutEvents(testEvent2, jetNumberCut)
CutEvents(testEvent2, leptonNumberCut)
# CutEvents(testEvent2, shatCutAlpha2)

CutEvents(testEvent3, jetNumberCut)
CutEvents(testEvent3, leptonNumberCut)
# CutEvents(testEvent3, shatCutAlpha3)

CutEvents(testEvent4, jetNumberCut)
CutEvents(testEvent4, leptonNumberCut)
# CutEvents(testEvent4, shatCutAlpha4)

CutEvents(testEvent5, jetNumberCut)
CutEvents(testEvent5, leptonNumberCut)
# CutEvents(testEvent5, shatCutAlpha5)


print(testEventsm.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

vbfCut = StandardVBFCut(True, 0.0, 2.3)

testMjj = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 1500], 50)
print(testMjj.minMax)
print(testMjj.listCount)
testMjj0 = HistogramWithMinMax(testEvent1, Mjj2Filter, [0, 1500], 50)
print(testMjj0.minMax)
print(testMjj0.listCount)
testMjj1 = HistogramWithMinMax(testEvent2, Mjj2Filter, [0, 1500], 50)
print(testMjj1.minMax)
print(testMjj1.listCount)
testMjj2 = HistogramWithMinMax(testEvent3, Mjj2Filter, [0, 1500], 50)
print(testMjj2.minMax)
print(testMjj2.listCount)
testMjj3 = HistogramWithMinMax(testEvent4, Mjj2Filter, [0, 1500], 50)
print(testMjj3.minMax)
print(testMjj3.listCount)
testMjj4 = HistogramWithMinMax(testEvent5, Mjj2Filter, [0, 1500], 50)
print(testMjj4.minMax)
print(testMjj4.listCount)
testYjj = HistogramWithMinMax(testEventsm, Yjj2Filter, [0, 10], 50)
print(testYjj.minMax)
print(testYjj.listCount)
testYjj0 = HistogramWithMinMax(testEvent1, Yjj2Filter, [0, 10], 50)
print(testYjj0.minMax)
print(testYjj0.listCount)
testYjj1 = HistogramWithMinMax(testEvent2, Yjj2Filter, [0, 10], 50)
print(testYjj1.minMax)
print(testYjj1.listCount)
testYjj2 = HistogramWithMinMax(testEvent3, Yjj2Filter, [0, 10], 50)
print(testYjj2.minMax)
print(testYjj2.listCount)
testYjj3 = HistogramWithMinMax(testEvent4, Yjj2Filter, [0, 10], 50)
print(testYjj3.minMax)
print(testYjj3.listCount)
testYjj4 = HistogramWithMinMax(testEvent5, Yjj2Filter, [0, 10], 50)
print(testYjj4.minMax)
print(testYjj4.listCount)

CutEvents(testEventsm, vbfCut)
CutEvents(testEvent1, vbfCut)
CutEvents(testEvent2, vbfCut)
CutEvents(testEvent3, vbfCut)
CutEvents(testEvent4, vbfCut)
CutEvents(testEvent5, vbfCut)


print(testEventsm.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

testEventsmETMissing = HistogramWithMinMax(testEventsm, PTLandPTMissing, [0, 3000], 50)
print(testEventsmETMissing.minMax)
print(testEventsmETMissing.listCount)
testEventAlpha0ETMissing = HistogramWithMinMax(testEvent1, PTLandPTMissing, [0, 3000], 50)
print(testEventAlpha0ETMissing.minMax)
print(testEventAlpha0ETMissing.listCount)
testEventAlpha1ETMissing = HistogramWithMinMax(testEvent2, PTLandPTMissing, [0, 3000], 50)
print(testEventAlpha1ETMissing.minMax)
print(testEventAlpha1ETMissing.listCount)
testEventAlpha2ETMissing = HistogramWithMinMax(testEvent3, PTLandPTMissing, [0, 3000], 50)
print(testEventAlpha2ETMissing.minMax)
print(testEventAlpha2ETMissing.listCount)
testEventAlpha3ETMissing = HistogramWithMinMax(testEvent4, PTLandPTMissing, [0, 3000], 50)
print(testEventAlpha3ETMissing.minMax)
print(testEventAlpha3ETMissing.listCount)
testEventAlpha4ETMissing = HistogramWithMinMax(testEvent5, PTLandPTMissing, [0, 3000], 50)
print(testEventAlpha4ETMissing.minMax)
print(testEventAlpha4ETMissing.listCount)

testEventsmLeptonDot = HistogramWithMinMax(testEventsm, LeptonDot, [-1.0, 1.0], 40)
print(testEventsmLeptonDot.minMax)
print(testEventsmLeptonDot.listCount)
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

molCut = MolCut(1, False, 500)
CutEvents(testEventsm, molCut)
CutEvents(testEvent1, molCut)
CutEvents(testEvent2, molCut)
CutEvents(testEvent3, molCut)
CutEvents(testEvent4, molCut)
CutEvents(testEvent5, molCut)
# etMissingCut = ETMissingCount(1, 200)
# CutEvents(testEventsm, etMissingCut)
# CutEvents(testEvent1, etMissingCut)
# CutEvents(testEvent2, etMissingCut)
# CutEvents(testEvent3, etMissingCut)
# CutEvents(testEvent4, etMissingCut)
# CutEvents(testEvent5, etMissingCut)

print(testEventsm.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

leptonCut = LeptonPMDotCut(0, False, -0.75)
CutEvents(testEventsm, leptonCut)
CutEvents(testEvent1, leptonCut)
CutEvents(testEvent2, leptonCut)
CutEvents(testEvent3, leptonCut)
CutEvents(testEvent4, leptonCut)
CutEvents(testEvent5, leptonCut)

print(testEventsm.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())

