import math

from CutAndExport.FilterFunctions import Mjj2Filter
from DataStructure.EventSample import EventSample
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType


def PTMissing(eventSample: EventSample) -> float:
    for i in range(len(eventSample.particles)):
        if ParticleType.Missing == eventSample.particles[i].particleType:
            return math.sqrt(
                (eventSample.particles[i].momentum.values[1] ** 2) + (eventSample.particles[i].momentum.values[2] ** 2))
    return 0.0


def PTMissing1500(eventSample: EventSample) -> float:
    missingMomentum = LorentzVector(3000, 0, 0, 0)
    for i in range(len(eventSample.particles)):
        if ParticleType.Missing != eventSample.particles[i].particleType:
            missingMomentum = missingMomentum - eventSample.particles[i].momentum
    return math.sqrt(
        (missingMomentum.values[1] ** 2) +
        (missingMomentum.values[2] ** 2) +
        (missingMomentum.values[3] ** 2))


class MjjCut:

    def __init__(self, value):
        self.value = value

    def Cut(self, eventSample: EventSample) -> bool:
        mjj = Mjj2Filter(eventSample)
        return mjj < self.value


class PTMissingCut:

    def __init__(self, value):
        self.value = value

    def Cut(self, eventSample: EventSample) -> bool:
        ptmissing = PTMissing(eventSample)
        return ptmissing < self.value
