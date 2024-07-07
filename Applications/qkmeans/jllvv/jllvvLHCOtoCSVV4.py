import os

import numpy as np

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import findJetAndTwoLeptonsV4
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.UsefulFunctions import BannerReaderCS

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

loadfiles1 = ["ft0"]
loadfiles2 = ["jllvvsm1-1", "jllvvsm1-2"]
loadfiles3 = ["jllvvsm2-{}".format(i + 1) for i in range(8)] + ["jjll{}".format(i + 1) for i in range(2)] + [
    "jjllnew-{}".format(i + 1) for i in range(77)]
loadfiles4 = ["jllvvtt1", "jllvvtt2"] + ["tt0j-{}".format(i + 1) for i in range(31)]
loadfiles5 = ["jjllvv-sm1", "jjllvv-sm2", "jjllvv-sm3", "jjllvv-sm4"]
loadfiles6 = ["jlpv-{}".format(i + 1) for i in range(48)]
loadfiles7 = ["ppll-{}".format(i + 1) for i in range(8)]
loadfiles8 = ["jll-{}".format(i + 1) for i in range(4)] + ["jllnew-{}".format(i + 1) for i in range(12)]
loadfiles9 = ["jjjll-{}".format(i + 1) for i in range(4)]
loadfiles10 = ["pplpv-{}".format(i + 1) for i in range(72)]
loadfiles11 = ["ttj-{}".format(i + 1) for i in range(2)]
loadfiles12 = ["lllv-{}".format(i + 1) for i in range(12)]
loadfiles13 = ["llll-{}".format(i + 1) for i in range(1)]
loadfiles14 = ["allvv-{}".format(i + 1) for i in range(2)]
loadfiles15 = ["jjjjll-{}".format(i + 1) for i in range(2)]
loadfiles16 = ["jlllv-{}".format(i + 1) for i in range(6)]
loadfiles17 = ["jlllvb-{}".format(i + 1) for i in range(7)]
loadfiles18 = ["ttjj0-1"] + ["ttjj-{}".format(i + 2) for i in range(10)]
loadfiles19 = ["jllll-{}".format(i + 1) for i in range(1)]
loadfiles20 = ["ttjjj-{}".format(i + 1) for i in range(1)]
loadfiles21 = ["ggwwnp-{}".format(i + 1) for i in range(1)]
loadfiles22 = ["llvv-{}".format(i + 1) for i in range(1)]

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

missingcut = 200
leptoncut = -1
jetcut = -1

for FILETYPEIDX in [1]:
    totale0 = 0
    totale1 = 0
    lhcoevent = LoadLHCOlympics("features/{}.lhco".format(loadfiles[FILETYPEIDX][0]))
    print("{}.lhco loaded with {} events".format(loadfiles[FILETYPEIDX][0], len(lhcoevent.events)))
    totale0 = totale0 + len(lhcoevent.events)
    filtered = findJetAndTwoLeptonsV4(lhcoevent, missingcut, jetcut, leptoncut, 6)
    totale1 = len(filtered)
    sbanner = "features/{}-banner.txt".format(loadfiles[FILETYPEIDX][0])
    cs = 0.0
    if os.path.exists(sbanner):
        cs = BannerReaderCS(sbanner)
    print("{} / {}  {} / {}".format(totale1, totale0, (totale1 / totale0) * cs, cs))
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
            newfiltered = findJetAndTwoLeptonsV4(lhcoevent, missingcut, jetcut, leptoncut, 6)
            if 0 == len(filtered):
                filtered = newfiltered
            else:
                if len(newfiltered) > 0:
                    filtered = np.vstack((filtered, newfiltered))
            totale1 = len(filtered)
            print("{} / {}  {} / {}".format(totale1, totale0, (totale1 / totale0) * cs, cs))

    np.savetxt("featurecsvv4/{}.csv".format(savefiles[FILETYPEIDX]), filtered, delimiter=',')
    print("featurecsvv4/{}.csv saved".format(savefiles[FILETYPEIDX]))

"""
ETMissing = 200

ft0    : 430176 / 902883  0.07073844631088536 / 0.148470720404
ggww   : 449431 / 1000000  0.06961145294928862 / 0.15488796489180456
SM     : 24454 / 2000000  0.01402457836063733 / 1.1470171228132273
jjllvv : 49822 / 2000000  0.0 / 0.0
tt     : 20469 / 5100000  0.10109226131694019 / 25.187871059475057

validation:
ttj    : 6546 / 1147221  0.1620649258421806 / 28.40273239987661
ttjj   : 20075 / 2556974  0.16457653978451578 / 20.962288081642466
ttjjj  : 887 / 100000  0.10919607441384768 / 12.310718648686324


jll    : 141 / 9501000  0.007399314428142393 / 498.58784667929694  (489.95593333333335)
jjll   : 1256 / 15756073  0.01657523181827877 / 207.9303841725502 (206.68229309003863)
jjjll  : 814 / 4000000  0.017151212164832046 / 84.28114085912553
jjjjll : 258 / 812683  0.010432533758892998 / 32.86179392549782

jlllvb : 9363 / 3001000  0.00021919635499129085 / 0.07025614240402263
jlllv  : 13628 / 2501000  0.0005780954491399667 / 0.10609162887430708

not considered:

pplpv 1 / 7200000  0.00164639274691358 / 11854.027777777777
jlpv  0 / 4800000  0.0 / 3227.8121875
ppll  13 / 8000000  0.00269771125 / 1660.13

lllv   : 2195 / 1200000  0.00021421650960300347 / 0.11711153144583333
llll   : 3 / 100000  7.376574180000001e-07 / 0.0245885806
allvv  : 372 / 101484  8.561849092600908e-05 / 0.02335727670197609

jllll  : 0 / 2001  0.0 / 0.012674003232000039
llvv   : 2960 / 1000000  0.0057160011562320005 / 1.9310814717000002
"""
