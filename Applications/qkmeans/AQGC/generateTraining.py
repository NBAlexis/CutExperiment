import os

import numpy as np

os.chdir("../../../_DataFolder/")

senergy = ["1500", "5000", "7000", "15000"]

h1 = "kmeans/cs/"
h2 = "qkmeans/aqgc/newfeature/"
h3 = "qkmeans/aqgc/ansatz/"
h4 = "qkmeans/aqgc/testdata/"


def normalizDataPoints(v):
    return v / np.transpose(np.array([np.sqrt(np.sum(v * v, axis=1))]))


def picktwophoton(v, start, end):
    return v[start:end, [1, 2, 3, 5, 6, 7]]


def pickdata(v, start, end, meansall, stdall):
    v = picktwophoton(v, start, end)
    # v = v[start:end]
    v = (v - meansall) / stdall
    v = np.hstack((
        v,
        np.ones((len(v), 1)),
        np.zeros((len(v), 1))
    ))
    return normalizDataPoints(v)


for energyIdx in range(0, 1):
    smfile = np.loadtxt(h2 + "SM-" + senergy[energyIdx] + ".csv", delimiter=',')
    ft0file = np.loadtxt(h2 + "FT0-" + senergy[energyIdx] + ".csv", delimiter=',')
    datatraining = np.vstack((smfile[0:128], ft0file[0:128]))
    datatraining = picktwophoton(datatraining, 0, len(datatraining))
    means = np.mean(datatraining, axis=0)
    stds = np.std(datatraining, axis=0)
    datatraining = (datatraining - means) / stds
    datatraining = np.hstack((
        datatraining,
        np.ones((len(datatraining), 1)),
        np.zeros((len(datatraining), 1))
    ))
    datatraining = normalizDataPoints(datatraining)
    np.savetxt(h3 + "aqgcwf{}-128.csv".format(senergy[energyIdx]),
               datatraining, delimiter=',')
    np.savetxt(h3 + "validationsm-{}.csv".format(senergy[energyIdx]),
               pickdata(smfile, 4500, 5500, means, stds), delimiter=',')
    np.savetxt(h3 + "validationft0-{}.csv".format(senergy[energyIdx]),
               pickdata(ft0file, 4500, 5500, means, stds), delimiter=',')
    # """
    numberofEventEach = 50000
    csfileCombin = None
    csfileCombinCreated = False
    useCombine = False
    # for headers in ["FT0", "FT2", "FT5", "FT7", "FT8", "FT9"]:
    for headers in ["FT0"]:
        for k in range(0, 21):
            print("dealing with E{}/{}/{}-{}-{}.csv".format(senergy[energyIdx], headers, headers, senergy[energyIdx], k))
            csfile = np.loadtxt(h1 + "E{}/{}/{}-{}-{}.csv".format(senergy[energyIdx], headers, headers, senergy[energyIdx], k), delimiter=',')
            csfile = csfile[:, 0:12]
            if not csfileCombinCreated:
                csfileCombin = pickdata(csfile, 0, numberofEventEach, means, stds)
                csfileCombinCreated = True
            elif useCombine:
                csfileCombin = np.vstack((csfileCombin, pickdata(csfile, 0, numberofEventEach, means, stds)))
            if not useCombine:
                np.savetxt(h4 + "{}-{}-{}.csv".format(headers, senergy[energyIdx], k), csfileCombin, delimiter=',')
                csfileCombinCreated = False
    if useCombine:
        np.savetxt(h4 + "Comb-{}.csv".format(senergy[energyIdx], senergy[energyIdx]), csfileCombin, delimiter=',')
    # """
