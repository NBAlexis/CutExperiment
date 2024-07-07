import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "sm", "tt",
            "jjllvv", "ttj", "ttjj", "ttjjj",
            "jll", "jjll", "jjjll", "jjjjll",
            "jlllv", "jlllvb", "pplpv", "jlpv",
            "ppll", "lllv", "llll", "allvv",
            "llvv"]

# """
savefix = 16384
VALIDATIONCOUNT = 30000
trainpick = [16384, 16384, 16384, 16384,
             32768, 0, 0, 0,
             0, 0, 0, 0,
             16384, 16384, 0, 0,
             0, 0, 0, 0,
             0]
# """


"""
savefix = 256
VALIDATIONCOUNT = 10000
trainpick = [256, 256, 256, 256,
             512, 0, 0, 0,
             0, 0, 0, 0,
             256, 256, 0, 0,
             0, 0, 0, 0,
             0]
"""

countlist = []
trainPointSet = None
validationPointSet = None

for i in range(len(trainset)):
    s = np.loadtxt("featurecsvv2/{}.csv".format(trainset[i]), delimiter=',')
    if trainpick[i] > 0 or len(s) > VALIDATIONCOUNT:
        np.random.shuffle(s)
    left = 0
    right = 0
    if trainpick[i] > 0:
        left = trainpick[i]
        right = trainpick[i]
        if trainPointSet is None:
            trainPointSet = s[0:trainpick[i]]
        else:
            trainPointSet = np.vstack((trainPointSet, s[0:trainpick[i]]))
    tobeadd = None
    if len(s) > (trainpick[i] + VALIDATIONCOUNT):
        tobeadd = s[trainpick[i]:trainpick[i] + VALIDATIONCOUNT]
    else:
        tobeadd = s[trainpick[i]:]
    if validationPointSet is None:
        validationPointSet = tobeadd
    else:
        validationPointSet = np.vstack((validationPointSet, tobeadd))
    countlist.append(len(tobeadd))

traingsetmean = np.mean(trainPointSet, axis=0)
traingsetstd = np.std(trainPointSet, axis=0)

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd
trainPointSet = np.hstack((trainPointSet, np.ones((len(trainPointSet), 1))))
traingsetnorm = np.sqrt(np.sum(trainPointSet * trainPointSet, axis=1))
trainPointSet = np.transpose(np.transpose(trainPointSet) / traingsetnorm)

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd
validationPointSet = np.hstack((validationPointSet, np.ones((len(validationPointSet), 1))))
validationsetnorm = np.sqrt(np.sum(validationPointSet * validationPointSet, axis=1))
validationPointSet = np.transpose(np.transpose(validationPointSet) / validationsetnorm)

np.savetxt("wfv2/train-{}.csv".format(savefix), trainPointSet, delimiter=',')
np.savetxt("wfv2/validation-{}.csv".format(savefix), validationPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)

"""

16384:
[ 6.82082781e+02  3.59048064e-01 -6.89131177e-01  1.58702189e+00
  2.82663950e+02 -3.05639134e-01  3.49619132e-01 -7.67547315e-02
  1.33896265e+02  1.33498611e-01  1.76807741e-01 -9.74707441e-01
  3.23986200e+02 -6.79863572e-02  7.26505894e-01 -7.98780548e-01
  6.02308442e+00  4.82901256e-02  2.35778761e-02 -4.95877466e-02
  3.09480051e+02 -2.56798943e-01  1.18378824e+00 -1.26651872e+00
  6.25118256e+00  9.57489241e-04  4.26237643e-02  2.39752005e-02
  3.73516097e+02  3.96283638e-01 -1.71697048e+00]
[503.63901796 222.95600848 223.51468145 786.07053278 231.82284553
 132.664456   132.86868892 312.81794581 136.16405224  75.6627909
  75.57785805 157.55392451 434.5314952  278.53818988 279.30052829
 371.74075974  29.17233515  14.99919311  15.22416574  20.7495974
 427.06026084 275.14522307 273.90959808 356.964884    30.98106094
  15.00827781  14.54185696  23.71047238 271.90574514 326.14193375
 327.22368999]
[30000, 30000, 8328, 5542, 18862, 7482, 26844, 1499, 152, 1304, 910, 332, 24356, 11663, 31, 2, 13, 4839, 8, 384, 2975]

Process finished with exit code 0



256:

[ 6.67222779e+02  1.67238593e+00 -6.18198339e+00 -2.71705260e+01
  2.83428907e+02 -4.94097396e+00  3.97102196e+00  8.98954714e-01
  1.30828441e+02  2.27766463e-01 -2.16994112e-01  8.36566658e-01
  3.44489236e+02 -3.58193097e+00  5.44557917e+00 -1.71172228e+01
  5.83862221e+00  1.42452703e-01  2.77485018e-02  2.33616169e-01
  2.99165285e+02  3.44318352e-01  1.07218810e+01 -3.74883034e-01
  6.99810176e+00 -7.64881014e-02 -4.21090654e-01 -2.58314562e-01
  3.71783813e+02  3.65232155e+00 -1.10547175e+01]
[494.06677272 208.80400952 213.72298492 773.33247006 233.79673489
 135.85326435 132.9463337  313.54150068 130.16100084  75.10749175
  74.23355339 150.63539643 457.26991637 286.96317038 290.07910348
 401.17249617  27.80285115  13.51124923  16.10388084  19.10819291
 412.93657394 265.3859808  264.78111006 345.48878753  32.34442715
  13.8015102   19.29591089  23.06666509 270.69107212 325.54366763
 324.6269162 ]
[10000, 10000, 10000, 10000, 10000, 7482, 10000, 1499, 152, 1304, 910, 332, 10000, 10000, 31, 2, 13, 4839, 8, 384, 2975]

Process finished with exit code 0




"""