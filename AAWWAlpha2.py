from Interfaces.LHCOlympics import LoadLHCOlympics
from CutAndExport.CutFunctions import *
from CutAndExport.CutEvent import CutEvents

folderName = "a1"
fileHeader = "alpha1"
a0 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-0.lhco")
a1 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-1.lhco")
a2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-2.lhco")
a3 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-3.lhco")
a4 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-4.lhco")
a5 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-5.lhco")
a6 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-6.lhco")
a7 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-7.lhco")
a8 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-8.lhco")
a9 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-9.lhco")
a10 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-10.lhco")

hasAdd = False
if hasAdd:
    # ====================== for a4 or a5 =========================
    folderName = "a4b"
    fileHeader = "alpha4-b"
    b0 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-0.lhco")
    b1 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-1.lhco")
    b2 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-2.lhco")
    b3 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-3.lhco")
    b4 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-4.lhco")
    b5 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-5.lhco")
    b6 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-6.lhco")
    b7 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-7.lhco")
    b8 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-8.lhco")
    b9 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-9.lhco")
    b10 = LoadLHCOlympics("F:/PyworkingFolder/CutExperiment/_DataFolder/wwaa/" + folderName + "/" + fileHeader + "-10.lhco")
    a0.AddEventSet(b0)
    a1.AddEventSet(b1)
    a2.AddEventSet(b2)
    a3.AddEventSet(b3)
    a4.AddEventSet(b4)
    a5.AddEventSet(b5)
    a6.AddEventSet(b6)
    a7.AddEventSet(b7)
    a8.AddEventSet(b8)
    a9.AddEventSet(b9)
    a10.AddEventSet(b10)

# alpha 1
crossSection = [824.0, 786.5, 755.5, 733.3, 722.1, 718.5, 721.9, 734.7, 765.7, 786.8, 823.2]
# alpha 2
# crossSection = [736.9, 729.7, 726.4, 721.0, 719.4, 718.2, 719.0, 720.5, 726.3, 731.7, 738.0]
# alpha 3
# crossSection = [736.9, 728.4, 725.9, 720.6, 719.3, 718.5, 719.7, 722.0, 725.9, 732.2, 739.8]
# alpha 4
# crossSection = [723.4, 720.3, 721.2, 718.6, 718.8, 719.4, 719.4, 719.7, 721.0, 722.8, 726.4]
# alpha 4 b
# crossSectionb = [724.2, 720.7, 721.2, 718.8, 718.4, 719.7, 720.4, 719.0, 722.0, 721.4, 725.9]
# alpha 5
# why this is smaller? crossSection = [719.8, 718.9, 720.7, 718.1, 719.9, 717.7, 718.3, 717.8, 719.5, 717.8, 720.2]
# alpha 5 b
# crossSection = [724.0, 723.3, 723.2, 722.9, 722.5, 722.3, 722.9, 722.4, 722.7, 723.6, 724.9]

print(a0.GetEventCount())
print(a1.GetEventCount())
print(a2.GetEventCount())
print(a3.GetEventCount())
print(a4.GetEventCount())
print(a5.GetEventCount())
print(a6.GetEventCount())
print(a7.GetEventCount())
print(a8.GetEventCount())
print(a9.GetEventCount())
print(a10.GetEventCount())

jetNumberCut = JetNumberCut(1, [2])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(a0, jetNumberCut)
CutEvents(a1, jetNumberCut)
CutEvents(a2, jetNumberCut)
CutEvents(a3, jetNumberCut)
CutEvents(a4, jetNumberCut)
CutEvents(a5, jetNumberCut)
CutEvents(a6, jetNumberCut)
CutEvents(a7, jetNumberCut)
CutEvents(a8, jetNumberCut)
CutEvents(a9, jetNumberCut)
CutEvents(a10, jetNumberCut)

CutEvents(a0, leptonNumberCut)
CutEvents(a1, leptonNumberCut)
CutEvents(a2, leptonNumberCut)
CutEvents(a3, leptonNumberCut)
CutEvents(a4, leptonNumberCut)
CutEvents(a5, leptonNumberCut)
CutEvents(a6, leptonNumberCut)
CutEvents(a7, leptonNumberCut)
CutEvents(a8, leptonNumberCut)
CutEvents(a9, leptonNumberCut)
CutEvents(a10, leptonNumberCut)

