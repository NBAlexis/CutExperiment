import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/aqgc/testdata")

aqgcs = ["FT0", "FT2", "FT5", "FT7", "FT8", "FT9"]
energies = ["1500", "5000", "7000", "15000"]

toCheckOperator = 0
toCheckEnergy = 0
ansatzType = "l50"
threasholdScore = 475

eventsPerFile = 5000
# allScores = np.loadtxt("Comb-{}-{}.csv".format(energies[toCheckEnergy], ansatzType), delimiter=',')

numberofevents = []
# startpoint = 21 * eventsPerFile * toCheckOperator
for i in range(0, 10):
    scores = np.loadtxt("{}-{}-{}-{}.csv".format(aqgcs[toCheckOperator], energies[toCheckEnergy], i, ansatzType), delimiter=',')
    # scoresThisFile = allScores[(startpoint + i * eventsPerFile):(startpoint + (i + 1) * eventsPerFile)]
    # goodpoint = len(scoresThisFile[scoresThisFile > threasholdScore])
    goodpoint = len(scores[scores > threasholdScore])
    numberofevents.append(goodpoint)

print(numberofevents)
plt.plot(numberofevents)
plt.show()


