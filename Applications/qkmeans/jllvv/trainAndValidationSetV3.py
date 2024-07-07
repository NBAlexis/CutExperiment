import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "sm", "tt",
            "jjllvv", "ttj", "ttjj", "ttjjj",
            "jll", "jjll", "jjjll", "jjjjll",
            "jlllv", "jlllvb"]

# """
savefix = 16384
VALIDATIONCOUNT = 30000
trainpick = [16384, 16384, 8192, 8192,
             16384, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
# """


"""
savefix = 256
VALIDATIONCOUNT = 10000
trainpick = [256, 256, 128, 128,
             256, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]
"""

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

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd
trainPointSet = np.hstack((trainPointSet, np.ones((len(trainPointSet), 1))))
traingsetnorm = np.sqrt(np.sum(trainPointSet * trainPointSet, axis=1))
trainPointSet = np.transpose(np.transpose(trainPointSet) / traingsetnorm)

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd
validationPointSet = np.hstack((validationPointSet, np.ones((len(validationPointSet), 1))))
validationsetnorm = np.sqrt(np.sum(validationPointSet * validationPointSet, axis=1))
validationPointSet = np.transpose(np.transpose(validationPointSet) / validationsetnorm)

np.savetxt("wfv3/trainv3-{}.csv".format(savefix), trainPointSet, delimiter=',')
np.savetxt("wfv3/validationv3-{}.csv".format(savefix), validationPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)

"""

16384:
[6.79385429e+02 2.28280163e+02 2.64436537e+02 1.16345988e+02
 1.11732614e+02 5.66218716e+01 4.55104880e+02 3.30837429e+02
 4.49283668e+02 3.27921548e+02 4.72226958e+02 7.55061273e+02
 5.90650681e+02 5.62774658e-01 5.66909790e-01]
[5.14961968e+02 2.25231272e+02 2.36001518e+02 1.29076701e+02
 1.27879597e+02 7.18995572e+01 5.35928460e+02 4.12404251e+02
 5.42554284e+02 4.20542014e+02 3.42961615e+02 6.80359815e+02
 6.66831983e+02 4.96043690e-01 4.95502856e-01]
[30000, 30000, 16262, 12277, 30000, 6546, 20075, 887, 141, 1256, 814, 258, 13628, 9363]

256:

[6.57285699e+02 2.32655068e+02 2.61125956e+02 1.16258604e+02
 1.08168462e+02 5.68321094e+01 4.61647654e+02 3.39645830e+02
 4.67637171e+02 3.32328057e+02 4.77495889e+02 7.22718080e+02
 6.06487483e+02 5.51757812e-01 5.70312500e-01]
[4.97514246e+02 2.29607722e+02 2.28621590e+02 1.34261686e+02
 1.27342615e+02 7.30376010e+01 5.33232357e+02 4.23932382e+02
 5.92795943e+02 4.34935985e+02 3.58212018e+02 6.50723636e+02
 7.02358822e+02 4.97313914e-01 4.95031466e-01]
[10000, 10000, 10000, 10000, 10000, 6546, 10000, 887, 141, 1256, 814, 258, 10000, 9363]




"""