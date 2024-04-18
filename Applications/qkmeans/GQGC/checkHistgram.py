import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/gqgc/")

smscore = np.loadtxt("res/gqgcsm5000l2.csv")
ft0score = np.loadtxt("res/gqgcft05000l2.csv")
ft1score = np.loadtxt("res/gqgcft15000l2.csv")
ft2score = np.loadtxt("res/gqgcft25000l2.csv")
ft3score = np.loadtxt("res/gqgcft35000l2.csv")

# plt.hist(smscore, bins=50)
# plt.show()

# plt.hist(ft0score, bins=50)
# plt.show()
print(len(smscore))
print(np.histogram(smscore, bins=50, range=[0, 1000]))

print(len(ft0score))
print(np.histogram(ft0score, bins=50, range=[0, 1000]))

print(len(ft1score))
print(np.histogram(ft1score, bins=50, range=[0, 1000]))

print(len(ft2score))
print(np.histogram(ft2score, bins=50, range=[0, 1000]))

print(len(ft3score))
print(np.histogram(ft3score, bins=50, range=[0, 1000]))
"""
plt.hist(ft1score, bins=50)
plt.show()

plt.hist(ft2score, bins=50)
plt.show()

plt.hist(ft3score, bins=50)
plt.show()
"""