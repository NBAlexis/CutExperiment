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
testEventm0 = LoadLHCOlympics("wa/features/fm0.lhco")
testEventm1 = LoadLHCOlympics("wa/features/fm1.lhco")
testEventm2 = LoadLHCOlympics("wa/features/fm2.lhco")
testEventm3 = LoadLHCOlympics("wa/features/fm3.lhco")
testEventm4 = LoadLHCOlympics("wa/features/fm4.lhco")
testEventm5 = LoadLHCOlympics("wa/features/fm5.lhco")
testEventm7 = LoadLHCOlympics("wa/features/fm7.lhco")

jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)

CutEvents(testEventsm, jetNumberCut)
CutEvents(testEventsm, leptonNumberCut)
CutEvents(testEventsm, photonNumberCut)

CutEvents(testEventm0, jetNumberCut)
CutEvents(testEventm0, leptonNumberCut)
CutEvents(testEventm0, photonNumberCut)
CutEvents(testEventm1, jetNumberCut)
CutEvents(testEventm1, leptonNumberCut)
CutEvents(testEventm1, photonNumberCut)
CutEvents(testEventm2, jetNumberCut)
CutEvents(testEventm2, leptonNumberCut)
CutEvents(testEventm2, photonNumberCut)
CutEvents(testEventm3, jetNumberCut)
CutEvents(testEventm3, leptonNumberCut)
CutEvents(testEventm3, photonNumberCut)
CutEvents(testEventm4, jetNumberCut)
CutEvents(testEventm4, leptonNumberCut)
CutEvents(testEventm4, photonNumberCut)
CutEvents(testEventm5, jetNumberCut)
CutEvents(testEventm5, leptonNumberCut)
CutEvents(testEventm5, photonNumberCut)
CutEvents(testEventm7, jetNumberCut)
CutEvents(testEventm7, leptonNumberCut)
CutEvents(testEventm7, photonNumberCut)

print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

vbfCut = StandardVBFCut(True, 0.0, 2.0)

CutEvents(testEventsm, vbfCut)
CutEvents(testEventm0, vbfCut)
CutEvents(testEventm1, vbfCut)
CutEvents(testEventm2, vbfCut)
CutEvents(testEventm3, vbfCut)
CutEvents(testEventm4, vbfCut)
CutEvents(testEventm5, vbfCut)
CutEvents(testEventm7, vbfCut)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

ptMissingCut = PtMissing(1, 120)

CutEvents(testEventsm, ptMissingCut)
CutEvents(testEventm0, ptMissingCut)
CutEvents(testEventm1, ptMissingCut)
CutEvents(testEventm2, ptMissingCut)
CutEvents(testEventm3, ptMissingCut)
CutEvents(testEventm4, ptMissingCut)
CutEvents(testEventm5, ptMissingCut)
CutEvents(testEventm7, ptMissingCut)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())


megammaCut = MeGammaCut(1, False, 800)

CutEvents(testEventsm, megammaCut)
CutEvents(testEventm0, megammaCut)
CutEvents(testEventm1, megammaCut)
CutEvents(testEventm2, megammaCut)
CutEvents(testEventm3, megammaCut)
CutEvents(testEventm4, megammaCut)
CutEvents(testEventm5, megammaCut)
CutEvents(testEventm7, megammaCut)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

thetaGammaLepton = ThetaGammaLeptonCut(0, False, 0)

CutEvents(testEventsm, thetaGammaLepton)
CutEvents(testEventm0, thetaGammaLepton)
CutEvents(testEventm1, thetaGammaLepton)
CutEvents(testEventm2, thetaGammaLepton)
CutEvents(testEventm3, thetaGammaLepton)
CutEvents(testEventm4, thetaGammaLepton)
CutEvents(testEventm5, thetaGammaLepton)
CutEvents(testEventm7, thetaGammaLepton)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

phiGammaMissing = PhiGammaMissingCut(0, -0.75)

CutEvents(testEventsm, phiGammaMissing)
CutEvents(testEventm0, phiGammaMissing)
CutEvents(testEventm1, phiGammaMissing)
CutEvents(testEventm2, phiGammaMissing)
CutEvents(testEventm3, phiGammaMissing)
CutEvents(testEventm4, phiGammaMissing)
CutEvents(testEventm5, phiGammaMissing)
CutEvents(testEventm7, phiGammaMissing)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())


lmCut = PhiLeptonMissingCut(1, False, 0)

CutEvents(testEventsm, lmCut)
CutEvents(testEventm0, lmCut)
CutEvents(testEventm1, lmCut)
CutEvents(testEventm2, lmCut)
CutEvents(testEventm3, lmCut)
CutEvents(testEventm4, lmCut)
CutEvents(testEventm5, lmCut)
CutEvents(testEventm7, lmCut)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

"""
raCut = RadiusACut(1, 0.05, 1)

CutEvents(testEventsm, raCut)
CutEvents(testEventm0, raCut)
CutEvents(testEventm1, raCut)
CutEvents(testEventm2, raCut)
CutEvents(testEventm3, raCut)
CutEvents(testEventm4, raCut)
CutEvents(testEventm5, raCut)
CutEvents(testEventm7, raCut)


print(testEventsm.GetEventCount())
print(testEventm0.GetEventCount())
print(testEventm1.GetEventCount())
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventm7.GetEventCount())

testYjjSM1 = HistogramWithMinMax(testEventsm, LpFilter, [0, 1], 20)
print(testYjjSM1.listCount)
testYjjSM2 = HistogramWithMinMax(testEventsm, PhotonDegree, [-1, 1], 20)
print(testYjjSM2.listCount)
"""