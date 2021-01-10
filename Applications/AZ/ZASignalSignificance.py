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

# ft5-new-0 has problem

os.chdir("../../_DataFolder/za/newfittings")
eventfileNameA = "ft5/ft5"
eventfileNameB = "ft5-new"
usercut = True

particleNumberCut = ParticleNumberZA()
vbsCut = StandardVBFCut(True, 180.0, 0.0)
vbsCut2 = StandardVBFCut(True, 0.0, 1.6)
invllCut = EllInvMass(25, 91.1876)
drCut = DeltaRCutM(0.7)
rCut = RZACut(0.1, -1)
mzaCut = SHatZACut(1000, -1)

mw = 80.379
mz = 91.1876
cw = 0.876801
sw = 0.480853
vev = 246
e2 = 0.0934761  # sqrt{ 4 pi alpha} for alpha = 1/134
smbg = 11.75 if usercut else 14.25

cefm2 = [-8.2e-12, -6.15e-12, -4.1e-12, -2.05e-12, 2.0e-12, 4.0e-12, 6.0e-12, 8.0e-12]
cefm3 = [-21.0e-12, -15.75e-12, -10.5e-12, -5.25e-12, 5.25e-12, 10.5e-12, 15.75e-12, 21.0e-12]
cefm4 = [-15.0e-12, -11.25e-12, -7.5e-12, -3.75e-12, 4.0e-12, 8.0e-12, 12.0e-12, 16.0e-12]
cefm5 = [-25.0e-12, -18.75e-12, -12.5e-12, -6.25e-12, 6.0e-12, 12.0e-12, 18.0e-12, 24.0e-12]
ceft2 = [-0.28e-12, -0.21e-12, -0.14e-12, -0.07e-12, 0.07e-12, 0.14e-12, 0.21e-12, 0.28e-12]
ceft5 = [-0.7e-12, -0.525e-12, -0.35e-12, -0.175e-12, 0.185e-12, 0.37e-12, 0.555e-12, 0.74e-12]
ceft6 = [-1.6e-12, -1.2e-12, -0.8e-12, -0.4e-12, 0.425e-12, 0.85e-12, 1.275e-12, 1.7e-12]
ceft7 = [-2.6e-12, -1.95e-12, -1.3e-12, -0.65e-12, 0.7e-12, 1.4e-12, 2.1e-12, 2.8e-12]
ceft8 = [-0.47e-12, -0.3525e-12, -0.235e-12, -0.1175e-12, 0.1175e-12, 0.235e-12, 0.3525e-12, 0.47e-12]
ceft9 = [-1.3e-12, -0.975e-12, -0.65e-12, -0.325e-12, 0.325e-12, 0.65e-12, 0.975e-12, 1.3e-12]

mzam2 = [math.sqrt(math.sqrt(32 * 3.14159265359 * cw * sw * mz * mz / (abs(cefm2[i]) * e2 * vev * vev))) for i in
         range(0, 8)]
mzam3 = [math.sqrt(math.sqrt(96 * 3.14159265359 * sw * sw * mz * mz / (abs(cefm3[i] + 1.0e-22) * e2 * vev * vev))) for i
         in range(0, 8)]
mzam4 = [math.sqrt(math.sqrt(
    128 * 3.14159265359 * cw * cw * sw * sw * mz * mz / (abs(cefm4[i]) * (cw * cw - sw * sw) * e2 * vev * vev))) for i
         in range(0, 8)]
mzam5 = [math.sqrt(math.sqrt(96 * 3.14159265359 * sw * sw * mz * mz / (abs(cefm5[i]) * e2 * vev * vev))) for i in
         range(0, 8)]
mzat2 = [math.sqrt(math.sqrt(16 * 3.14159265359 / (3 * abs(ceft2[i]) * cw * cw * cw * sw))) for i in range(0, 8)]
mzat5 = [math.sqrt(math.sqrt(2 * 3.14159265359 / (abs(ceft5[i]) * cw * cw * sw * sw))) for i in range(0, 8)]
mzat6 = [math.sqrt(math.sqrt(8 * 3.14159265359 / (abs(ceft6[i]) * (cw * cw - sw * sw)))) for i in range(0, 8)]
mzat7 = [math.sqrt(math.sqrt(16 * 3.14159265359 / (3 * abs(ceft7[i]) * (cw * cw - sw * sw) * cw * sw))) for i in
         range(0, 8)]
