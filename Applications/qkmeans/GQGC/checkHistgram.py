import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/gqgc/")

allscore = np.loadtxt("res/gqgctest1500-Comb-2048-l30.csv")
smscore = allscore[0:100000]
ft0score = allscore[100000:200000]

print(len(smscore))
print(np.histogram(smscore, bins=50, range=[0, 1000]))

print(len(ft0score))
print(np.histogram(ft0score, bins=50, range=[0, 1000]))

"""
print(len(ft1score))
print(np.histogram(ft1score, bins=50, range=[0, 1000]))

print(len(ft2score))
print(np.histogram(ft2score, bins=50, range=[0, 1000]))

print(len(ft3score))
print(np.histogram(ft3score, bins=50, range=[0, 1000]))

plt.hist(ft1score, bins=50)
plt.show()

plt.hist(ft2score, bins=50)
plt.show()

plt.hist(ft3score, bins=50)
plt.show()
"""