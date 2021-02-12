from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut, LeptonPMCut, StandardVBFCut, PhiLLMCut, SHatCutWWTest, \
    LeptonPMDotCut, MolCut
from UsefulFunctions import *

lst1 = [16846, 37390]
lst2 = [23654, 52500]

smEvent = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/bgsm.lhco")
ttEvent = LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar.lhco")
ttEvent.AddEventSet(LoadLHCOlympics("../../_DataFolder/wwaa/ttbar/ttbar2.lhco"))

v0Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
v3Event = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha3.lhco")

jetNumberCut = JetNumberCut(2, [2, 3, 4, 5])
leptonNumberCut = LeptonPMCut(False, 1, 1)

CutEvents(smEvent, jetNumberCut)
CutEvents(smEvent, leptonNumberCut)
CutEvents(ttEvent, jetNumberCut)
CutEvents(ttEvent, leptonNumberCut)
CutEvents(v0Event, jetNumberCut)
CutEvents(v0Event, leptonNumberCut)
CutEvents(v3Event, jetNumberCut)
CutEvents(v3Event, leptonNumberCut)


newsm1 = EventSet()
newsm2 = EventSet()
newsm1.events = smEvent.events[0:lst1[0]]
newsm2.events = smEvent.events[0:lst1[1]]
newtt1 = EventSet()
newtt2 = EventSet()
newtt1.events = ttEvent.events[0:lst2[0]]
newtt2.events = ttEvent.events[0:lst2[1]]

newv0 = EventSet()
newv0.events = v0Event.events[0:50]
newv3 = EventSet()
newv3.events = v3Event.events[0:50]

vbfCut = StandardVBFCut(True, 150.0, 1.2)
phillmCut = PhiLLMCut(1, 0.3)
shatCut = SHatCutWWTest(1, 1.5e6)
leptonCut = LeptonPMDotCut(0, False, -0.0)
molCut = MolCut(1, False, 600)

CutEvents(newsm1, vbfCut)
CutEvents(newsm1, phillmCut)
CutEvents(newsm1, shatCut)
CutEvents(newsm1, leptonCut)
CutEvents(newsm1, molCut)

CutEvents(newsm2, vbfCut)
CutEvents(newsm2, phillmCut)
CutEvents(newsm2, shatCut)
CutEvents(newsm2, leptonCut)
CutEvents(newsm2, molCut)

CutEvents(newtt1, vbfCut)
CutEvents(newtt1, phillmCut)
CutEvents(newtt1, shatCut)
CutEvents(newtt1, leptonCut)
CutEvents(newtt1, molCut)

CutEvents(newtt2, vbfCut)
CutEvents(newtt2, phillmCut)
CutEvents(newtt2, shatCut)
CutEvents(newtt2, leptonCut)
CutEvents(newtt2, molCut)

CutEvents(newv0, vbfCut)
CutEvents(newv0, phillmCut)
CutEvents(newv0, shatCut)
CutEvents(newv0, leptonCut)
CutEvents(newv0, molCut)

CutEvents(newv3, vbfCut)
CutEvents(newv3, phillmCut)
CutEvents(newv3, shatCut)
CutEvents(newv3, leptonCut)
CutEvents(newv3, molCut)

print("================ v0 ================")
print(newsm1.GetEventCount())
print(newtt1.GetEventCount())
print(newv0.GetEventCount())

print("================ v3 ================")
print(newsm2.GetEventCount())
print(newtt2.GetEventCount())
print(newv3.GetEventCount())