mzat8 = [math.sqrt(math.sqrt(3 * 3.14159265359 / (5 * abs(ceft8[i]) * cw * cw * sw * sw))) for i in range(0, 8)]
mzat9 = [math.sqrt(math.sqrt(4 * 3.14159265359 / (3 * abs(ceft9[i]) * cw * cw * sw * sw))) for i in range(0, 8)]

csm2 = [3.215410e+00, 3.217469e+00, 3.213814e+00, 3.212588e+00, 3.212947e+00, 3.212922e+00, 3.213983e+00,
        3.213225e+00, 3.214454e+00, 3.215051e+00, 3.215380e+00]

csm3 = [3.203768e+00, 3.206316e+00, 3.203915e+00, 3.206732e+00, 3.207897e+00, 3.205920e+00, 3.205227e+00,
        3.206619e+00, 3.203864e+00, 3.204256e+00, 3.208087e+00]

csm4 = [3.203609e+00, 3.206203e+00, 3.205216e+00, 3.207030e+00, 3.206418e+00, 3.205890e+00, 3.205941e+00,
        3.206313e+00, 3.204434e+00, 3.204689e+00, 3.206745e+00]

csm5 = [3.208825e+00, 3.206464e+00, 3.209123e+00, 3.205803e+00, 3.207462e+00, 3.207297e+00, 3.204420e+00,
        3.204355e+00, 3.205512e+00, 3.206417e+00, 3.206025e+00]

cst6 = [3.216633e+00, 3.215404e+00, 3.213892e+00, 3.214929e+00, 3.213107e+00, 3.213356e+00, 3.215419e+00,
        3.216316e+00, 3.213690e+00, 3.214740e+00, 3.213266e+00]

cst5 = [3.303006, 3.303974, 3.304534, 3.303556, 3.302258, 3.302601, 3.302754, 3.302576]

cst8 = [3.302875, 3.302347, 3.304139, 3.302024, 3.302585, 3.302273, 3.304855, 3.302232]

cst9 = [3.306318, 3.302258, 3.303408, 3.301470, 3.302400, 3.299432, 3.301730, 3.301839]

cs = cst5
mzaub = mzat5
print(mzaub)
mzaCut2 = [SHatZACut(-1, mzaub[i]) for i in range(0, 8)]

testEvent0 = LoadLHCOlympics(eventfileNameA + "-0.lhco")
testEvent1 = LoadLHCOlympics(eventfileNameA + "-1.lhco")
testEvent2 = LoadLHCOlympics(eventfileNameA + "-2.lhco")
testEvent3 = LoadLHCOlympics(eventfileNameA + "-3.lhco")
testEvent4 = LoadLHCOlympics(eventfileNameA + "-4.lhco")
testEvent5 = LoadLHCOlympics(eventfileNameA + "-5.lhco")
testEvent6 = LoadLHCOlympics(eventfileNameA + "-6.lhco")
testEvent7 = LoadLHCOlympics(eventfileNameA + "-7.lhco")

"""
testEvent0.AddEventSet(LoadLHCOlympics(eventfileNameB + "-0.lhco"))
testEvent1.AddEventSet(LoadLHCOlympics(eventfileNameB + "-1.lhco"))
testEvent2.AddEventSet(LoadLHCOlympics(eventfileNameB + "-2.lhco"))
testEvent3.AddEventSet(LoadLHCOlympics(eventfileNameB + "-3.lhco"))
testEvent4.AddEventSet(LoadLHCOlympics(eventfileNameB + "-4.lhco"))
testEvent5.AddEventSet(LoadLHCOlympics(eventfileNameB + "-5.lhco"))
testEvent6.AddEventSet(LoadLHCOlympics(eventfileNameB + "-6.lhco"))
testEvent7.AddEventSet(LoadLHCOlympics(eventfileNameB + "-7.lhco"))
testEvent8.AddEventSet(LoadLHCOlympics(eventfileNameB + "-8.lhco"))
testEvent9.AddEventSet(LoadLHCOlympics(eventfileNameB + "-9.lhco"))
testEvent10.AddEventSet(LoadLHCOlympics(eventfileNameB + "-10.lhco"))
"""

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm0 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount()]

CutEvents(testEvent0, particleNumberCut)
CutEvents(testEvent1, particleNumberCut)
CutEvents(testEvent2, particleNumberCut)
CutEvents(testEvent3, particleNumberCut)
CutEvents(testEvent4, particleNumberCut)
CutEvents(testEvent5, particleNumberCut)
CutEvents(testEvent6, particleNumberCut)
CutEvents(testEvent7, particleNumberCut)

