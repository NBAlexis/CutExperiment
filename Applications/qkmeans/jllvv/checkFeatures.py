import os

import numpy as np
import matplotlib.pyplot as plt

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import jetCount
from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from CutAndExport.FilterFunctions import PtSlashFilter
from CutAndExport.Histogram import Histogram, EventObservables
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/jllvv/features/")
loadevent1 = LoadLHCOlympics("ggwwnp-1.lhco")
loadevent2 = LoadLHCOlympics("ft0.lhco")
# loadevent3 = LoadLHCOlympics("jjjll-1.lhco")
"""
loadevent2 = LoadLHCOlympics("jllvvsm1-1.lhco")
loadevent2.AddEventSet(LoadLHCOlympics("jllvvsm1-2.lhco"))
loadevent3 = LoadLHCOlympics("jllvvsm2-1.lhco")
loadevent3.AddEventSet(LoadLHCOlympics("jllvvsm2-2.lhco"))
loadevent4 = LoadLHCOlympics("jllvvtt1.lhco")
loadevent4.AddEventSet(LoadLHCOlympics("jllvvtt2.lhco"))
"""


def jetdiff(event: EventSample) -> float:
    alljets = FindHardestParticlesByType(event, ParticleType.Jet)
    if 0 == len(alljets):
        return 0
    e1 = event.GetParticle(alljets[0]).momentum.values[0]
    if 1 == len(alljets):
        return e1
    e2 = event.GetParticle(alljets[1]).momentum.values[0]
    return e1 - e2


def jetCount(eventSample: EventSample) -> float:
    lep = 0.0
    for particle in eventSample.particles:
        if ParticleType.Jet == particle.particleType:
            lep = lep + 1.0
    return lep


def positiveLepton(eventSample: EventSample) -> float:
    lep = 0.0
    for particle in eventSample.particles:
        if particle.PGDid > 0:
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                lep = lep + 1.0
    return lep


def negativeLepton(eventSample: EventSample) -> float:
    lep = 0.0
    for particle in eventSample.particles:
        if particle.PGDid < 0:
            if ParticleType.Electron == particle.particleType or ParticleType.Muon == particle.particleType:
                lep = lep + 1.0
    return lep


def jetE(event: EventSample) -> float:
    jets = FindHardestParticlesByType(event, ParticleType.Jet)
    if 0 == len(jets):
        return 0.0
    return event.GetParticle(jets[0]).momentum.values[0]


def positiveE(event: EventSample) -> float:
    lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
    if 0 == len(lps):
        return 0.0
    return event.GetParticle(lps[0]).momentum.values[0]


def nagetiveE(event: EventSample) -> float:
    lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
    if 0 == len(lms):
        return 0.0
    return event.GetParticle(lms[0]).momentum.values[0]


# """
histres1 = EventObservables(loadevent1, jetCount)
histres2 = EventObservables(loadevent2, jetCount)
# histres3 = EventObservables(loadevent1, nagetiveE)
# histres2 = EventObservables(loadevent2, jetCount)
# histres3 = EventObservables(loadevent3, jetCount)
"""
histres2 = EventObservables(loadevent2, PtSlashFilter)
histres3 = EventObservables(loadevent3, PtSlashFilter)
histres4 = EventObservables(loadevent4, PtSlashFilter)
"""

plt.hist(histres1, bins=15, range=[0, 15], histtype="step", color="red")
plt.hist(histres2, bins=15, range=[0, 15], histtype="step", color="green")
# plt.hist(histres3, bins=10, range=[0, 1000], histtype="step", color="blue")
"""
plt.hist(histres2, bins=50, range=[0, 100], histtype="step")
plt.hist(histres3, bins=50, range=[0, 100], histtype="step")
plt.hist(histres4, bins=50, range=[0, 100], histtype="step")
"""
plt.show()

# """

"""
histres1 = Histogram(loadevent1, jetdiff, 50)
histres2 = Histogram(loadevent2, jetdiff, 50)
histres3 = Histogram(loadevent3, jetdiff, 50)
histres4 = Histogram(loadevent4, jetdiff, 50)
"""
