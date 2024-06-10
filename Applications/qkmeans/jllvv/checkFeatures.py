import os

import numpy as np
import matplotlib.pyplot as plt

from CutAndExport.CutFunctions import FindHardestParticlesByType
from CutAndExport.FilterFunctions import PtSlashFilter
from CutAndExport.Histogram import Histogram, EventObservables
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/jllvv/features/")
loadevent1 = LoadLHCOlympics("ft0.lhco")
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

# """
histres1 = EventObservables(loadevent1, negativeLepton)
"""
histres2 = EventObservables(loadevent2, PtSlashFilter)
histres3 = EventObservables(loadevent3, PtSlashFilter)
histres4 = EventObservables(loadevent4, PtSlashFilter)
"""

plt.hist(histres1, bins=50, range=[0, 5], histtype="step")
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