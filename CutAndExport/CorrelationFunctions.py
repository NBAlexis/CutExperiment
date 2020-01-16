from DataStructure import Constants
from DataStructure.EventSample import *
from DataStructure.EventSet import *
from DataStructure.LorentzVector import *
from DataStructure.Matrix4x4 import Matrix4x4
import re


def AllMomentumSum(event: EventSample, debuged: int) -> LorentzVector:
    momentumSum = LorentzVector()
    for particle in event.particles:
        if particle.particleType in [0, 3, 4]:  # photon, tau and jets
            momentumSum = momentumSum + particle.momentum
            if debuged < 10:
                print(particle.momentum)
    if debuged < 10:
        print(LorentzVector(13000 - momentumSum.values[0], -momentumSum.values[1], -momentumSum.values[2], -momentumSum.values[3]))
    return LorentzVector(13000 - momentumSum.values[0], -momentumSum.values[1], -momentumSum.values[2], -momentumSum.values[3])


def WRestTest(eventSet: EventSet):
    xList = []
    yList = []
    debuged = 0
    for eventSample in eventSet.events:
        largestPhotonIdx = -1
        largestEa = -1.0
        leptonIdx = -1
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        p4lp = eventSample.particles[leptonIdx].momentum
        p4wp = AllMomentumSum(eventSample, debuged)
        if debuged < 10:
            print(p4wp.Mass())
            debuged = debuged + 1
        rotMatrixWp = Matrix4x4.MakeRotationFromTo(p4wp.V3d(), [0.0, 0.0, 1.0])
        p4lpTowpDir = rotMatrixWp.MultiplyVector(p4lp)
        p4wpTowpDir = rotMatrixWp.MultiplyVector(p4wp)
        p4lpInwpRest = Matrix4x4.MakeBoost(p4wpTowpDir.V3d()).MultiplyVector(p4lpTowpDir)
        p3lp = Constants.normalize3d(p4lpInwpRest.P3d())
        # we need cos(theta _lp) and cos(photon)
        yList.append(p3lp[2])
        xList.append(math.cos(momentumPhoton.Theta()))
    import matplotlib.pyplot as plt
    plt.scatter(xList, yList, s=1)
    plt.show()


def LpTest(eventSet: EventSet, fileName: str):
    xList = []
    smallXlist = []
    yList = []
    result_f = open(fileName, 'a')
    for eventSample in eventSet.events:
        missingIdx = -1
        leptonIdx = -1
        largestPhotonIdx = -1
        largestEa = -1.0
        for i in range(len(eventSample.particles)):
            if 0 == eventSample.particles[i].particleType:
                if eventSample.particles[i].momentum.values[0] > largestEa:
                    largestEa = eventSample.particles[i].momentum.values[0]
                    largestPhotonIdx = i
            if 6 == eventSample.particles[i].particleType:
                missingIdx = i
            if 1 == eventSample.particles[i].particleType or 2 == eventSample.particles[i].particleType:
                leptonIdx = i
        pMissing = eventSample.particles[missingIdx].momentum
        pLepton = eventSample.particles[leptonIdx].momentum
        p2Wt = [pMissing.values[1] + pLepton.values[1], pMissing.values[2] + pLepton.values[2]]
        p2Lt = [pLepton.values[1], pLepton.values[2]]
        momentumPhoton = eventSample.particles[largestPhotonIdx].momentum
        lp = (p2Lt[0] * p2Wt[0] + p2Lt[1] * p2Wt[1]) / (p2Wt[0] * p2Wt[0] + p2Wt[1] * p2Wt[1])
        thetaPhoton = math.cos(momentumPhoton.Theta())
        if 0 <= lp <= 1:
            result_f.write("{}, {}\n".format(thetaPhoton, lp))
        if 0 <= lp <= 1:
            yList.append(2 * (lp - 0.5))
            xList.append(math.cos(momentumPhoton.Theta()))
            smallXlist.append(lp)
    result_f.close()
    import matplotlib.pyplot as plt
    plt.scatter(xList, yList, s=1)
    plt.show()


