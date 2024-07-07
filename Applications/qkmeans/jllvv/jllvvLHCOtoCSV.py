import os

import numpy as np

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import findJetAndTwoLeptons
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.UsefulFunctions import BannerReaderCS

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

loadfiles1 = ["ft0"]
loadfiles2 = ["jllvvsm1-1", "jllvvsm1-2"]
loadfiles3 = ["jllvvsm2-{}".format(i+1) for i in range(8)] + ["jjll{}".format(i+1) for i in range(2)]
loadfiles4 = ["jllvvtt1", "jllvvtt2"] + ["tt0j-{}".format(i+1) for i in range(31)]
loadfiles5 = ["jjllvv-sm1", "jjllvv-sm2", "jjllvv-sm3", "jjllvv-sm4"]
loadfiles6 = ["jlpv1"]
loadfiles7 = ["ppll-{}".format(i+1) for i in range(8)]
loadfiles8 = ["jll-{}".format(i+1) for i in range(3)]
loadfiles9 = ["jjjll-{}".format(i+1) for i in range(2)]
loadfiles10 = ["pplpv-{}".format(i+1) for i in range(72)]
loadfiles11 = ["ttj-{}".format(i+1) for i in range(2)]
loadfiles12 = ["jlpv-{}".format(i+1) for i in range(48)]
loadfiles13 = ["lllv-{}".format(i+1) for i in range(12)]
loadfiles14 = ["llll-{}".format(i+1) for i in range(1)]
loadfiles15 = ["allvv-{}".format(i+1) for i in range(2)]
loadfiles16 = ["jjjjll-{}".format(i+1) for i in range(1)]
loadfiles17 = ["jlllv-{}".format(i+1) for i in range(6)]
loadfiles18 = ["jlllvb-{}".format(i+1) for i in range(3)]
loadfiles19 = ["ttjj0-1"]
loadfiles20 = ["jllll-{}".format(i+1) for i in range(1)]
loadfiles21 = ["ttjjj-{}".format(i+1) for i in range(1)]

loadfiles = [loadfiles1, loadfiles2, loadfiles3, loadfiles4,
             loadfiles5, loadfiles6, loadfiles7, loadfiles8,
             loadfiles9, loadfiles10, loadfiles11, loadfiles12,
             loadfiles13, loadfiles14, loadfiles15, loadfiles16,
             loadfiles17, loadfiles18, loadfiles19, loadfiles20,
             loadfiles21]

savefiles = ["ft0", "sm", "jjll", "tt",
             "jjllvv", "jlpv", "ppll", "jll",
             "jjjll", "pplpv", "ttj", "jlpv",
             "lllv", "llll", "allvv", "jjjjll",
             "jlllv", "jlllvb", "ttjj", "jllll",
             "ttjjj"]

FILETYPEIDX = 20
missingcut = 200
leptoncut = -1
jetcut = -1

totale0 = 0
totale1 = 0
lhcoevent = LoadLHCOlympics("features/{}.lhco".format(loadfiles[FILETYPEIDX][0]))
print("{}.lhco loaded with {} events".format(loadfiles[FILETYPEIDX][0], len(lhcoevent.events)))
totale0 = totale0 + len(lhcoevent.events)
filtered = findJetAndTwoLeptons(lhcoevent, missingcut, jetcut, leptoncut)
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
        newfiltered = findJetAndTwoLeptons(lhcoevent, missingcut, jetcut, leptoncut)
        if 0 == len(filtered):
            filtered = newfiltered
        else:
            if len(newfiltered) > 0:
                filtered = np.vstack((filtered, newfiltered))
        totale1 = len(filtered)
        print("{} / {}  {} / {}".format(totale1, totale0, (totale1/totale0)*cs, cs))


np.savetxt("featurecsv/{}.csv".format(savefiles[FILETYPEIDX]), filtered, delimiter=',')

"""
ETMissing = 50                         100                          200

ft0    : 520482/902883                 501223/902883                447927/902883           16384
SM     : 543214/2000000                160345/2000000 (88fb)        24712/2000000 (13fb)    16384
jjllvv : 656796/2000000 (0.26pb)       260768/2000000 (100fb)       51630/2000000 (21fb)    16384
tt     : 500288/2000000 (0.33pb)       157358/2000000 (100fb)       21926 / 5100000  0.10828809036275493 / 25.187871059475057 (*23%^2 = 5.7fb) 16384

validation:
ttj    :                                                            7482 / 1147221   0.1852382791248389 / 28.40273239987661 (*23%^2 = 9.8fb)
ttjj   :                                                            2655 / 256974    0.21674342419215695 / 20.978314383561333
ttjjj  :                                                            1499 / 100000    0.18453767254380798 / 12.310718648686324

jll    : 2762/1000000   (1.38pb)       233/1000000    (120fb)       41 / 3000000     0.006696064422222223 / 489.95593333333335
jjll   : 73432/8056073  (1.88pb)       7932/8056073   (200fb)       696 / 8056073    0.01785620313900667 / 206.68229309003863
jjjll  : 18096/1000000  (1.54pb)       2305/1000000   (200fb)       482 / 2000000    0.020308679510154505 / 84.26837971018466
jjjjll :                                                            38 / 100000      0.012294925410330204 / 32.355066869290006

jlllvb :                                                            9326 / 1001000   0.0006544285950270425 / 0.07024265747609582
jlllv  :                                                            40740 / 2501000  0.00172817791297052 / 0.10609162887430708

not considered:

pplpv (about 23720pb)                                                             1/7200000      0.00164639274691358 / 11854.027777777777
jlpv  (about 6000pb)                                                              2 / 4800000    0.0013449217447916667 / 3227.8121875
ppll  (1660.1875pb)    964/2000000    (0.8pb)        60/2000000     (50fb)        13 / 8000000   0.00269771125 / 1660.13

lllv                                                                              4839 / 1200000 0.0004722522505553229 / 0.11711153144583333
llll                                                                              8 / 100000     1.967086448e-06 / 0.0245885806
allvv  :                                                                          384 / 101484   8.83803777300739e-05 / 0.02335727670197609

jllll  :                                                                          0 / 2001       0.0 / 0.012674003232000039 < 0.006fb
"""