print(a0.GetEventCount())
print(a1.GetEventCount())
print(a2.GetEventCount())
print(a3.GetEventCount())
print(a4.GetEventCount())
print(a5.GetEventCount())
print(a6.GetEventCount())
print(a7.GetEventCount())
print(a8.GetEventCount())
print(a9.GetEventCount())
print(a10.GetEventCount())

mw=80.379
mz=91.1876
cw=0.876801
sw=0.480853
vev=246
e2=0.0934761 # sqrt{ 4 pi alpha} for alpha = 1/134
shatCutAlpha1 = [SHatCutWW(1000.0 * math.sqrt(32 * math.pi * mw * mw / (abs(-0.12 + i * 0.024) + 1.0e-8))) for i in range(0, 11)]
shatCutAlpha2 = [SHatCutWW(1000.0 * math.sqrt(128 * math.pi * mw * mw / (abs(-0.2 + i * 0.04) + 1.0e-8))) for i in range(0, 11)]
shatCutAlpha3 = [SHatCutWW(1.0e6 * math.sqrt(16 * math.pi / (abs(-2.9 + i * 0.58) + 1.0e-8))) for i in range(0, 11)]
shatCutAlpha4 = [SHatCutWW(1.0e6 * math.sqrt(64 * math.pi / (abs(-5.6 + i * 1.18) + 1.0e-8))) for i in range(0, 11)]
shatCutAlpha5 = [SHatCutWW(1.0e6 * math.sqrt(48 * math.pi / (abs(-2.2 + i * 0.45) + 1.0e-8))) for i in range(0, 11)]

vbfCut = StandardVBFCut(True, 180.0, 2.3)

CutEvents(a0, shatCutAlpha1[0])
CutEvents(a1, shatCutAlpha1[1])
CutEvents(a2, shatCutAlpha1[2])
CutEvents(a3, shatCutAlpha1[3])
CutEvents(a4, shatCutAlpha1[4])
CutEvents(a5, shatCutAlpha1[5])
CutEvents(a6, shatCutAlpha1[6])
CutEvents(a7, shatCutAlpha1[7])
CutEvents(a8, shatCutAlpha1[8])
CutEvents(a9, shatCutAlpha1[9])
CutEvents(a10, shatCutAlpha1[10])

print(a0.GetEventCount())
print(a1.GetEventCount())
print(a2.GetEventCount())
print(a3.GetEventCount())
print(a4.GetEventCount())
print(a5.GetEventCount())
print(a6.GetEventCount())
print(a7.GetEventCount())
print(a8.GetEventCount())
print(a9.GetEventCount())
print(a10.GetEventCount())

CutEvents(a0, vbfCut)
CutEvents(a1, vbfCut)
CutEvents(a2, vbfCut)
CutEvents(a3, vbfCut)
CutEvents(a4, vbfCut)
CutEvents(a5, vbfCut)
CutEvents(a6, vbfCut)
CutEvents(a7, vbfCut)
CutEvents(a8, vbfCut)
CutEvents(a9, vbfCut)
CutEvents(a10, vbfCut)

molCut = MolCut(1, False, 500)

CutEvents(a0, molCut)
CutEvents(a1, molCut)
CutEvents(a2, molCut)
CutEvents(a3, molCut)
CutEvents(a4, molCut)
CutEvents(a5, molCut)
CutEvents(a6, molCut)
CutEvents(a7, molCut)
CutEvents(a8, molCut)
CutEvents(a9, molCut)
CutEvents(a10, molCut)

leptonCut = LeptonPMDotCut(0, False, -0.75)

CutEvents(a0, leptonCut)
CutEvents(a1, leptonCut)
CutEvents(a2, leptonCut)
CutEvents(a3, leptonCut)
CutEvents(a4, leptonCut)
CutEvents(a5, leptonCut)
CutEvents(a6, leptonCut)
CutEvents(a7, leptonCut)
CutEvents(a8, leptonCut)
CutEvents(a9, leptonCut)
CutEvents(a10, leptonCut)

print(a0.GetEventCount())
print(a1.GetEventCount())
print(a2.GetEventCount())
print(a3.GetEventCount())
print(a4.GetEventCount())
print(a5.GetEventCount())
print(a6.GetEventCount())
print(a7.GetEventCount())
print(a8.GetEventCount())
print(a9.GetEventCount())
print(a10.GetEventCount())

lstSets = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

for i in range(11):
    print(str(lstSets[i].GetEventCount() * crossSection[i] / 250000.0) + ", ")
