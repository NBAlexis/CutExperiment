import os

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.UsefulFunctions import BannerReaderCS

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

findeventfunctions = [findJetAndTwoLeptons,
                      findJetAndTwoLeptonsV2,
                      findJetAndTwoLeptonsV3,
                      findJetAndTwoLeptonsV4,
                      findJetAndTwoLeptonsV5,
                      findJetAndTwoLeptonsV6,
                      findJetAndTwoLeptonsV7]

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
loadfiles23 = ["ajll-{}".format(i + 1) for i in range(23)]
loadfiles24 = ["ajllvvnp-{}".format(i + 1) for i in range(5)]
loadfiles25 = ["ajjll-{}".format(i + 1) for i in range(20)]
loadfiles26 = ["ajllvv-{}".format(i + 1) for i in range(11)]

loadfiles = [loadfiles1, loadfiles2, loadfiles3, loadfiles4,
             loadfiles5, loadfiles6, loadfiles7, loadfiles8,
             loadfiles9, loadfiles10, loadfiles11, loadfiles12,
             loadfiles13, loadfiles14, loadfiles15, loadfiles16,
             loadfiles17, loadfiles18, loadfiles19, loadfiles20,
             loadfiles21, loadfiles22, loadfiles23, loadfiles24,
             loadfiles25, loadfiles26]

savefiles = ["ft0", "sm", "jjll", "tt",
             "jjllvv", "jlpv", "ppll", "jll",
             "jjjll", "pplpv", "ttj", "lllv",
             "llll", "allvv", "jjjjll", "jlllv",
             "jlllvb", "ttjj", "jllll", "ttjjj",
             "ggwwnp", "llvv", "ajll", "ajllvvnp",
             "ajjll", "ajllvv"]


missingcut = 200
leptoncut = -1
jetcut = -1

for VERSION in [4]:
    resstrlst = []
    for FILETYPEIDX in range(len(savefiles)):
        totale0 = 0
        totale1 = 0
        lhcoevent = LoadLHCOlympics("features/{}.lhco".format(loadfiles[FILETYPEIDX][0]))
        print("{}.lhco loaded with {} events".format(loadfiles[FILETYPEIDX][0], len(lhcoevent.events)))
        totale0 = totale0 + len(lhcoevent.events)
        filtered = findeventfunctions[VERSION - 1](lhcoevent, missingcut, jetcut, leptoncut, 6)
        totale1 = len(filtered)
        sbanner = "features/{}-banner.txt".format(loadfiles[FILETYPEIDX][0])
        cs = 0.0
        if os.path.exists(sbanner):
            cs = BannerReaderCS(sbanner)
        resstr = "{} / {}  {} / {}".format(totale1, totale0, (totale1 / totale0) * cs, cs)
        print(resstr)
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
                newfiltered = findeventfunctions[VERSION - 1](lhcoevent, missingcut, jetcut, leptoncut, 6)
                if 0 == len(filtered):
                    filtered = newfiltered
                else:
                    if len(newfiltered) > 0:
                        filtered = np.vstack((filtered, newfiltered))
                totale1 = len(filtered)
                resstr = "{}: {} / {}  {} / {}".format(savefiles[FILETYPEIDX], totale1, totale0, (totale1 / totale0) * cs, cs)
                print(resstr)
        resstrlst.append(resstr)
        np.savetxt("featurecsvv{}/{}.csv".format(VERSION, savefiles[FILETYPEIDX]), filtered, delimiter=',')
        print("featurecsvv{}/{}.csv saved".format(VERSION, savefiles[FILETYPEIDX]))
    print(resstrlst)

"""

V4
savefiles = ["ft0", "sm", "jjll", "tt",
             "jjllvv", "jlpv", "ppll", "jll",
             "jjjll", "pplpv", "ttj", "lllv",
             "llll", "allvv", "jjjjll", "jlllv",
             "jlllvb", "ttjj", "jllll", "ttjjj",
             "ggwwnp", "llvv", "ajll", "ajllvvnp",
             "ajjll", "ajllvv"]
['430176 / 902883  0.07073844631088536 / 0.148470720404', 
'24454 / 2000000  0.01402457836063733 / 1.1470171228132273', 
'1256 / 15756073  0.01657523181827877 / 207.9303841725502', 
'20469 / 5100000  0.10109226131694019 / 25.187871059475057', 
'49822 / 2000000  0.0 / 0.0', 
'0 / 4800000  0.0 / 3227.8121875', 
'13 / 8000000  0.00269771125 / 1660.13', 
'141 / 9501000  0.007399314428142393 / 498.58784667929694', 
'814 / 4000000  0.017151212164832046 / 84.28114085912553', 
'1 / 7200000  0.00164639274691358 / 11854.027777777777', 
'6546 / 1147221  0.1620649258421806 / 28.40273239987661', 
'2195 / 1200000  0.00021421650960300347 / 0.11711153144583333', 
'3 / 100000  7.376574180000001e-07 / 0.0245885806', 
'372 / 101484  8.561849092600908e-05 / 0.02335727670197609', 
'258 / 812683  0.010432533758892998 / 32.86179392549782', 
'13628 / 2501000  0.0005780954491399667 / 0.10609162887430708', 
'9363 / 3001000  0.00021919635499129085 / 0.07025614240402263', 
'20075 / 2556974  0.16457653978451578 / 20.962288081642466', 
'0 / 2001  0.0 / 0.012674003232000039', 
'887 / 100000  0.10919607441384768 / 12.310718648686324', 
'449431 / 1000000  0.06961145294928862 / 0.15488796489180456', 
'2960 / 1000000  0.0057160011562320005 / 1.9310814717000002', 
'26 / 2281263  7.423126735118416e-05 / 6.513117063514017', 
'19104 / 44382  0.007480979499961728 / 0.01737964992500531', 
'167 / 2000000  0.00023833607106907 / 2.85432420442', 
'19265 / 1001237  0.0003636891310919217 / 0.018901583937040355']

V567

ETMissing = 200

ft0      427724 / 902883  0.07033523769312358 / 0.148470720404
ggwwnp   446996 / 1000000  0.06923430075477707 / 0.15488796489180456
ajllvvnp 17568 / 44382  0.006879493711020082 / 0.01737964992500531

jllvv    24437 / 2000000  0.014014828715093419 / 1.1470171228132273
jjllvv   49787 / 2000000  0.0 / 0.7 (0.01742545)

tt       20464 / 5100000  0.1010675673257054 / 25.187871059475057
ttj      6543 / 1147221  0.16199065227396697 / 28.40273239987661
ttjj     20071 / 2556974  0.16454374744782152 / 20.962288081642466
ttjjj    887 / 100000  0.10919607441384768 / 12.310718648686324

jll      139 / 9501000  0.0072943596135588125 / 498.58784667929694
jjll     1256 / 15756073  0.01657523181827877 / 207.9303841725502
jjjll    813 / 4000000  0.017130141879617266 / 84.28114085912553
jjjjll   257 / 812683  0.010392097581532946 / 32.86179392549782

jlllv    13520 / 2501000  0.0005735141233029315 / 0.10609162887430708
jlllvb   9307 / 3001000  0.00021788534400341174 / 0.07025614240402263

ajll     22 / 2281263  6.28110723740789e-05 / 6.513117063514017
ajjll    163 / 2000000  0.00023262742266023 / 2.85432420442
ajllvv   18697 / 1001237  0.0003529662955632318 / 0.018901583937040355


"""