print("============== after particle number ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, vbsCut)
CutEvents(testEvent1, vbsCut)
CutEvents(testEvent2, vbsCut)
CutEvents(testEvent3, vbsCut)
CutEvents(testEvent4, vbsCut)
CutEvents(testEvent5, vbsCut)
CutEvents(testEvent6, vbsCut)
CutEvents(testEvent7, vbsCut)

print("============== after vbs cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, invllCut)
CutEvents(testEvent1, invllCut)
CutEvents(testEvent2, invllCut)
CutEvents(testEvent3, invllCut)
CutEvents(testEvent4, invllCut)
CutEvents(testEvent5, invllCut)
CutEvents(testEvent6, invllCut)
CutEvents(testEvent7, invllCut)

print("============== after mll cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, drCut)
CutEvents(testEvent1, drCut)
CutEvents(testEvent2, drCut)
CutEvents(testEvent3, drCut)
CutEvents(testEvent4, drCut)
CutEvents(testEvent5, drCut)
CutEvents(testEvent6, drCut)
CutEvents(testEvent7, drCut)

print("============== after ell cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

CutEvents(testEvent0, mzaCut)
CutEvents(testEvent1, mzaCut)
CutEvents(testEvent2, mzaCut)
CutEvents(testEvent3, mzaCut)
CutEvents(testEvent4, mzaCut)
CutEvents(testEvent5, mzaCut)
CutEvents(testEvent6, mzaCut)
CutEvents(testEvent7, mzaCut)

print("============== after shat cut ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

if usercut:
    CutEvents(testEvent0, rCut)
    CutEvents(testEvent1, rCut)
    CutEvents(testEvent2, rCut)
    CutEvents(testEvent3, rCut)
    CutEvents(testEvent4, rCut)
    CutEvents(testEvent5, rCut)
    CutEvents(testEvent6, rCut)
    CutEvents(testEvent7, rCut)
else:
    CutEvents(testEvent0, vbsCut2)
    CutEvents(testEvent1, vbsCut2)
    CutEvents(testEvent2, vbsCut2)
    CutEvents(testEvent3, vbsCut2)
    CutEvents(testEvent4, vbsCut2)
    CutEvents(testEvent5, vbsCut2)
    CutEvents(testEvent6, vbsCut2)
    CutEvents(testEvent7, vbsCut2)

print("============== before unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm1 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount()]


CutEvents(testEvent0, mzaCut2[0])
CutEvents(testEvent1, mzaCut2[1])
CutEvents(testEvent2, mzaCut2[2])
CutEvents(testEvent3, mzaCut2[3])
CutEvents(testEvent4, mzaCut2[4])
CutEvents(testEvent5, mzaCut2[5])
CutEvents(testEvent6, mzaCut2[6])
CutEvents(testEvent7, mzaCut2[7])


print("============== after unitarity bound ============")

print(testEvent0.GetEventCount())
print(testEvent1.GetEventCount())
print(testEvent2.GetEventCount())
print(testEvent3.GetEventCount())
print(testEvent4.GetEventCount())
print(testEvent5.GetEventCount())
print(testEvent6.GetEventCount())
print(testEvent7.GetEventCount())

evnm2 = [testEvent0.GetEventCount(), testEvent1.GetEventCount(), testEvent2.GetEventCount(), testEvent3.GetEventCount(),
         testEvent4.GetEventCount(), testEvent5.GetEventCount(), testEvent6.GetEventCount(), testEvent7.GetEventCount()]

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm1[0] / evnm0[0],
      1000 * cs[1] * evnm1[1] / evnm0[1],
      1000 * cs[2] * evnm1[2] / evnm0[2],
      1000 * cs[3] * evnm1[3] / evnm0[3],
      0.078 if usercut else 0.094,
      1000 * cs[4] * evnm1[4] / evnm0[4],
      1000 * cs[5] * evnm1[5] / evnm0[5],
      1000 * cs[6] * evnm1[6] / evnm0[6],
      1000 * cs[7] * evnm1[7] / evnm0[7]))

print("[{}, {}, {}, {}, {}, {}, {}, {}, {}]".format(
      1000 * cs[0] * evnm2[0] / evnm0[0],
      1000 * cs[1] * evnm2[1] / evnm0[1],
      1000 * cs[2] * evnm2[2] / evnm0[2],
      1000 * cs[3] * evnm2[3] / evnm0[3],
      0.078 if usercut else 0.094,
      1000 * cs[4] * evnm2[4] / evnm0[4],
      1000 * cs[5] * evnm2[5] / evnm0[5],
      1000 * cs[6] * evnm2[6] / evnm0[6],
      1000 * cs[7] * evnm2[7] / evnm0[7]))

