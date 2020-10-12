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
testEventt5 = LoadLHCOlympics("_DataFolder/za/features/azsignalt5.lhco")

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

particleNumberCut = ParticleNumberZA()

CutEvents(testEventsm, particleNumberCut)
CutEvents(testEventj3, particleNumberCut)
CutEvents(testEventm2, particleNumberCut)
CutEvents(testEventt5, particleNumberCut)

print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventt5.GetEventCount())

# ===================================================
# Here starts the cut flow

"""
# Invariant mass of l+l-
testTlSM = HistogramWithMinMax(testEventsm, InvMass, [0, 120], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, InvMass, [0, 120], 40)
testTlM2 = HistogramWithMinMax(testEventm2, InvMass, [0, 120], 40)
testTlT5 = HistogramWithMinMax(testEventt5, InvMass, [0, 120], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
"""

"""
# Yjj
testTlSM = HistogramWithMinMax(testEventsm, Yjj2Filter, [0, 8], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Yjj2Filter, [0, 8], 40)
testTlM2 = HistogramWithMinMax(testEventm2, Yjj2Filter, [0, 8], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Yjj2Filter, [0, 8], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
"""

"""
# Mjj
testTlSM = HistogramWithMinMax(testEventsm, Mjj2Filter, [0, 2000], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, Mjj2Filter, [0, 2000], 40)
testTlM2 = HistogramWithMinMax(testEventm2, Mjj2Filter, [0, 2000], 40)
testTlT5 = HistogramWithMinMax(testEventt5, Mjj2Filter, [0, 2000], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
"""

"""
# theta ll
testTlSM = HistogramWithMinMax(testEventsm, LeptonDotZA, [-1, 1], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, LeptonDotZA, [-1, 1], 40)
testTlM2 = HistogramWithMinMax(testEventm2, LeptonDotZA, [-1, 1], 40)
testTlT5 = HistogramWithMinMax(testEventt5, LeptonDotZA, [-1, 1], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
"""

"""
# shat
testTlSM = HistogramWithMinMax(testEventsm, SHatZA, [0, 8000], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, SHatZA, [0, 8000], 40)
testTlM2 = HistogramWithMinMax(testEventm2, SHatZA, [0, 8000], 40)
testTlT5 = HistogramWithMinMax(testEventt5, SHatZA, [0, 8000], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
print(testTlM2.listCount)
print(testTlT5.listCount)
"""

# """
# Polarization
testTlSM = HistogramWithMinMax(testEventsm, LeptonPZAndGammaTheta, [0, 1.25], 40)
testTlJ3 = HistogramWithMinMax(testEventj3, LeptonPZAndGammaTheta, [0, 1.25], 40)
# testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZAndGammaTheta, [0, 1.25], 40)
testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZAndGammaTheta, [0, 1.25], 40)
print(testTlSM.listCount)
print(testTlJ3.listCount)
# print(testTlM2.listCount)
print(testTlT5.listCount)
# """


