import os

import numpy as np
VERSION = 9
K = 1000

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = np.loadtxt("wfv{}/trainv{}se-16384.csv".format(VERSION, VERSION), delimiter=',')
# validationset = np.loadtxt("wfv{}/validationv{}se-16384.csv".format(VERSION, VERSION), delimiter=',')
validationset = np.loadtxt("wfv{}/testv{}-16384se.csv".format(VERSION, VERSION), delimiter=',')

reslst = []
reslst2 = []
for i in range(len(validationset)):
    v = validationset[i]
    d = trainset - v
    d = np.sum(d * d, axis=1)
    indices = np.argpartition(d, K)[:K]
    indices = (indices // 32768)
    counts = np.array([np.count_nonzero(indices == 0), np.count_nonzero(indices == 1)])
    res = 1 - np.argmax(counts)
    counts = counts / K
    print("v: {}, res: {}, count: {}".format(i, res, counts))
    reslst.append(res)
    reslst2.append(counts)

# np.savetxt("wfv{}/validation-16384-classical-K{}.csv".format(VERSION, K), np.array(reslst), delimiter=',')
# np.savetxt("wfv{}/validation-16384-classical-K{}-P.csv".format(VERSION, K), np.array(reslst2), delimiter=',')
np.savetxt("wfv{}/test-16384-classical-K{}.csv".format(VERSION, K), np.array(reslst), delimiter=',')
np.savetxt("wfv{}/test-16384-classical-K{}-P.csv".format(VERSION, K), np.array(reslst2), delimiter=',')


