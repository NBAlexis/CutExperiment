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

cutType = 1
jetNumberCut = JetNumberCut(1, [2])
photonNumberCut = PhotonNumberCut(1, [1])
leptonNumberCut = LeptonPMCut(False, 1, 0)
vbfCut = StandardVBFCut(True, 0.0, 2.0)
ptMissingCutM = PtMissing(1, 120)
megammaCut = MeGammaCut(1, False, 800)
thetaGammaLeptonCut = ThetaGammaLeptonCut(0, False, 0)
phiGammaMissingCut = PhiGammaMissingCut(0, -0.75)
lmCut = PhiLeptonMissingCut(1, False, 0)
ptMissingCutT = PtMissing(1, 75)
r2Cut = RadiusACut(1, 0.15, 3)
r1Cut = RadiusACut(1, 0.15, 2)

#fileHeader = "wa/fittings/fm0/fm0-"
fileHeader = "wa/fittings/fm5/fm5-"

event0 = LoadLHCOlympics("{}0.lhco".format(fileHeader))
event1 = LoadLHCOlympics("{}1.lhco".format(fileHeader))
event2 = LoadLHCOlympics("{}2.lhco".format(fileHeader))
event3 = LoadLHCOlympics("{}3.lhco".format(fileHeader))
event4 = LoadLHCOlympics("{}4.lhco".format(fileHeader))
event5 = LoadLHCOlympics("{}5.lhco".format(fileHeader))
event6 = LoadLHCOlympics("{}6.lhco".format(fileHeader))
event7 = LoadLHCOlympics("{}7.lhco".format(fileHeader))
event8 = LoadLHCOlympics("{}8.lhco".format(fileHeader))
event9 = LoadLHCOlympics("{}9.lhco".format(fileHeader))
event10 = LoadLHCOlympics("{}10.lhco".format(fileHeader))


lstCSfm2 = [9.510859, 9.497277, 9.487940, 9.452338, 9.464482, 9.468111, 9.452898, 9.477976, 9.469637, 9.501467, 9.517759]
lstCSfm3 = [9.528, 9.512, 9.490, 9.480, 9.458, 9.467, 9.459, 9.467, 9.480, 9.508, 9.537]
lstCSfm4 = [9.494640, 9.487761, 9.484158, 9.471298, 9.450375, 9.467428, 9.457633, 9.461426, 9.469377, 9.490119, 9.501709]
lstCSfm5 = [9.598661, 9.528272, 9.514946, 9.495662, 9.452598, 9.467065, 9.462070, 9.481284, 9.497909, 9.553497, 9.597163]
lstCSft5 = [9.483595, 9.486116, 9.467484, 9.483185, 9.477002, 9.453485, 9.453840, 9.461221, 9.466951, 9.486543, 9.493931]
lstCSft6 = [9.482633, 9.488846, 9.475363, 9.464999, 9.467833, 9.458731, 9.467364, 9.475578, 9.466784, 9.486712, 9.492641]
lstCSft7 = [9.477430, 9.483161, 9.476230, 9.453199, 9.467709, 9.472897, 9.448550, 9.475297, 9.465846, 9.481408, 9.487982]

lstEventN = [event0.GetEventCount(),
             event1.GetEventCount(),
             event2.GetEventCount(),
             event3.GetEventCount(),
             event4.GetEventCount(),
             event5.GetEventCount(),
             event6.GetEventCount(),
             event7.GetEventCount(),
             event8.GetEventCount(),
             event9.GetEventCount(),
             event10.GetEventCount()]

print(lstEventN)

eventLst = [event0, event1, event2, event3, event4, event5, event6, event7, event8, event9, event10]

if 1 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, vbfCut)
        CutEvents(eventSet, ptMissingCutM)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, thetaGammaLeptonCut)
        CutEvents(eventSet, phiGammaMissingCut)
        CutEvents(eventSet, lmCut)
elif 2 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r1Cut)
        CutEvents(eventSet, ptMissingCutT)
        CutEvents(eventSet, megammaCut)
        CutEvents(eventSet, thetaGammaLeptonCut)
elif 3 == cutType:
    for eventSet in eventLst:
        CutEvents(eventSet, jetNumberCut)
        CutEvents(eventSet, photonNumberCut)
        CutEvents(eventSet, leptonNumberCut)
        CutEvents(eventSet, r2Cut)
        CutEvents(eventSet, ptMissingCutT)
        CutEvents(eventSet, megammaCut)


lstEventN2 = [event0.GetEventCount(),
              event1.GetEventCount(),
              event2.GetEventCount(),
              event3.GetEventCount(),
              event4.GetEventCount(),
              event5.GetEventCount(),
              event6.GetEventCount(),
              event7.GetEventCount(),
              event8.GetEventCount(),
              event9.GetEventCount(),
              event10.GetEventCount()]


for i in range(0, 11):
    print(lstEventN2[i] * lstCSfm5[i] / lstEventN[i])