"""
from Applications.AZ.ZGammaCuts import ParticleNumberZA, DeltaRCut, SHatZA, InvMass, DeltaR
from CutAndExport.CutEvent import CutEvents
from UsefulFunctions import *


#########################################################
# 我们把所有的事例拿来比较一下event selection strategy和 isolate forest
# IsItCutted，如果是0，则被event selection strategy判断为SM，否则是QGC
#########################################################
def IsItCutted(eventSample: EventSample) -> int:
    shat = SHatZA(eventSample)
    if shat < 1000.0:
        return 0
    largestJetIndex1 = 0
    largestJetM1 = 0.0
    largestJetIndex2 = 0
    largestJetM2 = 0.0
    finalV = LorentzVector()
    for particle in eventSample.particles:
        if ParticleStatus.Outgoing == particle.status \
                and ParticleType.Jet == particle.particleType:
            momentum = particle.momentum.Momentum()
            finalV = finalV + particle.momentum
            if momentum > largestJetM1:
                largestJetM2 = largestJetM1
                largestJetIndex2 = largestJetIndex1
                largestJetM1 = momentum
                largestJetIndex1 = particle.index
            elif momentum > largestJetM2:
                largestJetM2 = momentum
                largestJetIndex2 = particle.index
    if largestJetIndex1 > 0 and largestJetIndex2 > 0:
        p1 = eventSample.particles[largestJetIndex1 - 1].momentum
        p2 = eventSample.particles[largestJetIndex2 - 1].momentum
    else:
        return True
    yjj = abs(p1.Y() - p2.Y())
    beforeSqrt = 2.0 * (finalV * finalV)
    mjj = math.sqrt(0.0 if beforeSqrt < 0.0 else beforeSqrt)
    if yjj < 1.6:
        return 0
    if mjj < 180.0:
        return 0
    deltaMZ = abs(InvMass(eventSample) - 91.1876)
    if deltaMZ > 25.0:
        return 0
    deltaR = DeltaR(eventSample)
    if deltaR > 0.7:
        return 0
    return 1


def ChooseEventsAZAndTagWithCut(allEvents: EventSet, count: int) -> list:
    result = []
    idx = 0
    while ((count > 0) and (len(result) < count)) or ((count <= 0) and (len(allEvents.events) > idx)):
        theEvent = allEvents.events[idx]
        largestJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        largestJetEnergy = 0
        secondJetIndex = -1  # 对于一个list, list[i] 这个i通常叫index
        secondJetEnergy = 0
        largestElectronIndex = -1
        largestElectronEnergy = 0
        largestAntiElectronIndex = -1
        largestAntiElectronEnergy = 0
        largestMuonIndex = -1
        largestMuonEnergy = 0
        largestAntiMuonIndex = -1
        largestAntiMuonEnergy = 0
        largestPhotonIndex = -1
        largestPhotonEnergy = 0
        for theParticle in theEvent.particles:
            if theParticle.particleType == ParticleType.Jet:
                jetEnergy = theParticle.momentum.Momentum()
                if jetEnergy > largestJetEnergy:
                    secondJetIndex = largestJetIndex
                    secondJetEnergy = largestJetEnergy
                    largestJetIndex = theParticle.index - 1
                    largestJetEnergy = jetEnergy
                elif jetEnergy > secondJetEnergy:
                    secondJetIndex = theParticle.index - 1
                    secondJetEnergy = jetEnergy
            elif theParticle.particleType == ParticleType.Electron or theParticle.particleType == ParticleType.Muon:
                particleEnergy = theParticle.momentum.Momentum()
                if theParticle.PGDid > 0:
                    if theParticle.particleType == ParticleType.Electron:
                        if particleEnergy > largestElectronEnergy:
                            largestElectronEnergy = particleEnergy
                            largestElectronIndex = theParticle.index - 1
                    else:
                        if particleEnergy > largestMuonEnergy:
                            largestMuonEnergy = particleEnergy
                            largestMuonIndex = theParticle.index - 1
                else:
                    if theParticle.particleType == ParticleType.Electron:
                        if particleEnergy > largestAntiElectronEnergy:
                            largestAntiElectronEnergy = particleEnergy
                            largestAntiElectronIndex = theParticle.index - 1
                    else:
                        if particleEnergy > largestAntiMuonEnergy:
                            largestAntiMuonEnergy = particleEnergy
                            largestAntiMuonIndex = theParticle.index - 1
            elif theParticle.particleType == ParticleType.Photon:
                photonEnergy = theParticle.momentum.Momentum()
                if photonEnergy > largestPhotonEnergy:
                    largestPhotonEnergy = photonEnergy
                    largestPhotonIndex = theParticle.index - 1
        if largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestElectronIndex >= 0 and largestAntiElectronIndex > 0 and largestPhotonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestElectronIndex].momentum
            p4 = theEvent.particles[largestAntiElectronIndex].momentum
            p5 = theEvent.particles[largestPhotonIndex].momentum
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            momentumList = [p1 * p2, p1 * p3, p1 * p4, p1 * p5, p2 * p3, p2 * p4, p2 * p5, p3 * p4, p3 * p5, p4 * p5] + [IsItCutted(theEvent), 0, 0]
            result = result + [momentumList]
        elif largestJetIndex >= 0 and secondJetIndex >= 0 \
                and largestMuonIndex >= 0 and largestAntiMuonIndex > 0 and largestPhotonIndex >= 0:
            p1 = theEvent.particles[largestJetIndex].momentum
            p2 = theEvent.particles[secondJetIndex].momentum
            p3 = theEvent.particles[largestMuonIndex].momentum
            p4 = theEvent.particles[largestAntiMuonIndex].momentum
            p5 = theEvent.particles[largestPhotonIndex].momentum
            # length1是一次isolate forest的长度
            # length2是n次isolate forest的平均长度
            momentumList = [p1 * p2, p1 * p3, p1 * p4, p1 * p5, p2 * p3, p2 * p4, p2 * p5, p3 * p4, p3 * p5, p4 * p5] + [IsItCutted(theEvent), 0, 0]
            result = result + [momentumList]
        idx = idx + 1
    print("ChooseEventsAZ Loaded\n")
    return result


testEvent = LoadLHCOlympics("../../_DataFolder/za/newfittings/fm3/fm3-7.lhco")


resultList = ChooseEventsAZAndTagWithCut(testEvent, -1)

SaveCSVFile("dataESSTest.txt", resultList, 0, 12)

print("Finished")

"""
