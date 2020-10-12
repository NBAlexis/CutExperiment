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

os.chdir("../../_DataFolder/")
testEventsm = LoadLHCOlympics("za/features/azsm14.lhco")
testEventsm2 = LoadLHCOlympics("za/features/azsm2.lhco")
testEventsm3 = LoadLHCOlympics("za/features/azsm3.lhco")
testEventsm4 = LoadLHCOlympics("za/features/azsm4.lhco")
testEventsm.AddEventSet(testEventsm2)
testEventsm.AddEventSet(testEventsm3)
testEventsm.AddEventSet(testEventsm4)
testEventj3 = LoadLHCOlympics("za/backgrounds/jjjll.lhco")
testEventj32 = LoadLHCOlympics("_DataFolder/za/backgrounds/jjjll2.lhco")
testEventj3.AddEventSet(testEventj32)
testEventm2 = LoadLHCOlympics("za/features/azsignalm2.lhco")
testEventm3 = LoadLHCOlympics("za/features/azsignalm3.lhco")
testEventm4 = LoadLHCOlympics("za/features/azsignalm4.lhco")
testEventm5 = LoadLHCOlympics("za/features/azsignalm5.lhco")
testEventt5 = LoadLHCOlympics("za/features/azsignalt5.lhco")
testEventt6 = LoadLHCOlympics("za/features/azsignalt6.lhco")
testEventt7 = LoadLHCOlympics("za/features/azsignalt7.lhco")
testEventt8 = LoadLHCOlympics("za/features/azsignalt8.lhco")
testEventt9 = LoadLHCOlympics("za/features/azsignalt9.lhco")

particleNumberCut = ParticleNumberZA()
invllCut = EllInvMass(10, 91.1876)
ellDotCut = DotEllCut(0.7)
mzaCut = SHatZACut(300, -1)

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

"""
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


CutEvents(testEventsm, ellDotCut)
CutEvents(testEventm2, ellDotCut)
CutEvents(testEventm3, ellDotCut)
CutEvents(testEventm4, ellDotCut)
CutEvents(testEventm5, ellDotCut)
CutEvents(testEventt5, ellDotCut)
CutEvents(testEventt6, ellDotCut)
CutEvents(testEventt7, ellDotCut)
CutEvents(testEventt8, ellDotCut)
CutEvents(testEventt9, ellDotCut)

CutEvents(testEventsm, mzaCut)
CutEvents(testEventm2, mzaCut)
CutEvents(testEventm3, mzaCut)
CutEvents(testEventm4, mzaCut)
CutEvents(testEventm5, mzaCut)
CutEvents(testEventt5, mzaCut)
CutEvents(testEventt6, mzaCut)
CutEvents(testEventt7, mzaCut)
CutEvents(testEventt8, mzaCut)
CutEvents(testEventt9, mzaCut)
"""

# Note: This function save .csv use append, remember to delete the old files
CorrelationDataAndSave(testEventsm, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zasmpl.csv')
CorrelationDataAndSave(testEventj3, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zaj3pl.csv')
CorrelationDataAndSave(testEventm2, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam2pl.csv')
CorrelationDataAndSave(testEventm3, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam3pl.csv')
CorrelationDataAndSave(testEventm4, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam4pl.csv')
CorrelationDataAndSave(testEventm5, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zam5pl.csv')
CorrelationDataAndSave(testEventt5, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat5pl.csv')
CorrelationDataAndSave(testEventt6, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat6pl.csv')
CorrelationDataAndSave(testEventt7, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat7pl.csv')
CorrelationDataAndSave(testEventt8, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat8pl.csv')
CorrelationDataAndSave(testEventt9, LeptonPZ, PhotonDegreeCS, 40, 40, [-1, 1], [-1, 1], 'zat9pl.csv')


# print(testEventsm.GetEventCount())
# print(testEventm2.GetEventCount())
# print(testEventt5.GetEventCount())


# testTlSM = HistogramWithMinMax(testEventsm, LeptonPZ, [-1, 1], 50)
# testTlM2 = HistogramWithMinMax(testEventm2, LeptonPZ, [-1, 1], 50)
# testTlT5 = HistogramWithMinMax(testEventt5, LeptonPZ, [-1, 1], 50)

# ZpAndGammaDirTest(testEventsm)
# ZpAndGammaDirTest(testEventm2)
# ZpAndGammaDirTest(testEventt5)

# print(testTlSM.listCount)
# print(testTlM2.listCount)
# print(testTlT5.listCount)
