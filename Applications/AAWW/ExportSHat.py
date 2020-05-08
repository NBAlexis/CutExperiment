import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent


def Export(eventSetLHCO, eventSetLHE, startIndex, endIndex, file):
    normalizer = 1000.0
    # result_f.write("j1x,j1y,j1z,j2x,j2y,j2z,l1x,l1y,l1z,l2x,l2y,l2z,mx,my,shat\n")
    for i in range(startIndex, endIndex):
        oneEvent = eventSetLHCO.events[i]
        lepton1 = LorentzVector(0, 0, 0, 0)
        lepton2 = LorentzVector(0, 0, 0, 0)
        jet1 = LorentzVector(0, 0, 0, 0)
        jet2 = LorentzVector(0, 0, 0, 0)
        jet3 = LorentzVector(0, 0, 0, 0)
        missing = LorentzVector(0, 0, 0, 0)
        largestJetIndex1 = 0
        largestJetM1 = 0.0
        largestJetIndex2 = 0
        largestJetM2 = 0.0
        largestJetIndex3 = 0
        largestJetM3 = 0.0
        leptonIdx1 = 0
        leptonIdx2 = 0
        leptonCount = 0
        lepton1Found = False
        hasMissing = False
        for oneParticle in oneEvent.particles:
            if ParticleStatus.Outgoing == oneParticle.status \
                    and ParticleType.Jet == oneParticle.particleType:
                momentum = oneParticle.momentum.Momentum()
                if momentum > largestJetM1:
                    largestJetM3 = largestJetM2
                    largestJetIndex3 = largestJetIndex2
                    largestJetM2 = largestJetM1
                    largestJetIndex2 = largestJetIndex1
                    largestJetM1 = momentum
                    largestJetIndex1 = oneParticle.index
                elif momentum > largestJetM2:
                    largestJetM3 = largestJetM2
                    largestJetIndex3 = largestJetIndex2
                    largestJetM2 = momentum
                    largestJetIndex2 = oneParticle.index
                elif momentum > largestJetM3:
                    largestJetM3 = momentum
                    largestJetIndex3 = oneParticle.index
            elif ParticleType.Electron <= oneParticle.particleType <= ParticleType.Muon:
                leptonCount = leptonCount + 1
                if not lepton1Found:
                    lepton1Found = True
                    leptonIdx1 = oneParticle.index
                else:
                    leptonIdx2 = oneParticle.index
            elif ParticleType.Missing == oneParticle.particleType:
                hasMissing = True
                missing = missing + oneParticle.momentum
        if largestJetIndex1 > 0 and largestJetIndex2 > 0:
            jet1 = oneEvent.particles[largestJetIndex1 - 1].momentum
            jet2 = oneEvent.particles[largestJetIndex2 - 1].momentum
            if largestJetIndex3 > 0:
                jet3 = oneEvent.particles[largestJetIndex3 - 1].momentum
        else:
            continue
        if leptonCount != 2:
            continue
        if leptonIdx1 > 0 and leptonIdx2 > 0:
            lepton1 = oneEvent.particles[leptonIdx1 - 1].momentum
            lepton2 = oneEvent.particles[leptonIdx2 - 1].momentum
        else:
            continue
        if not hasMissing:
            print(oneEvent.DebugPrint())
            continue
            # all good
        realShat = SHatWWReal(eventSetLHE.events[i])
        if lepton1.values[1] * lepton1.values[1] + lepton1.values[2] * lepton1.values[2] < 1.0e2:
            continue
        if lepton2.values[1] * lepton2.values[1] + lepton2.values[2] * lepton2.values[2] < 1.0e2:
            continue
        if missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2] < 1.0e2:
            continue
        lepX = lepton1.values[1] + lepton2.values[1]
        lepY = lepton1.values[2] + lepton2.values[2]
        if lepX * lepX + lepY * lepY < 100:
            continue
        lengthLep = math.sqrt(lepX * lepX + lepY * lepY)
        lengthM = math.sqrt(missing.values[1] * missing.values[1] + missing.values[2] * missing.values[2])
        dotLM = (lepX * missing.values[1] + lepY * missing.values[2]) / (lengthLep * lengthM)
        if abs(dotLM) < 0.8:
            continue
        lengthL1 = math.sqrt(lepton1.values[1] * lepton1.values[1]
                             + lepton1.values[2] * lepton1.values[2]
                             + lepton1.values[3] * lepton1.values[3])
        lengthL2 = math.sqrt(lepton2.values[1] * lepton2.values[1]
                             + lepton2.values[2] * lepton2.values[2]
                             + lepton2.values[3] * lepton2.values[3])
        dotLL = (lepton1.values[1] * lepton2.values[1]
                 + lepton1.values[2] * lepton2.values[2]
                 + lepton1.values[3] * lepton2.values[3]) / (lengthL1 * lengthL2)
        if dotLL > -0.5:
            continue
        paramLst = [jet1.values[1] / normalizer,
                    jet1.values[2] / normalizer,
                    jet1.values[3] / normalizer,
                    jet2.values[1] / normalizer,
                    jet2.values[2] / normalizer,
                    jet2.values[3] / normalizer,
                    # jet3.values[1] / normalizer,
                    # jet3.values[2] / normalizer,
                    # jet3.values[3] / normalizer,
                    lepton1.values[1] / normalizer,
                    lepton1.values[2] / normalizer,
                    lepton1.values[3] / normalizer,
                    lepton2.values[1] / normalizer,
                    lepton2.values[2] / normalizer,
                    lepton2.values[3] / normalizer,
                    missing.values[1] / normalizer,
                    missing.values[2] / normalizer]
        strW = ""
        for x in range(0, 14):
            for y in range(x, 14):
                strW = "{}{:.5e},".format(strW, paramLst[x] * paramLst[y])
        strW = "{}{:.5e}\n".format(strW, realShat / (normalizer * normalizer))
        file.write(strW)


trainFile = "../../_DataFolder/wwaa/alpha0train.csv"
testFile = "../../_DataFolder/wwaa/alpha0test.csv"
trainFile = open(trainFile, 'w')
testFile = open(testFile, 'w')

exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhco")
exportEventLHE = LoadLesHouchesEvent("../../_DataFolder/wwaa/newmaxsignal/alpha0.lhe")
Export(exportEventLHCO, exportEventLHE, 0, 40000, trainFile)
Export(exportEventLHCO, exportEventLHE, 40000, 50000, testFile)

exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha1.lhco")
exportEventLHE = LoadLesHouchesEvent("../../_DataFolder/wwaa/newmaxsignal/alpha1.lhe")
Export(exportEventLHCO, exportEventLHE, 0, 40000, trainFile)
Export(exportEventLHCO, exportEventLHE, 40000, 50000, testFile)

exportEventLHCO = LoadLHCOlympics("../../_DataFolder/wwaa/newmaxsignal/alpha2.lhco")
exportEventLHE = LoadLesHouchesEvent("../../_DataFolder/wwaa/newmaxsignal/alpha2.lhe")
Export(exportEventLHCO, exportEventLHE, 0, 40000, trainFile)
Export(exportEventLHCO, exportEventLHE, 40000, 50000, testFile)

trainFile.close()
testFile.close()

print("========== done ===============")
