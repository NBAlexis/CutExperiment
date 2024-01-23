import os

import numpy as np
import matplotlib.pyplot as plt

os.chdir("../../_DataFolder/SVM/E1500T0")

wb = np.loadtxt('wb.csv', delimiter=',')
w = wb[0:16]
w = np.reshape(w, (16, 1))
b = wb[16]

for i in range(0, 21):
    testset = np.loadtxt('testft0-{}.csv'.format(i), delimiter=',')
    ayk = np.dot(testset, np.conjugate(w))
    ayk = ayk.flatten()
    ayk = ayk + b
    np.savetxt('testyift0-{}.csv'.format(i), ayk, delimiter=',')
    print('testyift0-{}.csv saved'.format(i))

