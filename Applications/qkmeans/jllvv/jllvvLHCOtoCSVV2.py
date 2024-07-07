import os

import numpy as np

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import findJetAndTwoLeptonsV2
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.UsefulFunctions import BannerReaderCS

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

loadfiles1 = ["ft0"]
loadfiles2 = ["jllvvsm1-1", "jllvvsm1-2"]
loadfiles3 = ["jllvvsm2-{}".format(i+1) for i in range(8)] + ["jjll{}".format(i+1) for i in range(2)] + ["jjllnew-{}".format(i+1) for i in range(77)]
loadfiles4 = ["jllvvtt1", "jllvvtt2"] + ["tt0j-{}".format(i+1) for i in range(31)]
loadfiles5 = ["jjllvv-sm1", "jjllvv-sm2", "jjllvv-sm3", "jjllvv-sm4"]
loadfiles6 = ["jlpv-{}".format(i+1) for i in range(48)]
loadfiles7 = ["ppll-{}".format(i+1) for i in range(8)]
loadfiles8 = ["jll-{}".format(i+1) for i in range(4)] + ["jllnew-{}".format(i+1) for i in range(12)]
loadfiles9 = ["jjjll-{}".format(i+1) for i in range(4)]
loadfiles10 = ["pplpv-{}".format(i+1) for i in range(72)]
loadfiles11 = ["ttj-{}".format(i+1) for i in range(2)]
loadfiles12 = ["lllv-{}".format(i+1) for i in range(12)]
loadfiles13 = ["llll-{}".format(i+1) for i in range(1)]
loadfiles14 = ["allvv-{}".format(i+1) for i in range(2)]
loadfiles15 = ["jjjjll-{}".format(i+1) for i in range(2)]
loadfiles16 = ["jlllv-{}".format(i+1) for i in range(6)]
loadfiles17 = ["jlllvb-{}".format(i+1) for i in range(7)]
loadfiles18 = ["ttjj0-1"] + ["ttjj-{}".format(i+2) for i in range(10)]
loadfiles19 = ["jllll-{}".format(i+1) for i in range(1)]
loadfiles20 = ["ttjjj-{}".format(i+1) for i in range(1)]
loadfiles21 = ["ggwwnp-{}".format(i+1) for i in range(1)]
loadfiles22 = ["llvv-{}".format(i+1) for i in range(1)]

loadfiles = [loadfiles1, loadfiles2, loadfiles3, loadfiles4,
             loadfiles5, loadfiles6, loadfiles7, loadfiles8,
             loadfiles9, loadfiles10, loadfiles11, loadfiles12,
             loadfiles13, loadfiles14, loadfiles15, loadfiles16,
             loadfiles17, loadfiles18, loadfiles19, loadfiles20,
             loadfiles21, loadfiles22]

savefiles = ["ft0", "sm", "jjll", "tt",
             "jjllvv", "jlpv", "ppll", "jll",
             "jjjll", "pplpv", "ttj", "lllv",
             "llll", "allvv", "jjjjll", "jlllv",
             "jlllvb", "ttjj", "jllll", "ttjjj",
             "ggwwnp", "llvv"]

FILETYPEIDX = 21
missingcut = 200
leptoncut = -1
jetcut = -1

totale0 = 0
totale1 = 0
lhcoevent = LoadLHCOlympics("features/{}.lhco".format(loadfiles[FILETYPEIDX][0]))
print("{}.lhco loaded with {} events".format(loadfiles[FILETYPEIDX][0], len(lhcoevent.events)))
totale0 = totale0 + len(lhcoevent.events)
filtered = findJetAndTwoLeptonsV2(lhcoevent, missingcut, jetcut, leptoncut)
totale1 = len(filtered)
sbanner = "features/{}-banner.txt".format(loadfiles[FILETYPEIDX][0])
cs = 0.0
if os.path.exists(sbanner):
    cs = BannerReaderCS(sbanner)
print("{} / {}  {} / {}".format(totale1, totale0, (totale1/totale0)*cs, cs))
for i in range(len(loadfiles[FILETYPEIDX])):
    if 0 != i:
        lhcoevent = LoadLHCOlympics("features/{}.lhco".format(loadfiles[FILETYPEIDX][i]))
        print("{}.lhco loaded with {} events".format(loadfiles[FILETYPEIDX][i], len(lhcoevent.events)))
        sbanner = "features/{}-banner.txt".format(loadfiles[FILETYPEIDX][i])
        if os.path.exists(sbanner):
            cs = cs * totale0 + BannerReaderCS(sbanner) * len(lhcoevent.events)
        totale0 = totale0 + len(lhcoevent.events)
        if os.path.exists(sbanner):
            cs = cs / totale0
        newfiltered = findJetAndTwoLeptonsV2(lhcoevent, missingcut, jetcut, leptoncut)
        if 0 == len(filtered):
            filtered = newfiltered
        else:
            if len(newfiltered) > 0:
                filtered = np.vstack((filtered, newfiltered))
        totale1 = len(filtered)
        print("{} / {}  {} / {}".format(totale1, totale0, (totale1/totale0)*cs, cs))


np.savetxt("featurecsvv2/{}.csv".format(savefiles[FILETYPEIDX]), filtered, delimiter=',')

"""
ETMissing = 200

ft0    : 447927 / 902883  0.07365743333123174 / 0.148470720404         32768
ggww   : 494665 / 1000000  0.07661765515320451 / 0.15488796489180456   32768
SM     : 24712 / 2000000  0.014172543569480238 / 1.1470171228132273    16384
jjllvv : 51630 / 2000000                                               16384
tt     : 21926 / 5100000  0.10828809036275493 / 25.187871059475057     16384

validation:
ttj    :                                                            7482 / 1147221  0.1852382791248389 / 28.40273239987661
ttjj   :                                                            26844 / 2556974  0.2200693715554442 / 20.962288081642466
ttjjj  :                                                            1499 / 100000  0.18453767254380798 / 12.310718648686324


jll    : 152 / 9501000  0.007976565908352082 / 498.58784667929694  (489.95593333333335)
jjll   : 1304 / 15756073  0.017208680168021906 / 207.9303841725502 (206.68229309003863)
jjjll  : 910 / 4000000  0.019173959545451057 / 84.28114085912553
jjjjll : 332 / 812683  0.013424810883536725 / 32.86179392549782

jlllvb : 28047 / 3001000  0.0006566058067329633 / 0.07025614240402263
jlllv  : 40740 / 2501000  0.00172817791297052 / 0.10609162887430708   16384

not considered:

pplpv (about 23720pb)                                                             1 / 7200000  0.00164639274691358 / 11854.027777777777
jlpv  (about 6000pb)                                                              2 / 4800000  0.0013449217447916667 / 3227.8121875
ppll  (1660.1875pb)    964/2000000    (0.8pb)        60/2000000     (50fb)        13 / 8000000  0.00269771125 / 1660.13

lllv                                                                              4839 / 1200000  0.0004722522505553229 / 0.11711153144583333
llll                                                                              8 / 100000  1.967086448e-06 / 0.0245885806
allvv  :                                                                          384 / 101484  8.83803777300739e-05 / 0.02335727670197609

jllll  :                                                                          0 / 2001  0.0 / 0.012674003232000039
llvv   :                                                                          2975 / 1000000  0.005744967378307501 / 1.9310814717000002
"""
