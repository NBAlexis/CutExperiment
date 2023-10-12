import os

import numpy as np
from matplotlib import pyplot as plt

from Applications.IsolationForest.IsolationTree4 import Split
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut, JetNumberCut, FindHardestParticlesByType
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

"""
These are events of p p > j j a
"""
testEventSM = LoadLHCOlympics("sm.lhco")
testEventNP = LoadLHCOlympics("np.lhco")

"""
we requires the final state has at least 2 jets and one photon
"""
PhotonNumberCut = PhotonNumberCut(1, [1])
JetNumberCut = JetNumberCut(1, [2])
CutEvents(testEventSM, PhotonNumberCut)
CutEvents(testEventSM, JetNumberCut)
CutEvents(testEventNP, PhotonNumberCut)
CutEvents(testEventNP, JetNumberCut)

print(len(testEventSM.events))
print(len(testEventNP.events))

"""
The cross-section is 8.4e4 pb for SM and 2.8e-3 pb for NP
so, after number cuts, the cross-section is 3.0e4pb for SM and 2.1e-3pb for NP

assume the coefficient for nTGC is 300TeV-4, then it was
3.0e4pb for SM and 1.9e2pb for NP

so the number of events are 3500:22, when L=0.116pb-1, assume the luminosity is .116pb-1, we pick 3500 events from SM and 22 events from NP
"""


def ChooseEventWithStratege(allEvents: EventSet, count: int, tag: int):
    result = []
    idx = 0
    while len(result) < count:
        theEvent = allEvents.events[idx]
        jetids = FindHardestParticlesByType(theEvent, ParticleType.Jet)
        photonids = FindHardestParticlesByType(theEvent, ParticleType.Photon)
        toAdd = theEvent.particles[jetids[0]].momentum.values
        toAdd = toAdd + theEvent.particles[jetids[1]].momentum.values
        toAdd = toAdd + theEvent.particles[photonids[0]].momentum.values
        toAdd = toAdd + [tag]
        result.append(toAdd)
        idx = idx + 1
    return result


resultList1 = ChooseEventWithStratege(testEventSM, 3500, 0)
resultList2 = ChooseEventWithStratege(testEventNP, 22, 1)
combinedList = np.hstack((np.vstack((np.array(resultList1), np.array(resultList2))), np.zeros((3522, 1))))

"""
Build 100 isolation forest trees, and find the average depth of the leaves
"""
print(np.shape(combinedList))
averageDepth = np.zeros(3522)

averageDepthOfFirstPoint = 0
averageDepthOfLastPoint = 0
averageDepthListSM = []
averageDepthListNP = []
for i in range(100):
    resSet = Split(combinedList, 12, -1)
    averageDepth = averageDepth + resSet[:, 13]
    averageDepthOfFirstPoint = averageDepthOfFirstPoint + resSet[0, 13]
    averageDepthOfLastPoint = averageDepthOfLastPoint + resSet[3521, 13]
    averageDepthListSM.append(averageDepthOfFirstPoint / (i + 1))
    averageDepthListNP.append(averageDepthOfLastPoint / (i + 1))
averageDepth = averageDepth / 100

"""
Normalize it to anomaly score:
2^{-L/c}
where L is average depth
c(N) = 2H(N-1) - 2(N-1)/N
where H(n) is harmonic number
"""
harmonicNumber = 0
for i in range(3521):
    harmonicNumber = harmonicNumber + (1.0 / (i + 1))

cn = 2*harmonicNumber - 2.0*3521/3522
anomalyScore = np.power(2, -averageDepth / cn)

"""
Depict the anomaly score distribution for SM and NP
"""
fig, ax = plt.subplots()
ax.hist(anomalyScore[0:3500], label="SM", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
ax.hist(anomalyScore[3500:3522], label="NP", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
ax.legend()
ax.set_xlabel('a', fontsize=20)
ax.set_ylabel('1/N dN/{0:.3f}'.format((max(anomalyScore) - min(anomalyScore)) / 10), fontsize=20)
plt.show()

fig, ax = plt.subplots()
ax.plot(averageDepthListSM, label="SM")
ax.plot(averageDepthListNP, label="NP")
ax.legend()
ax.set_xlabel('number of trees', fontsize=20)
ax.set_ylabel('average depth', fontsize=20)
plt.show()
