import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/gqgc/")
nsm = 8192
senergy = ["1500", "5000", "7000", "15000"]


def normalizDataPoints(v):
    return v / np.transpose(np.array([np.sqrt(np.sum(v * v, axis=1))]))


def pickdata(v, start, end, meansall, stdall):
    v = v[start:end]
    v = (v - meansall) / stdall
    v = np.hstack((
        v,
        np.ones((len(v), 1)),
        np.zeros((len(v), 1)),
        np.zeros((len(v), 1)),
        np.zeros((len(v), 1))
    ))
    return np.array(normalizDataPoints(v))


for energyIdx in range(0, 1):
    smfile = np.loadtxt("SM-" + senergy[energyIdx] + ".csv", delimiter=',')
    ft0file = np.loadtxt("FgT0-" + senergy[energyIdx] + ".csv", delimiter=',')
    datatraining = np.vstack((smfile[0:30000], ft0file[0:30000]))
    means = np.mean(datatraining, axis=0)
    stds = np.std(datatraining, axis=0)
    datatraining = np.vstack((datatraining[0:nsm], datatraining[30000:(30000 + nsm)]))
    datatraining = (datatraining - means) / stds
    datatraining = np.hstack((
        datatraining,
        np.ones((len(datatraining), 1)),
        np.zeros((len(datatraining), 1)),
        np.zeros((len(datatraining), 1)),
        np.zeros((len(datatraining), 1))
    ))
    datatraining = normalizDataPoints(datatraining)
    np.savetxt("wf/gqgcwf{}-{}.csv".format(senergy[energyIdx], nsm),
               datatraining, delimiter=',')
    """
    ft1file = np.loadtxt("FgT1-" + senergy[energyIdx] + ".csv", delimiter=',')
    ft2file = np.loadtxt("FgT2-" + senergy[energyIdx] + ".csv", delimiter=',')
    ft3file = np.loadtxt("FgT3-" + senergy[energyIdx] + ".csv", delimiter=',')
    np.savetxt("gqgctest{}-Comb-{}.csv".format(senergy[energyIdx], nsm),
               np.vstack((
                   pickdata(smfile, 30000, 130000, means, stds),
                   pickdata(ft0file, 30000, 130000, means, stds),
                   pickdata(ft1file, 30000, 130000, means, stds),
                   pickdata(ft2file, 30000, 130000, means, stds),
                   pickdata(ft3file, 30000, 130000, means, stds)
                          )),
               delimiter=',')
    """
