import re

import numpy as np

from Applications.mmvva.exportFunctions import findCS, selectLargestPhotons, findCoff
from Interfaces.LHCOlympics import LoadLHCOlympics

folder1 = "../../_DataFolder/wwaa/signal/"
folder2 = "../../_DataFolder/wwaa/bg/"
folder3 = "../../_DataFolder/wwaa/"

energies = ["3TeV", "10TeV", "14TeV", "30TeV"]
energiesnumber = [3000.0, 10000.0, 14000.0, 30000.0]
namesbg = ["bg", "m2", "m3", "m4", "t0", "t1", "t2", "t5", "t6", "t7"]
paramNames = ["", "fm2", "fm3", "fm4", "ft0", "ft1", "ft2", "ft5", "ft6", "ft7"]

for i in range(len(energies)):
    infoList = []
    infoList.append(["filename", "n1", "n2", "cs", "coeff"])
    for j in range(len(namesbg)):
        fileToLoad = ""
        if 0 == j:
            fileToLoad = folder2
        else:
            fileToLoad = folder1
        eventToLoad = fileToLoad + "{}-{}.lhco".format(namesbg[j], energies[i])
        print("dealing with " + eventToLoad + " ......")
        bannerToLoad = fileToLoad + "{}-{}-banner.txt".format(namesbg[j], energies[i])
        outputFileName = "{}-{}.csv".format(namesbg[j], energies[i])
        cs = findCS(bannerToLoad)
        coeffs = "0"
        if 0 != j:
            coeffs = findCoff(bannerToLoad, paramNames[j])
        events = LoadLHCOlympics(eventToLoad)
        n1 = len(events.events)
        csvlst = selectLargestPhotons(events, energiesnumber[i])
        n2 = len(csvlst)
        csvlst = np.array(csvlst)
        np.savetxt(folder3 + "csv/" + energies[i] + "/" + "bgsignal/" + outputFileName, csvlst, delimiter=',')
        infoList.append([outputFileName, n1, n2, str(cs), coeffs])
    file = open(folder3 + "csv/" + energies[i] + "/" + "bgsignal/info.txt", 'w')
    file.write("n1=event number before particle number cut\nn2=event number after particle number cut\ncs=cross-section before particle number cut(pb)\n")
    file.write(str(np.array(infoList)))
    file.close()




