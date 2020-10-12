from math import *

from CutAndExport.CutEvent import CutEvents
from DataStructure.EventSet import *
from DataStructure.Matrix4x4 import Matrix4x4
from DataStructure.Particles import *
from DataStructure.Constants import *
from Interfaces.BESLogFile import LoadBESCIII

class ParticleTheta:
    """
    If cutType = 0, cut all with cos(theta) > parameters[0]
    If cutType = 1, cut all with cos(theta) < parameters[0]
    """

    def __init__(self, cutType: int, cutValue: float):
        self.cutType = cutType
        self.cutValue = cutValue

    def Cut(self, eventSample: EventSample) -> bool:
        jetCount = 0
        for particle in eventSample.particles:
            if 0 == self.cutType and cos(particle.momentum.Theta()) > self.cutValue:
                return True
            if 1 == self.cutType and cos(particle.momentum.Theta()) < self.cutValue:
                return True
        return False


"""
# This convert the n1,n2,n3,n4 to the rest frame
idx = 0
idx2 = 0
maximumAllowedAngle = 0.93
bSkipFirstLine = True
bFirstLine = True
fileName2 = "_DataFolder/lambda/evt.log"
fileName3 = "_DataFolder/lambda/evt4.log"
with open(fileName2) as f:
    f2 = open(fileName3, "w")
    for lines in f.readlines():
        if bFirstLine:
            bFirstLine = False
            if bSkipFirstLine:
                print("Skip first line")
                continue
        if 17 != len(lines.split()):
            print("line have no 17 element: " + lines)
            continue
        idx = idx + 1
        print(str(idx) + "/8486824")
        valueList = lines.split()
        p1 = LorentzVector(float(valueList[4]), float(valueList[1]), float(valueList[2]), float(valueList[3]))
        p2 = LorentzVector(float(valueList[8]), float(valueList[5]), float(valueList[6]), float(valueList[7]))
        p3 = LorentzVector(float(valueList[12]), float(valueList[9]), float(valueList[10]), float(valueList[11]))
        p4 = LorentzVector(float(valueList[16]), float(valueList[13]), float(valueList[14]), float(valueList[15]))
        if abs(cos(p1.Theta())) > maximumAllowedAngle:
            continue
        if abs(cos(p2.Theta())) > maximumAllowedAngle:
            continue
        if abs(cos(p3.Theta())) > maximumAllowedAngle:
            continue
        if abs(cos(p4.Theta())) > maximumAllowedAngle:
            continue
        plambda1 = p1 + p2
        plambda2 = p3 + p4
        # print("plambda1={} plambda2={}".format(str(plambda1), str(plambda2)))
        # rot to x-z plane
        vfromY = normalize3d(cross3d(normalize3d(plambda1.V3d()), [0, 0, 1]))
        rot1 = Matrix4x4.MakeRotationFromTo(vfromY, [0, 1, 0])
        p1 = rot1.MultiplyVector(p1)
        p2 = rot1.MultiplyVector(p2)
        p3 = rot1.MultiplyVector(p3)
        p4 = rot1.MultiplyVector(p4)
        plambda1 = p1 + p2
        plambda2 = p3 + p4
        # print("plambda1={} plambda2={}".format(str(plambda1), str(plambda2)))
        rotlambda1 = Matrix4x4.MakeRotationFromTo(plambda1.V3d(), [0, 0, 1])
        plambda1dir = rotlambda1.MultiplyVector(plambda1)
        p1dir = rotlambda1.MultiplyVector(p1)
        p2dir = rotlambda1.MultiplyVector(p2)
        # print("plambda1dir={}".format(str(plambda1dir)))
        boostlambda1 = Matrix4x4.MakeBoost(plambda1dir.V3d())
        p1final = boostlambda1.MultiplyVector(p1dir)
        p2final = boostlambda1.MultiplyVector(p2dir)
        # print("p1final + p2final={}".format(str(p1final + p2final)))
        # plambda1dir = boostlambda1.MultiplyVector(plambda1dir)
        # print("plambda1dir={}".format(str(plambda1dir)))
        rotlambda2 = Matrix4x4.MakeRotationFromTo(plambda2.V3d(), [0, 0, 1])
        plambda2dir = rotlambda2.MultiplyVector(plambda2)
        p3dir = rotlambda2.MultiplyVector(p3)
        p4dir = rotlambda2.MultiplyVector(p4)
        boostlambda2 = Matrix4x4.MakeBoost(plambda2dir.V3d())
        p3final = boostlambda2.MultiplyVector(p3dir)
        p4final = boostlambda2.MultiplyVector(p4dir)
        # print("p3final + p4final={}".format(str(p3final + p4final)))
        # only check p1 and p4
        costheta = cos(plambda1.Theta())
        m1 = p1final.Momentum()
        m3 = p3final.Momentum()
        f2.write("{} {} {} {} {} {} {}\n".format(
            costheta,
            p1final.values[1] / m1,
            p1final.values[2] / m1,
            p1final.values[3] / m1,
            p3final.values[1] / m3,
            p3final.values[2] / m3,
            p3final.values[3] / m3
        ))
        f2.flush()

f2.close()
"""

