import numpy as np

from CutAndExport.CutFunctions import FindHardestParticlesByType
from DataStructure.Particles import ParticleType
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

"""
These are events of p p > tau tau~ + invisible
"""

# loadfileName = "sm-mssm.lhe"
# savefileName = "sm-mssm.csv"
loadfileName = "np-mssm.lhe"
savefileName = "np-mssm.csv"
allEvents = LoadLesHouchesEvent(loadfileName)

"""
The LHE does not using detector simulation, so all particles exist
"""
# tauNumberCut = TauNumberCut(1, [2])
# CutEvents(allEvents, tauNumberCut)

dataset = []
for collisionEvent in allEvents.events:
    tauids = FindHardestParticlesByType(collisionEvent, ParticleType.Tau)
    oneCollisionData = collisionEvent.GetParticle(tauids[0]).momentum.values
    oneCollisionData = oneCollisionData + collisionEvent.GetParticle(tauids[1]).momentum.values
    dataset.append(oneCollisionData)

np.savetxt(savefileName, np.array(dataset), delimiter=',')
