import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "sm", "tt",
            "jjllvv", "ttj", "ttjj", "ttjjj",
            "jll", "jjll", "jjjll", "jjjjll",
            "jlllv", "jlllvb"]

savefix = 16384
if 16384 == savefix:
    VALIDATIONCOUNT = 30000
    trainpick = [16384, 16384, 8192, 8192,
                 16384, 0, 0, 0,
                 0, 0, 0, 0,
                 0, 0]


if 2048 == savefix:
    VALIDATIONCOUNT = 20000
    trainpick = [2048, 2048, 1024, 1024,
                 2048, 0, 0, 0,
                 0, 0, 0, 0,
                 0, 0]

if 256 == savefix:
    VALIDATIONCOUNT = 10000
    trainpick = [256, 256, 128, 128,
                 256, 0, 0, 0,
                 0, 0, 0, 0,
                 0, 0]


countlist = []
trainPointSet = None
validationPointSet = None

for i in range(len(trainset)):
    s = np.loadtxt("featurecsvv4/{}.csv".format(trainset[i]), delimiter=',')
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
traingsetstd = np.std(trainPointSet, axis=0) + 1.0e-18

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd
np.savetxt("wfv4/trainv4se-{}.csv".format(savefix), trainPointSet[:, 0:27] / 4, delimiter=',')
trainPointSet = np.hstack((trainPointSet, np.ones((len(trainPointSet), 1))))
traingsetnorm = np.sqrt(np.sum(trainPointSet * trainPointSet, axis=1))
trainPointSet = np.transpose(np.transpose(trainPointSet) / traingsetnorm)

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd
np.savetxt("wfv4/validationv4se-{}.csv".format(savefix), validationPointSet[:, 0:27] / 4, delimiter=',')
validationPointSet = np.hstack((validationPointSet, np.ones((len(validationPointSet), 1))))
validationsetnorm = np.sqrt(np.sum(validationPointSet * validationPointSet, axis=1))
validationPointSet = np.transpose(np.transpose(validationPointSet) / validationsetnorm)

np.savetxt("wfv4/trainv4-{}.csv".format(savefix), trainPointSet, delimiter=',')
np.savetxt("wfv4/validationv4-{}.csv".format(savefix), validationPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)

"""

16384:
[ 6.82807031e+02  5.11558165e-01  1.01761133e+00 -4.07011349e+00
  2.65677068e+02  3.78731301e-01  4.64689653e-02  1.62838913e+00
  1.11714082e+02  2.43658093e-01  3.24546898e-01  5.78583065e-01
  4.60194877e+02  2.47309834e+00 -8.41844063e-01  2.11305441e-01
  4.49507606e+02 -1.89422230e+00 -1.23825862e+00  9.79819286e-01
  7.59001938e+02  5.92810230e+02  5.63247681e-01  5.68038940e-01
  4.73910552e+02 -1.26696906e+00  7.15570077e-01  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
[5.15613521e+02 2.26627035e+02 2.26588836e+02 7.92489965e+02
 2.38133398e+02 1.22532902e+02 1.22943701e+02 3.10910723e+02
 1.28957953e+02 6.40297466e+01 6.53488471e+01 1.43378108e+02
 5.42710431e+02 3.78723558e+02 3.80051424e+02 4.67371846e+02
 5.48889667e+02 3.76318066e+02 3.74838599e+02 4.70331377e+02
 6.87335644e+02 6.68293315e+02 4.95983599e-01 4.95349071e-01
 3.48651394e+02 4.15268757e+02 4.16771817e+02 1.00000000e-18
 1.00000000e-18 1.00000000e-18 1.00000000e-18]
[30000, 30000, 16262, 12277, 30000, 6546, 20075, 887, 141, 1256, 814, 258, 13628, 9363]

Process finished with exit code 0


2048:
[ 6.80436259e+02  1.17145779e+00  6.19146321e+00  1.81653831e+01
  2.63951963e+02  7.48821306e-01 -5.03241412e-01 -2.89484505e+00
  1.12408700e+02 -6.71096070e-01 -1.82704193e+00  7.61366499e-01
  4.62718805e+02 -1.64554777e+00 -4.97449626e+00  2.33073342e+00
  4.40938757e+02  1.08849762e+00 -2.22640015e+00  7.09329885e+00
  7.61688011e+02  5.86203938e+02  5.60058594e-01  5.70312500e-01
  4.73849830e+02  7.84655897e-01  2.96669541e+00  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
[5.16564175e+02 2.24256176e+02 2.28393702e+02 7.91026975e+02
 2.36214522e+02 1.19927287e+02 1.22136935e+02 3.09303248e+02
 1.30400530e+02 6.39091770e+01 6.32834684e+01 1.46168116e+02
 5.43831098e+02 3.72592533e+02 3.86697876e+02 4.70603463e+02
 5.42126335e+02 3.75730302e+02 3.73090136e+02 4.55962694e+02
 6.86822068e+02 6.56970236e+02 4.96379860e-01 4.95031466e-01
 3.46280097e+02 4.14359160e+02 4.15620785e+02 1.00000000e-18
 1.00000000e-18 1.00000000e-18 1.00000000e-18]
[20000, 20000, 20000, 19445, 20000, 6546, 20000, 887, 141, 1256, 814, 258, 13628, 9363]

Process finished with exit code 0



"""
