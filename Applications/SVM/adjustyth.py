import os
import numpy as np

import matplotlib.pyplot as plt

os.chdir("../../_DataFolder/SVM/E1500T0")

yth = 0.1
counts = []

for i in range(0, 21):
    yi = np.loadtxt('testyift0-{}.csv'.format(i), delimiter=',')
    counts.append(len(yi[yi > yth]))

counts = np.array(counts)
print(counts)
plt.plot(counts / 300000)
plt.show()
