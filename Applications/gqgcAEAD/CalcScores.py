import numpy as np
from keras.models import load_model

num_epoch = 500

for latent in [1, 2, 3, 4]:
    for energy in ["1500", "5000", "7000", "15000"]:
        sm = np.loadtxt('../datas/SMTest-{}.csv'.format(energy), delimiter=',')
        ft0 = np.loadtxt('../datas/FgT0-{}.csv'.format(energy), delimiter=',')
        ft1 = np.loadtxt('../datas/FgT1-{}.csv'.format(energy), delimiter=',')
        ft2 = np.loadtxt('../datas/FgT2-{}.csv'.format(energy), delimiter=',')
        ft3 = np.loadtxt('../datas/FgT3-{}.csv'.format(energy), delimiter=',')
        ae = load_model("../networks/b64lr001ae{}-{}-{}.h5".format(latent, energy, num_epoch))
        smres = ae.predict(sm) - sm
        ft0res = ae.predict(ft0) - ft0
        ft1res = ae.predict(ft1) - ft1
        ft2res = ae.predict(ft2) - ft2
        ft3res = ae.predict(ft3) - ft3
        dsm = np.mean(np.power(smres, 2), axis=1)
        dft0 = np.mean(np.power(ft0res, 2), axis=1)
        dft1 = np.mean(np.power(ft1res, 2), axis=1)
        dft2 = np.mean(np.power(ft2res, 2), axis=1)
        dft3 = np.mean(np.power(ft3res, 2), axis=1)
        np.savetxt("../results/b64lr001dsm-{}-{}-{}.csv".format(latent, energy, num_epoch), dsm, delimiter=',')
        np.savetxt("../results/b64lr001dft0-{}-{}-{}.csv".format(latent, energy, num_epoch), dft0, delimiter=',')
        np.savetxt("../results/b64lr001dft1-{}-{}-{}.csv".format(latent, energy, num_epoch), dft1, delimiter=',')
        np.savetxt("../results/b64lr001dft2-{}-{}-{}.csv".format(latent, energy, num_epoch), dft2, delimiter=',')
        np.savetxt("../results/b64lr001dft3-{}-{}-{}.csv".format(latent, energy, num_epoch), dft3, delimiter=',')
