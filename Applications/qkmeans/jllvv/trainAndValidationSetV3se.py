import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "sm", "tt",
            "jjllvv", "ttj", "ttjj", "ttjjj",
            "jll", "jjll", "jjjll", "jjjjll",
            "jlllv", "jlllvb"]

"""
savefix = 16384
VALIDATIONCOUNT = 30000
trainpick = [16384, 16384, 8192, 8192,
             16384, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
"""


# """
savefix = 256
VALIDATIONCOUNT = 10000
trainpick = [256, 256, 128, 128,
             256, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
# """

countlist = []
trainPointSet = None
validationPointSet = None

for i in range(len(trainset)):
    s = np.loadtxt("featurecsvv3/{}.csv".format(trainset[i]), delimiter=',')
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

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd / 4

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd / 4

np.savetxt("wfv3/trainv3se-{}.csv".format(savefix), trainPointSet, delimiter=',')
np.savetxt("wfv3/validationv3se-{}.csv".format(savefix), validationPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)

"""



256:

[6.57847715e+02 2.11674844e+02 2.59575492e+02 1.13792422e+02
 1.13018470e+02 5.84574023e+01 4.68709231e+02 3.47186523e+02
 4.41786379e+02 3.13328721e+02 4.67153730e+02 7.42265545e+02
 5.92068435e+02 5.42968750e-01 5.66406250e-01]
[5.03213589e+02 2.09760442e+02 2.31164893e+02 1.19079064e+02
 1.33447913e+02 7.55230636e+01 5.34399269e+02 4.28461450e+02
 5.53033610e+02 4.08665615e+02 3.40560122e+02 6.81349807e+02
 6.73964174e+02 4.98150265e-01 4.95570590e-01]
[10000, 10000, 10000, 10000, 10000, 6546, 10000, 887, 141, 1256, 814, 258, 10000, 9363]




"""