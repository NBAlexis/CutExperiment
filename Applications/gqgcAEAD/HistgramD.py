import numpy as np
# from matplotlib import pyplot as plt

batch_size = 1024
num_epoch = 5000
lenmaxd = [50, 200, 300, 1000]
energies = ["1500", "5000", "7000", "15000"]

for latent in [1]:
    for i in range(4):
        sm = np.loadtxt("../results/dsm-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft0 = np.loadtxt("../results/dft0-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft1 = np.loadtxt("../results/dft1-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft2 = np.loadtxt("../results/dft2-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        ft3 = np.loadtxt("../results/dft3-{}-{}-{}.csv".format(latent, energies[i], num_epoch), delimiter=',')
        """
        plt.hist(sm, bins=50, range=[0, lenmaxd[i]])
        plt.show()
        plt.hist(ft0, bins=50, range=[0, lenmaxd[i]])
        plt.show()
        plt.hist(ft1, bins=50, range=[0, lenmaxd[i]])
        plt.show()
        plt.hist(ft2, bins=50, range=[0, lenmaxd[i]])
        plt.show()
        plt.hist(ft3, bins=50, range=[0, lenmaxd[i]])
        plt.show()
        """
        # """
        totalsm = len(sm)
        totalft0 = len(ft0)
        totalft1 = len(ft1)
        totalft2 = len(ft2)
        totalft3 = len(ft3)
        hsmres = np.histogram(sm, bins=50, range=[0, lenmaxd[i]])
        hsm = np.append(hsmres[0], hsmres[0][49]) / totalsm
        hft0res = np.histogram(ft0, bins=50, range=[0, lenmaxd[i]])
        hft0 = np.append(hft0res[0], hft0res[0][49]) / totalft0
        hft1res = np.histogram(ft1, bins=50, range=[0, lenmaxd[i]])
        hft1 = np.append(hft0res[0], hft0res[0][49]) / totalft1
        hft2res = np.histogram(ft2, bins=50, range=[0, lenmaxd[i]])
        hft2 = np.append(hft0res[0], hft0res[0][49]) / totalft2
        hft3res = np.histogram(ft3, bins=50, range=[0, lenmaxd[i]])
        hft3 = np.append(hft0res[0], hft0res[0][49]) / totalft3
        np.savetxt("../results/hist{}-{}-{}.csv".format(latent, energies[i], num_epoch), np.array([hsm, hft0, hft1, hft2, hft3]), delimiter=',')
        # """


