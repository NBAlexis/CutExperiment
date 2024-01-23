import os

import numpy as np

from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")

def lhcoToCSV(eventSet: EventSet):
    retlst = []
    for events in eventSet.events:
        photonidx1 = -1
        photnenergy1 = 0
        photonidx2 = -1
        photnenergy2 = 0
        photonidx3 = -1
        photnenergy3 = 0
        for particles in events.particles:
            if ParticleType.Photon == particles.particleType:
                if particles.momentum.values[0] > photnenergy1:
                    photnenergy3 = photnenergy2
                    photonidx3 = photonidx2
                    photnenergy2 = photnenergy1
                    photonidx2 = photonidx1
                    photnenergy1 = particles.momentum.values[0]
                    photonidx1 = particles.index
                elif particles.momentum.values[0] > photnenergy2:
                    photnenergy3 = photnenergy2
                    photonidx3 = photonidx2
                    photnenergy2 = particles.momentum.values[0]
                    photonidx2 = particles.index
                elif particles.momentum.values[0] > photnenergy3:
                    photnenergy3 = particles.momentum.values[0]
                    photonidx3 = particles.index
        if photonidx1 >= 0 and photonidx2 >= 0 and photonidx3 >= 0:
            p1 = events.particles[photonidx1 - 1].momentum
            p2 = events.particles[photonidx2 - 1].momentum
            p3 = events.particles[photonidx3 - 1].momentum
            retlst.append([
                p1.values[0],
                p2.values[0],
                p3.values[0],
                p1.Pt(),
                p2.Pt(),
                p3.Pt(),
                p1.PseudoRapidity(),
                p2.PseudoRapidity(),
                p3.PseudoRapidity(),
                LorentzVector.DeltaR(p1, p2),
                LorentzVector.DeltaR(p1, p3),
                LorentzVector.DeltaR(p2, p3),
                (p1 + p2).Mass(),
                (p1 + p3).Mass(),
                (p2 + p3).Mass()
            ])
    return retlst

def v12Tov15CSV(v12data):
    retlst = []
    for onerow in v12data:
        p1 = LorentzVector(onerow[0], onerow[1], onerow[2], onerow[3])
        p2 = LorentzVector(onerow[4], onerow[5], onerow[6], onerow[7])
        p3 = LorentzVector(onerow[8], onerow[9], onerow[10], onerow[11])
        retlst.append([
            p1.values[0],
            p2.values[0],
            p3.values[0],
            p1.Pt(),
            p2.Pt(),
            p3.Pt(),
            p1.PseudoRapidity(),
            p2.PseudoRapidity(),
            p3.PseudoRapidity(),
            LorentzVector.DeltaR(p1, p2),
            LorentzVector.DeltaR(p1, p3),
            LorentzVector.DeltaR(p2, p3),
            (p1 + p2).Mass(),
            (p1 + p3).Mass(),
            (p2 + p3).Mass()
        ])
    return retlst

for i in range(0, 21):
    eventfile = np.loadtxt("_DataFolder/kmeans/cs/E1500/FT0/FT0-1500-{}.csv".format(i), delimiter=',')
    tobesave = np.array(v12Tov15CSV(eventfile))
    np.savetxt("_DataFolder/SVM/E1500T0/ft0-{}.csv".format(i), tobesave, delimiter=',')
