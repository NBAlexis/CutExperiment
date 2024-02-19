import os

import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/aqgc/newfeature/")

def findLargestTwoPhotons(events: EventSet):
    ret = []
    for event in events.events:
        photon1 = -1
        photonE1 = 0
        photon2 = -1
        photonE2 = 0
        photon3 = -1
        photonE3 = 0
        for particle in event.particles:
            if ParticleType.Photon == particle.particleType:
                if particle.momentum.values[0] > photonE1:
                    photonE3 = photonE2
                    photon3 = photon2
                    photonE2 = photonE1
                    photon2 = photon1
                    photonE1 = particle.momentum.values[0]
                    photon1 = particle.index
                elif particle.momentum.values[0] > photonE2:
                    photonE3 = photonE2
                    photon3 = photon2
                    photonE2 = particle.momentum.values[0]
                    photon2 = particle.index
                elif particle.momentum.values[0] > photonE3:
                    photonE3 = particle.momentum.values[0]
                    photon3 = particle.index
        if photon1 > 0 and photon2 > 0 and photon3 > 0:
            ret.append([
                event.particles[photon1 - 1].momentum.values[0],
                event.particles[photon1 - 1].momentum.values[1],
                event.particles[photon1 - 1].momentum.values[2],
                event.particles[photon1 - 1].momentum.values[3],
                event.particles[photon2 - 1].momentum.values[0],
                event.particles[photon2 - 1].momentum.values[1],
                event.particles[photon2 - 1].momentum.values[2],
                event.particles[photon2 - 1].momentum.values[3],
                event.particles[photon3 - 1].momentum.values[0],
                event.particles[photon3 - 1].momentum.values[1],
                event.particles[photon3 - 1].momentum.values[2],
                event.particles[photon3 - 1].momentum.values[3]
            ])
    return np.array(ret)


for energies in ["1500", "5000", "7000", "15000"]:
    for fileheads in ["SM", "FT0"]:
        fileName = "{}-{}".format(fileheads, energies)
        lhcoevent = LoadLHCOlympics(fileName + ".lhco")
        tobeSavedArray = findLargestTwoPhotons(lhcoevent)
        np.savetxt(fileName + ".csv", tobeSavedArray, delimiter=',')
        print(fileName + " saved")
