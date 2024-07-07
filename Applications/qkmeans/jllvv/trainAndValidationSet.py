import os

import numpy as np

TRAININGCOUNT = 16384
VALIDATIONCOUNT = 30000


os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "sm", "tt", "jjllvv"]
validationset = ["ttj", "ttjj", "ttjjj", "jll", "jjll", "jjjll", "jjjjll", "jlllv", "jlllvb", "pplpv", "jlpv", "ppll", "lllv", "llll", "allvv"]

countlist = []
trainPointSet = None
validationPointSet = None

for i in range(len(trainset)):
    s = np.loadtxt("featurecsv/{}.csv".format(trainset[i]), delimiter=',')
    np.random.shuffle(s)
    if trainPointSet is None:
        trainPointSet = s[0:TRAININGCOUNT]
    else:
        trainPointSet = np.vstack((trainPointSet, s[0:TRAININGCOUNT]))
    tobeadd = None
    if len(s) > (TRAININGCOUNT + VALIDATIONCOUNT):
        tobeadd = s[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT]
    else:
        tobeadd = s[TRAININGCOUNT:]
    if validationPointSet is None:
        validationPointSet = tobeadd
    else:
        validationPointSet = np.vstack((validationPointSet, tobeadd))
    countlist.append(len(tobeadd))

for i in range(len(validationset)):
    s = np.loadtxt("featurecsv/{}.csv".format(validationset[i]), delimiter=',')
    tobeadd = None
    if len(s) > VALIDATIONCOUNT:
        np.random.shuffle(s)
        tobeadd = s[0:VALIDATIONCOUNT]
    else:
        tobeadd = s
    validationPointSet = np.vstack((validationPointSet, tobeadd))
    countlist.append(len(tobeadd))

testPointSet = None
testcountlist = []
for i in range(11):
    s = np.loadtxt("fullcsv/ft0-{}.csv".format(i), delimiter=',')
    if 0 == i:
        testPointSet = s
    else:
        testPointSet = np.vstack((testPointSet, s))
    testcountlist.append(len(s))

traingsetmean = np.mean(trainPointSet, axis=0)
traingsetstd = np.std(trainPointSet, axis=0)

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd
np.savetxt("wf/trainse1-{}.csv".format(TRAININGCOUNT), trainPointSet, delimiter=',')
np.savetxt("wf/trainse2-{}.csv".format(TRAININGCOUNT), trainPointSet / 2, delimiter=',')
trainPointSet = np.hstack((trainPointSet, np.ones((len(trainPointSet), 1))))
traingsetnorm = np.sqrt(np.sum(trainPointSet * trainPointSet, axis=1))
trainPointSet = np.transpose(np.transpose(trainPointSet) / traingsetnorm)

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd
np.savetxt("wf/validationse1-{}.csv".format(TRAININGCOUNT), validationPointSet, delimiter=',')
np.savetxt("wf/validationse2-{}.csv".format(TRAININGCOUNT), validationPointSet / 2, delimiter=',')
validationPointSet = np.hstack((validationPointSet, np.ones((len(validationPointSet), 1))))
validationsetnorm = np.sqrt(np.sum(validationPointSet * validationPointSet, axis=1))
validationPointSet = np.transpose(np.transpose(validationPointSet) / validationsetnorm)

testPointSet = (testPointSet - traingsetmean) / traingsetstd
np.savetxt("wf/testse1-{}.csv".format(TRAININGCOUNT), testPointSet, delimiter=',')
np.savetxt("wf/testse2-{}.csv".format(TRAININGCOUNT), testPointSet / 2, delimiter=',')
testPointSet = np.hstack((testPointSet, np.ones((len(testPointSet), 1))))
testsetnorm = np.sqrt(np.sum(testPointSet * testPointSet, axis=1))
testPointSet = np.transpose(np.transpose(testPointSet) / testsetnorm)

np.savetxt("wf/train-{}.csv".format(TRAININGCOUNT), trainPointSet, delimiter=',')
np.savetxt("wf/validation-{}.csv".format(TRAININGCOUNT), validationPointSet, delimiter=',')
np.savetxt("wf/test-{}.csv".format(TRAININGCOUNT), testPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)
print(testcountlist)

"""

16384:
[ 6.61061068e+02  2.86020133e-01 -8.29084170e-01  4.50397527e-01
  3.09131900e+02  5.59417752e-01 -3.02887809e-01 -3.07655876e-01
  2.95720437e+02 -1.00101533e+00  7.65055265e-02 -3.14585883e-01
  3.67607453e+02  6.29048933e-01  1.31130673e+00]
[509.30639831 209.5628824  209.96847137 779.256823   428.62120252
 274.26318201 273.09011222 359.83281957 425.79727396 266.69408729
 273.26867311 350.64408946 264.46267331 319.08466252 321.33877467]
[30000, 8328, 5542, 30000, 7482, 2655, 1499, 41, 696, 482, 38, 30000, 9326, 15, 2, 13, 4839, 8, 384]
[13940, 13570, 12953, 12686, 12637, 12180, 12297, 12671, 13067, 13612, 14383]

"""