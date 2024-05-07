import numpy as np

num_epoch = 500
lenmaxd = [61, 201, 301, 1001]
energies = ["1500", "5000", "7000", "15000"]

for latent in [1, 2, 3, 4]:
    for i in range(4):
        sm = np.loadtxt("../results/b64lr001dsm-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft0 = np.loadtxt("../results/b64lr001dft0-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft1 = np.loadtxt("../results/b64lr001dft1-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft2 = np.loadtxt("../results/b64lr001dft2-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft3 = np.loadtxt("../results/b64lr001dft3-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        dth = []
        csm = []
        cft0 = []
        cft1 = []
        cft2 = []
        cft3 = []
        totalsm = len(sm)
        totalft0 = len(ft0)
        totalft1 = len(ft1)
        totalft2 = len(ft2)
        totalft3 = len(ft3)
        for k in range(lenmaxd[i]):
            csm.append(len(sm[sm > k + 1]) / totalsm)
            cft0.append(len(ft0[ft0 > k + 1]) / totalft0)
            cft1.append(len(ft1[ft1 > k + 1]) / totalft1)
            cft2.append(len(ft2[ft2 > k + 1]) / totalft2)
            cft3.append(len(ft3[ft3 > k + 1]) / totalft3)
        np.savetxt("../results/b64lr001eff{}-{}-{}.csv".format(latent, energies[i], num_epoch), np.transpose(np.array([csm, cft0, cft1, cft2, cft3])), delimiter=',')
