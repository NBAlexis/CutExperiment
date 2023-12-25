from CutAndExport.CutEvent import CutEvents
from CutAndExport.Histogram import HistogramWithMinMax
from DataStructure.EventSample import EventSample
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics
from CutAndExport.CutFunctions import PhotonNumberCut, FindHardestParticlesByType, JetNumberCut

ejasm = LoadLHCOlympics("../../_DataFolder/epntgc/feature/fccehejasm.lhco")
ejanp = LoadLHCOlympics("../../_DataFolder/epntgc/feature/fccehejasignal.lhco")
# ejasm = LoadLHCOlympics("../../_DataFolder/epntgc/feature/fccehvjasm.lhco")
# ejanp = LoadLHCOlympics("../../_DataFolder/epntgc/feature/fccehvjasignal.lhco")

print(len(ejasm.events))
print(len(ejanp.events))

photonNumberCut = PhotonNumberCut(1, [1])
jetNumberCut = JetNumberCut(1, [1])

CutEvents(ejasm, photonNumberCut)
CutEvents(ejanp, photonNumberCut)
CutEvents(ejasm, jetNumberCut)
CutEvents(ejanp, jetNumberCut)

print(len(ejasm.events))
print(len(ejanp.events))


def hardestPhotonPt(eventSample: EventSample) -> float:
    photonIndex = FindHardestParticlesByType(eventSample, ParticleType.Photon)
    return eventSample.particles[photonIndex[0] - 1].momentum.Pt()


def hardestJetPt(eventSample: EventSample) -> float:
    photonIndex = FindHardestParticlesByType(eventSample, ParticleType.Jet)
    return eventSample.particles[photonIndex[0] - 1].momentum.Pt()


HistogramWithMinMax(ejasm, hardestPhotonPt, [0, 2000], 50)
HistogramWithMinMax(ejanp, hardestPhotonPt, [0, 2000], 50)

HistogramWithMinMax(ejasm, hardestJetPt, [0, 2000], 50)
HistogramWithMinMax(ejanp, hardestJetPt, [0, 2000], 50)