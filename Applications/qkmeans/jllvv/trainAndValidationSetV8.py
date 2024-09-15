import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "ajllvvnp", "sm",
            "tt", "jjllvv", "ttj", "ttjj",
            "ttjjj", "jll", "jjll", "jjjll",
            "jjjjll", "jlllv", "jlllvb", "ajll",
            "ajjll", "ajllvv"]

savefix = 128
VALIDATIONCOUNT = 30000
trainpick = [24576, 32768, 8192, 16384,
             16384, 32768, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]

countlist = []
trainPointSet = None
validationPointSet = None

"""
            0 pj.values[0],
            1 pj.Pt(),

            2 pj2.values[0],
            3 pj2.Pt(),

            4 pj3.values[0],
            5 pj3.Pt(),

            6 plp.values[0],
            7 plp.Pt(),

            8 plm.values[0],
            9 plm.Pt(),

            10 pa.values[0],
            11 pa.Pt(),

            12 pm.Pt(),

            13 pjall.Mass(),
            14 plall.Mass(),

            15 plpf,
            16 plmf
"""
# pickfeatures = np.array([0, 1, 2, 3, 13, 6, 7, 8, 9, 14, 11, 12]) no good
# pickfeatures = np.array([1, 3, 13, 7, 9, 14, 11, 12]) too bad
# pickfeatures = np.array([0, 1, 2, 3, 4, 5, 13, 6, 7, 8, 9, 14, 11, 12, 15, 16]) no good
# pickfeatures = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16]) just so so
# pickfeatures = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) better
pickfeatures = np.array([0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

for i in range(len(trainset)):
    s = np.loadtxt("featurecsvv8/{}.csv".format(trainset[i]), delimiter=',')
    s = s[:, pickfeatures]
    if trainpick[i] > 0 or len(s) > VALIDATIONCOUNT:
        np.random.shuffle(s)
    if trainpick[i] > 0:
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
print(len(trainPointSet))
traingsetmean = np.mean(trainPointSet, axis=0)
traingsetstd = np.std(trainPointSet, axis=0)

trainPointSet = (trainPointSet - traingsetmean) / traingsetstd / 4
np.savetxt("wfv8/trainv8se.csv", trainPointSet, delimiter=',')

validationPointSet = (validationPointSet - traingsetmean) / traingsetstd / 4
np.savetxt("wfv8/validationv8se.csv", validationPointSet, delimiter=',')

print(traingsetmean)
print(traingsetstd)
print(countlist)
"""


131072
[6.85910115e+02 2.30749490e+02 2.67226221e+02 1.17508353e+02
 4.52143681e+02 3.28681000e+02 4.41386550e+02 3.21509847e+02
 5.20033277e+01 3.95081490e+01 4.73935004e+02 7.64027065e+02
 5.77444966e+02 5.60356140e-01 5.66604614e-01]
[5.18861204e+02 2.31224596e+02 2.38857160e+02 1.31152298e+02
 5.37533632e+02 4.14879854e+02 5.40944472e+02 4.16599289e+02
 2.64055146e+02 2.07119543e+02 3.47499039e+02 6.88043610e+02
 6.59555536e+02 4.96343768e-01 4.95543969e-01]
[30000, 30000, 9376, 8053, 4080, 17019, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697]

"""
