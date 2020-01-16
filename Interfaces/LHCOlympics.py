from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import Particle, ParticleStatus, ParticleType


def GetPGDIdByType(particleType: int, nTrack: float) -> int:
    if 0 == particleType:
        return 22
    if 6 == particleType:
        return 12
    if nTrack > 0.0:
        if 1 == particleType:
            return -11
        if 2 == particleType:
            return -13
        if 3 == particleType:
            return -15
    else:
        if 1 == particleType:
            return 11
        if 2 == particleType:
            return 13
        if 3 == particleType:
            return 15
    return 1


def LoadLHCOlympics(fileName: str) -> EventSet:
    ret = EventSet()
    oneEvent = None
    particleIndex = 0
    with open(fileName) as f:
        for lines in f.readlines():
            if lines.strip()[0] == "#":  # this is a comment line
                continue
            valueList = lines.split()
            if 3 == len(valueList):
                if oneEvent is None:  # first record
                    oneEvent = EventSample()
                    particleIndex = 0
                else:
                    ret.AddEvent(oneEvent)
                    oneEvent = EventSample()
                    particleIndex = 0
            elif 11 == len(valueList):
                if oneEvent is None:
                    print("The first line should be a start record!\n")
                    oneEvent = EventSample()
                    particleIndex = 0
                particleIndex += 1
                if particleIndex != int(valueList[0]):
                    print("The particle Index is wrong!\n")
                nTrack = float(valueList[6])
                particleType = int(valueList[1])
                oneParticle = Particle(
                    particleIndex,  # index
                    GetPGDIdByType(particleType, nTrack),  # PGD
                    ParticleType(particleType),  # Particle Type
                    ParticleStatus.Invisible if 6 == particleType else ParticleStatus.Outgoing,  # Status
                    LorentzVector.MakeWithRapidity(float(valueList[2]), float(valueList[3]), float(valueList[4]), float(valueList[5])),  # Momentum
                    float(valueList[5]),  # Mass
                    0.0,  # Decay Length
                    0.0  # Hecility
                )
                oneEvent.AddParticle(oneParticle)
            else:
                print("This line is either 3 value nor 11 value: {}\n".format(lines))
        if not (oneEvent is None):
            ret.AddEvent(oneEvent)
    return ret
