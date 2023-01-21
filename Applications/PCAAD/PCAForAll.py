import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from Applications.PCAAD.pcaadfunctions import PCAOnce

dimension = 9
outdim = 9
iteration = 1

for i in range(0, 21):
    data = np.loadtxt("../../_DataFolder/PCAAD/cs/FT0-15000-{0}.csv".format(i), delimiter=',')
    [data, ratio] = PCAOnce(data, dimension, outdim, True)
    plt.bar([i for i in range(0, outdim)], ratio)
    plt.show()
    plt.hist(data[:, 0], 50)
    plt.show()
    np.savetxt("../../_DataFolder/PCAAD/pca/FT0-15000-{0}.csv".format(i), data, "%f", delimiter=',')
