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
testEventsm = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm1.lhco")
testEventsm2 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm2.lhco")
testEventsm3 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm3.lhco")
testEventsm4 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/azsm4.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventsm.AddEventSet(testEventsm4)
testEventj3 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll1.lhco")
testEventj32 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll2.lhco")
testEventj33 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll3.lhco")
# testEventj34 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll4.lhco")
testEventj35 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll5.lhco")
testEventj3.AddEventSet(testEventj32)
testEventj3.AddEventSet(testEventj33)
# testEventj3.AddEventSet(testEventj34)
testEventj3.AddEventSet(testEventj35)
testEventm3 = LoadLHCOlympics("_DataFolder/za/features/azsignalm3.lhco")
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventt5.GetEventCount())

particleNumberCut = ParticleNumberZA()
deltaRCut = DeltaRCut(0.2)

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
CutEvents(testEventm3, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)
CutEvents(testEventm3, deltaRCut)
CutEvents(testEventt5, deltaRCut)

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventt5.GetEventCount())

# ===================================================
# Here starts the cut flow

# testDeltaRm2 = HistogramWithMinMax(testEventm2, DeltaR, [0, 1], 40)
# testDeltaRt5 = HistogramWithMinMax(testEventt5, DeltaR, [0, 1], 40)

"""
# Invariant mass of l+l-
testTlSM = HistogramWithMinMax(testEventsm, InvMass, [0, 120], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, InvMass, [0, 120], 40)
testTlM3 = HistogramWithMinMax(testEventm3, InvMass, [0, 120], 40)
testTlT5 = HistogramWithMinMax(testEventt5, InvMass, [0, 120], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# Yjj
testTlSM = HistogramWithMinMax(testEventsm, Yjj2Filter, [0, 8], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Yjj2Filter, [0, 8], 40)
testTlM3 = HistogramWithMinMax(testEventm3, Yjj2Filter, [0, 8], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Yjj2Filter, [0, 8], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# Mjj
testTlSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Mjj2Filter, [0, 2000], 40)
testTlM3 = HistogramWithMinMax(testEventm3, Mjj2Filter, [0, 2000], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# theta ll
testTlSM = HistogramWithMinMax(testEventsm, DeltaR, [0.2, 1], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, DeltaR, [0.2, 1], 40)
testTlM3 = HistogramWithMinMax(testEventm3, DeltaR, [0.2, 1], 40)
testTlT5 = HistogramWithMinMax(testEventt5, DeltaR, [0.2, 1], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# shat
testTlSM = HistogramWithMinMax(testEventsm, SHatZA, [0, 8000], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, SHatZA, [0, 8000], 40)
testTlM3 = HistogramWithMinMax(testEventm3, SHatZA, [0, 8000], 40)
testTlT5 = HistogramWithMinMax(testEventt5, SHatZA, [0, 8000], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM3.listCount)
print(testTlT5.listCount)
"""

"""
# Polarization
testTlSM = HistogramWithMinMax(testEventsm, LeptonPZAndGammaTheta, [0, 1.2], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, LeptonPZAndGammaTheta, [0, 1.2], 40)
# testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZAndGammaTheta, [0, 1.25], 40)
testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZAndGammaTheta, [0, 1.2], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
# print(testTlM2.listCount)
print(testTlT5.listCount)
"""


