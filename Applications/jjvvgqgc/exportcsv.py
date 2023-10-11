import os

import numpy as np

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

jetnumberCut = JetNumberCut(1, [2])

os.chdir("../../_DataFolder")


def exportMoemtumCSV(events: EventSet):
    retarray = []
    for sample in events.events:
        largestJetIdx = 0
        largestJetEnergy = -1.0
        secondJetIdx = 0
        secondJetEnergy = -1.0
        for particle in sample.particles:
            if ParticleType.Jet == particle.particleType:
                if particle.momentum.values[0] > largestJetEnergy:
                    secondJetEnergy = largestJetEnergy
                    secondJetIdx = largestJetIdx
                    largestJetEnergy = particle.momentum.values[0]
                    largestJetIdx = particle.index
                elif particle.momentum.values[0] > secondJetEnergy:
                    secondJetEnergy = particle.momentum.values[0]
                    secondJetIdx = particle.index
        p1 = sample.particles[largestJetIdx - 1].momentum
        p2 = sample.particles[secondJetIdx - 1].momentum
        retarray.append([p1.values[0], p1.values[1], p1.values[2], p1.values[3],
                         p2.values[0], p2.values[1], p2.values[2], p2.values[3]])
    return retarray


for energies in ["1500", "5000", "7000", "15000"]:
    for fileheads in ["SM", "FgT0", "FgT1", "FgT2", "FgT3"]:
        fileName = "jjvv/Feature/" + fileheads + "-" + energies + ".lhco"
        if fileheads == "SM":
            fileName = "jjvv/Feature/sm" + energies + ".lhco"
        print("loading " + fileName)
        eventsets = LoadLHCOlympics(fileName)
        CutEvents(eventsets, jetnumberCut)
        tobeSavedArray = np.array(exportMoemtumCSV(eventsets))
        np.savetxt("jjvv/csv/Features/" + fileheads + "-" + energies + ".csv", tobeSavedArray, delimiter=',')
        print("jjvv/csv/Features/" + fileheads + "-" + energies + ".csv" + " saved")
