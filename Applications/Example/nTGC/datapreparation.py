import numpy as np

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut, JetNumberCut, FindHardestParticlesByType
from DataStructure.Particles import ParticleType

"""
These are events of p p > j j a
"""
from Interfaces.LHCOlympics import LoadLHCOlympics

# loadfileName = "np.lhco"
# savefileName = "np.csv"
loadfileName = "np.lhco"
savefileName = "np.csv"
allEvents = LoadLHCOlympics(loadfileName)

"""
we requires the final state has at least 2 jets and one photon
"""
PhotonNumberCut = PhotonNumberCut(1, [1])
JetNumberCut = JetNumberCut(1, [2])
CutEvents(allEvents, PhotonNumberCut)
CutEvents(allEvents, JetNumberCut)

dataset = []
for collisionEvent in allEvents.events:
    jetids = FindHardestParticlesByType(collisionEvent, ParticleType.Jet)
    photonids = FindHardestParticlesByType(collisionEvent, ParticleType.Photon)
    oneCollisionData = collisionEvent.GetParticle(jetids[0]).momentum.values
    oneCollisionData = oneCollisionData + collisionEvent.GetParticle(jetids[1]).momentum.values
    oneCollisionData = oneCollisionData + collisionEvent.GetParticle(photonids[0]).momentum.values
    dataset.append(oneCollisionData)

np.savetxt(savefileName, np.array(dataset), delimiter=',')
