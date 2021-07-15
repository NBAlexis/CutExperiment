import os

from Applications.nTGC.nTGCCuts import *
from CutAndExport.CorrelationFunctions import *
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("G:\\ntgc")

idx = 0

particleNumberCut = ParticleNumberNTGCJJA()
mzcut = MjjMZCut(45, 15, 91.1876)
thetaGammaCut1 = ThetaGammaCut(0.9)
deltaPhi2 = DeltaPhiMax(-0.99)
deltaPhi1 = DeltaPhiMax(-0.9995)

fileNames = ["025", "05", "1", "3", "5"]
cutGroup = [[particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, thetaGammaCut1],
            [particleNumberCut, mzcut, deltaPhi2],
            [particleNumberCut, mzcut, deltaPhi1]]
cs = [ReadTXTFile("s025-scan_run_[01-21].txt"),
      ReadTXTFile("s05-scan_run_[22-42].txt"),
      ReadTXTFile("s1-scan_run_[43-63].txt"),
      ReadTXTFile("s3-scan_run_[64-84].txt"),
      ReadTXTFile("s5-scan_run_[85-105].txt")]

finalCS = []

for i in range(0, 21):
    eventSet = LoadLHCOlympics("s" + fileNames[idx] + "-" + str(i) + ".lhco")
    beforeCut = eventSet.GetEventCount()
    print("Events:", i, " before cut is ", beforeCut)
    for cuts in cutGroup[idx]:
        CutEvents(eventSet, cuts)
        print("Events:", i, " after cut {}".format(cuts), " is ", eventSet.GetEventCount())
    finalCount = eventSet.GetEventCount()
    print("Events:", i, " is ", finalCount)
    finalCS = finalCS + [cs[idx][i] * finalCount / beforeCut]

print(finalCS)

"""
s025
[0.5365801136280001, 0.47583085034999995, 0.4230424669319999, 0.378128686728, 0.33635669585600003, 0.30327951329999997, 0.275306990942, 0.25143887848, 0.23533620435599997, 0.22648791309599997, 0.22092551988, 0.222608397946, 0.22577533461000002, 0.24021231322400002, 0.258508618266, 0.28731070851199997, 0.31493104631200003, 0.3528139044, 0.39521902622399996, 0.44582810378, 0.49858166159999995]

s05
[0.27885318850400004, 0.2317097628, 0.19279297148799998, 0.154232879868, 0.12402111664399999, 0.09817445080000001, 0.07637762959200001, 0.058341908394, 0.04485560184, 0.038318419356, 0.035460627504, 0.03865499442, 0.045319297716000004, 0.05652975006000001, 0.07231786940000001, 0.09491250906, 0.11863583015200001, 0.149430382866, 0.183982252578, 0.224682549228, 0.270469088982]

s1
[0.09883120569, 0.08131107684000001, 0.066053376422, 0.052905993215999994, 0.040671109392, 0.030643810158, 0.022779422160000003, 0.016138218624, 0.011629960943999998, 0.008870809625999999, 0.00800451736, 0.009022803248, 0.011508711312000002, 0.0161857476, 0.022042149119999997, 0.029367863262, 0.03983786092, 0.051762023436000004, 0.065294215344, 0.080513206032, 0.097985741364]

s3
[0.0129213158688, 0.0106716056832, 0.0085483221512, 0.0068022516736, 0.005178750972, 0.0038570229752, 0.0028538143142, 0.0019605074160000003, 0.001374161664, 0.0009665447648, 0.0008638528835999999, 0.0009683723492000001, 0.0013523425608, 0.0019706866596, 0.0027957180732, 0.00391506818, 0.005180133546, 0.0068098506, 0.0087132440802, 0.010677937404, 0.012956304377600002]

s5
[0.005847053292799999, 0.0048151922674, 0.00382083316576, 0.0030527998264, 0.0023139323979199998, 0.00174075231078, 0.00119909095368, 0.000803957115, 0.00054378703548, 0.00036090907716, 0.00031180213767999996, 0.00036997027704, 0.0005296449384, 0.00080722893804, 0.0011857050025, 0.0016956676519, 0.0023343991699999998, 0.00298010351954, 0.0038537519147999995, 0.0047787077031, 0.00582824237976]

"""