import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

photonEvent13Tev = LoadLesHouchesEvent("photon13tev.lhe")

photonMomentum1 = LorentzVector()
photonMomentum2 = LorentzVector()
energyList = []
maxSq = 0
minSq = 1000000
partList = [0 for i in range(50)]

for event in photonEvent13Tev.events:
    photonFound = 0
    for particle in event.particles:
        if 22 == particle.PGDid:
            if 0 == photonFound:
                photonFound = photonFound + 1
                photonMomentum1 = particle.momentum
            elif 1 == photonFound:
                photonFound = photonFound + 1
                photonMomentum2 = particle.momentum
            else:
                photonFound = photonFound + 1
    if 2 == photonFound:
        photonMomentumSum = photonMomentum1 + photonMomentum2
        sq = photonMomentumSum * photonMomentumSum
        if sq > 0:
            sq = math.sqrt(sq)
        else:
            sq = 0
        if sq < 1070:
            energyList.append(sq)
            idx = math.floor(sq / 40)
            if idx < 0:
                idx = 0
            if idx >= 50:
                idx = 49
            partList[idx] = partList[idx] + 1
        if sq > maxSq:
            maxSq = sq
        if sq < minSq:
            minSq = sq

print(len(energyList))
print(minSq, maxSq)
print(partList)

import matplotlib.pyplot as plt

plt.hist(energyList, 100)
plt.show()
