import os

import numpy as np
from matplotlib import pyplot as plt

from Interfaces.UsefulFunctions import BannerReader, PrintMathematica, ScanReader

os.chdir("../../../_DataFolder/")

h1 = "kmeans/cs/"
h2 = "qkmeans/aqgc/testdata/"
h3 = "kmeans/crossections/"

aqgcs = ["FT0", "FT2", "FT5", "FT7", "FT8", "FT9"]
energies = ["1500", "5000", "7000", "15000"]
scannames = ["scan_run_[01-21].txt", "scan_run_[22-42].txt", "scan_run_[43-63].txt", "scan_run_[64-84].txt"]

toCheckOperator = 0
toCheckEnergy = 0
ansatzType = "l50"
threasholdScore = 485
printCoefAndCS = False
printCountAll = False
showFigure = False

eventsPerFile = 100000
allScores = np.loadtxt(h2 + "Comb-{}-{}.csv".format(energies[toCheckEnergy], ansatzType), delimiter=',')

for toCheckOperator in range(0, 6):
    numberofevents = []
    eventCounts = []
    startpoint = 21 * eventsPerFile * toCheckOperator
    if printCoefAndCS:
        cslst, paramlst = ScanReader(h3 + "{}/{}".format(aqgcs[toCheckOperator], scannames[toCheckEnergy]))
    for i in range(0, 21):
        if printCountAll:
            events = np.loadtxt(h1 + "E{}/{}/{}-{}-{}.csv".format(energies[toCheckEnergy], aqgcs[toCheckOperator], aqgcs[toCheckOperator], energies[toCheckEnergy], i), delimiter=',')
            eventCounts.append(len(events))
        # scores = np.loadtxt(h2 + "{}-{}-{}-{}.csv".format(aqgcs[toCheckOperator], energies[toCheckEnergy], i, ansatzType), delimiter=',')
        scoresThisFile = allScores[(startpoint + i * eventsPerFile):(startpoint + (i + 1) * eventsPerFile)]
        goodpoint = len(scoresThisFile[scoresThisFile > threasholdScore])
        # goodpoint = len(scores[scores > threasholdScore])
        numberofevents.append(goodpoint)
    print(numberofevents)
    if printCountAll:
        print(eventCounts)
    if printCoefAndCS:
        PrintMathematica(cslst)
        PrintMathematica(paramlst)
        print("------")
    if showFigure:
        plt.plot(numberofevents)
        plt.show()