# """
# This is to calculate C matrix
idx = 0
binCount = 40
sep = 2.0 / binCount
fileName3 = "_DataFolder/lambda/evt4.log"
lstn1xn2x = [0 for i in range(binCount)]
lstn1xn2y = [0 for i in range(binCount)]
lstn1xn2z = [0 for i in range(binCount)]
lstn1yn2x = [0 for i in range(binCount)]
lstn1yn2y = [0 for i in range(binCount)]
lstn1yn2z = [0 for i in range(binCount)]
lstn1zn2x = [0 for i in range(binCount)]
lstn1zn2y = [0 for i in range(binCount)]
lstn1zn2z = [0 for i in range(binCount)]
countall = [0 for i in range(binCount)]
with open(fileName3) as f:
    for lines in f.readlines():
        valueList = lines.split()
        lstIdx = floor((float(valueList[0]) + 1.0) / sep)
        if lstIdx < 0:
            lstIdx = 0
        if lstIdx >= binCount:
            lstIdx = binCount - 1
        countall[lstIdx] = countall[lstIdx] + 1
        lstn1xn2x[lstIdx] = lstn1xn2x[lstIdx] + float(valueList[1]) * float(valueList[4])
        lstn1xn2y[lstIdx] = lstn1xn2y[lstIdx] + float(valueList[1]) * float(valueList[5])
        lstn1xn2z[lstIdx] = lstn1xn2z[lstIdx] + float(valueList[1]) * float(valueList[6])
        lstn1yn2x[lstIdx] = lstn1yn2x[lstIdx] + float(valueList[2]) * float(valueList[4])
        lstn1yn2y[lstIdx] = lstn1yn2y[lstIdx] + float(valueList[2]) * float(valueList[5])
        lstn1yn2z[lstIdx] = lstn1yn2z[lstIdx] + float(valueList[2]) * float(valueList[6])
        lstn1zn2x[lstIdx] = lstn1zn2x[lstIdx] + float(valueList[3]) * float(valueList[4])
        lstn1zn2y[lstIdx] = lstn1zn2y[lstIdx] + float(valueList[3]) * float(valueList[5])
        lstn1zn2z[lstIdx] = lstn1zn2z[lstIdx] + float(valueList[3]) * float(valueList[6])
        idx = idx + 1
        print(str(idx) + "/8486824")

fileName4 = "_DataFolder/lambda/evt6.csv"
f = open(fileName4, "w")
for i in range(binCount):
    print("count = {}".format(countall[i]))
    f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(
        lstn1xn2x[i] / countall[i],
        lstn1xn2y[i] / countall[i],
        lstn1xn2z[i] / countall[i],
        lstn1yn2x[i] / countall[i],
        lstn1yn2y[i] / countall[i],
        lstn1yn2z[i] / countall[i],
        lstn1zn2x[i] / countall[i],
        lstn1zn2y[i] / countall[i],
        lstn1zn2z[i] / countall[i]
    ))
f.flush()
f.close()
# """
