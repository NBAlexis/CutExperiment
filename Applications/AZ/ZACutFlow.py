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

#jjjll=94335 fb
#sm=3214fb
#fm2=2.811
#fm3=6.791
#fm4=2.884
#fm5=10.87
#ft5=4.455
#ft6=4.462
#ft7=4.420
#ft8=6.250
#ft9=10.33

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
testEventj35 = LoadLHCOlympics("_DataFolder/za/newbackgrounds/jjjll5.lhco")
testEventj3.AddEventSet(testEventj32)
testEventj3.AddEventSet(testEventj33)
testEventj3.AddEventSet(testEventj35)
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
vbsCut = StandardVBFCut(True, 180.0, 0.0)
vbsCut2 = StandardVBFCut(True, 0.0, 1.6)
invllCut = EllInvMass(25, 91.1876)
ellDotCut = DeltaRCutM(0.7)
rCut = RZACut(0.1, -1)
mzaCut = SHatZACut(1000, -1)
deltaRCut = DeltaRCut(0.2)

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

print("============== before DeltaR ===============")
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())

CutEvents(testEventm2, deltaRCut)
CutEvents(testEventm3, deltaRCut)
CutEvents(testEventm4, deltaRCut)
CutEvents(testEventm5, deltaRCut)
CutEvents(testEventt5, deltaRCut)
CutEvents(testEventt6, deltaRCut)
CutEvents(testEventt7, deltaRCut)
CutEvents(testEventt8, deltaRCut)
CutEvents(testEventt9, deltaRCut)

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


CutEvents(testEventsm, ellDotCut)
CutEvents(testEventj3, ellDotCut)
CutEvents(testEventm2, ellDotCut)
CutEvents(testEventm3, ellDotCut)
CutEvents(testEventm4, ellDotCut)
CutEvents(testEventm5, ellDotCut)
CutEvents(testEventt5, ellDotCut)
CutEvents(testEventt6, ellDotCut)
CutEvents(testEventt7, ellDotCut)
CutEvents(testEventt8, ellDotCut)
CutEvents(testEventt9, ellDotCut)

print("============== after theta ll ===============")
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

testEventsmcpy = testEventsm.GetCopy()
testEventj3cpy = testEventj3.GetCopy()
CutEvents(testEventsm, mzaCut)
CutEvents(testEventj3, mzaCut)
CutEvents(testEventsmcpy, mzaCut)
CutEvents(testEventj3cpy, mzaCut)
CutEvents(testEventm2, mzaCut)
CutEvents(testEventm3, mzaCut)
CutEvents(testEventm4, mzaCut)
CutEvents(testEventm5, mzaCut)
CutEvents(testEventt5, mzaCut)
CutEvents(testEventt6, mzaCut)
CutEvents(testEventt7, mzaCut)
CutEvents(testEventt8, mzaCut)
CutEvents(testEventt9, mzaCut)

print("============== after s hat ===============")
print("sm j3 r")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print("sm j3 vbf")
print(testEventsmcpy.GetEventCount())
print(testEventj3cpy.GetEventCount())
print("om")
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print("os")
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())


CutEvents(testEventsm, rCut)
CutEvents(testEventj3, rCut)
CutEvents(testEventsmcpy, vbsCut2)
CutEvents(testEventj3cpy, vbsCut2)
CutEvents(testEventm2, vbsCut2)
CutEvents(testEventm3, vbsCut2)
CutEvents(testEventm4, vbsCut2)
CutEvents(testEventm5, vbsCut2)
CutEvents(testEventt5, rCut)
CutEvents(testEventt6, rCut)
CutEvents(testEventt7, rCut)
CutEvents(testEventt8, rCut)
CutEvents(testEventt9, rCut)

print("============== after r ===============")
print("sm j3 r")
print(testEventsm.GetEventCount())
print(testEventj3.GetEventCount())
print("sm j3 vbf")
print(testEventsmcpy.GetEventCount())
print(testEventj3cpy.GetEventCount())
print("om")
print(testEventm2.GetEventCount())
print(testEventm3.GetEventCount())
print(testEventm4.GetEventCount())
print(testEventm5.GetEventCount())
print("os")
print(testEventt5.GetEventCount())
print(testEventt6.GetEventCount())
print(testEventt7.GetEventCount())
print(testEventt8.GetEventCount())
print(testEventt9.GetEventCount())

"""
2000000
1843772
100000
100000
100000
100000
100000
100000
100000
100000
100000
============== after partical number ===============
442364
14081
24578
21838
24100
21984
19830
23248
20713
20171
20284
============== after vbf ===============
235764
9035
22955
20368
22526
20640
18745
21939
19576
18908
19041
============== after theta ll ===============
16222
1091
20538
18467
20259
18662
16632
19274
17359
16844
16988
============== after inv ll ===============
3026
424
20283
18236
19980
18462
16264
18923
17058
16518
16623
============== after s hat ===============
sm j3 r
89
1
sm j3 vbf
89
1
om
19626
17610
19302
17814
os
16052
18556
16744
16242
16313
============== after r ===============
sm j3 r
47
0
sm j3 vbf
57
1
om
18881
16923
18330
16909
os
13085
14572
13725
13139
13319

Process finished with exit code 0

"""