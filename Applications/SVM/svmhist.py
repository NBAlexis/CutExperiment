import os

import numpy as np
import matplotlib.pyplot as plt

os.chdir("../../_DataFolder/SVM/E1500T0")

validationres = np.loadtxt('quantumresvalidation.csv', delimiter=',')
ayres = np.loadtxt('ay.csv', delimiter=',')

print(np.shape(validationres))
print(np.shape(ayres))

b = ayres[len(ayres) - 1]
ayarray = np.array([ayres[0:len(ayres) - 1]])

ayk = np.dot(ayarray, validationres)
print(np.shape(ayk))
ayk = ayk.flatten()
ayk = ayk + b

result = np.histogram(ayk[0:1000], range=[-13, 13], bins=52)
distributions = result[0]/1000
distributions = np.hstack((np.array([distributions[0]]), distributions))
bins = result[1]

result2 = np.histogram(ayk[1000:2000], range=[-13, 13], bins=52)
distributions2 = result2[0]/1000
distributions2 = np.hstack((np.array([distributions2[0]]), distributions2))
bins2 = result2[1]

fig, ax = plt.subplots()
ax.step(bins, distributions, label="SM")
ax.step(bins2, distributions2, label="$O_{T_0}$")
ax.set_xlabel('$y_i$', fontsize=15)
ax.set_ylabel('$1/N dN/0.05$', fontsize=15)
ax.legend()
plt.xlim((-13, 13))
plt.show()