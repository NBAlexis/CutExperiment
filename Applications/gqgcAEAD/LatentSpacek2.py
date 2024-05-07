import numpy as np
from keras.models import load_model
from matplotlib import pyplot as plt

batch_size = 1024
adamlr = 0.002
num_epoch = 5000
rangessm = [[[-2, 2], [-2, 2]], [[-2, 2], [-2, 2]], [[-5, 5], [-5, 5]], [[-3, 3], [-3, 3]]]
rangesft0 = [[[-6, 6], [-6, 6]], [[-5, 15], [-10, 10]], [[-70, 50], [-40, 80]], [[-100, 200], [-200, 100]]]
energys = ["1500", "5000", "7000", "15000"]

for i in range(4):
    energy = energys[i]
    sm = np.loadtxt('../datas/SMTest-{}.csv'.format(energy), delimiter=',')
    ft0 = np.loadtxt('../datas/FgT0-{}.csv'.format(energy), delimiter=',')
    totalsm = len(sm)
    totalft0 = len(ft0)
    ae = load_model("../networks/encoder{}-{}-{}.h5".format(2, energy, num_epoch))
    smres = np.transpose(ae.predict(sm))
    ft0res = np.transpose(ae.predict(ft0))
    hsm, _, _ = np.histogram2d(smres[0], smres[1], bins=50, range=rangessm[i])
    hft0, _, _ = np.histogram2d(ft0res[0], ft0res[1], bins=50, range=rangesft0[i])
    np.savetxt("../results/letentsm{}-{}-{}.csv".format(2, energy, num_epoch), smres, delimiter=',')
    np.savetxt("../results/letenthsm{}-{}-{}.csv".format(2, energy, num_epoch), hsm, delimiter=',')
    np.savetxt("../results/letentft0{}-{}-{}.csv".format(2, energy, num_epoch), ft0res, delimiter=',')
    np.savetxt("../results/letenthft0{}-{}-{}.csv".format(2, energy, num_epoch), hft0, delimiter=',')
