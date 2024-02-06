import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/gqgc/")

smscore = np.loadtxt("res/gqgcsm1500.csv")
ft0score = np.loadtxt("res/gqgcft01500.csv")
# ft1score = np.loadtxt("res/gqgcft11500.csv")
# ft2score = np.loadtxt("res/gqgcft21500.csv")
# ft3score = np.loadtxt("res/gqgcft31500.csv")

plt.hist(smscore, bins=50)
plt.show()

plt.hist(ft0score, bins=50)
plt.show()

"""
plt.hist(ft1score, bins=50)
plt.show()

plt.hist(ft2score, bins=50)
plt.show()

plt.hist(ft3score, bins=50)
plt.show()
"""