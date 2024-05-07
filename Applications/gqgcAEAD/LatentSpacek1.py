import numpy as np
from keras.models import load_model

batch_size = 1024
adamlr = 0.002
num_epoch = 5000
ranges = [[-5, 5], [-20, 20], [-20, 10], [-100, 50]]
energys = ["1500", "5000", "7000", "15000"]

for i in range(4):
    energy = energys[i]
    sm = np.loadtxt('../datas/SMTest-{}.csv'.format(energy), delimiter=',')
    ft0 = np.loadtxt('../datas/FgT0-{}.csv'.format(energy), delimiter=',')
    ft1 = np.loadtxt('../datas/FgT1-{}.csv'.format(energy), delimiter=',')
    ft2 = np.loadtxt('../datas/FgT2-{}.csv'.format(energy), delimiter=',')
    ft3 = np.loadtxt('../datas/FgT3-{}.csv'.format(energy), delimiter=',')
    totalsm = len(sm)
    totalft0 = len(ft0)
    totalft1 = len(ft1)
    totalft2 = len(ft2)
    totalft3 = len(ft3)
    ae = load_model("../networks/encoder{}-{}-{}.h5".format(1, energy, num_epoch))
    smres = ae.predict(sm).flatten()
    ft0res = ae.predict(ft0).flatten()
    ft1res = ae.predict(ft1).flatten()
    ft2res = ae.predict(ft2).flatten()
    ft3res = ae.predict(ft3).flatten()
    hsmres = np.histogram(smres, bins=50, range=ranges[i])
    hsm = np.append(hsmres[0], hsmres[0][49]) / totalsm
    hft0res = np.histogram(ft0res, bins=50, range=ranges[i])
    hft0 = np.append(hft0res[0], hft0res[0][49]) / totalft0
    hft1res = np.histogram(ft1res, bins=50, range=ranges[i])
    hft1 = np.append(hft1res[0], hft1res[0][49]) / totalft1
    hft2res = np.histogram(ft2res, bins=50, range=ranges[i])
    hft2 = np.append(hft2res[0], hft2res[0][49]) / totalft2
    hft3res = np.histogram(ft3res, bins=50, range=ranges[i])
    hft3 = np.append(hft3res[0], hft3res[0][49]) / totalft3
    np.savetxt("../results/letent{}-{}-{}.csv".format(1, energy, num_epoch), np.array([hsm, hft0, hft1, hft2, hft3]), delimiter=',')
