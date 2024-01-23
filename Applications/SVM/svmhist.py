import os

import numpy as np
import matplotlib.pyplot as plt

os.chdir("../../_DataFolder/SVM/E1500T0")

wb = np.loadtxt('wb.csv', delimiter=',')
w = wb[0:16]
w = np.reshape(w, (16, 1))
b = wb[16]
validationset = np.loadtxt('validation.csv', delimiter=',')

ayk = np.dot(validationset, np.conjugate(w))
print(np.shape(ayk))
ayk = ayk.flatten()
ayk = ayk + b

# """
result = np.histogram(ayk[0:100000], range=[-1, 1], bins=52)
distributions = result[0]/100000
distributions = np.hstack((np.array([distributions[0]]), distributions))
bins = result[1]

result2 = np.histogram(ayk[100000:200000], range=[-1, 1], bins=52)
distributions2 = result2[0]/100000
distributions2 = np.hstack((np.array([distributions2[0]]), distributions2))
bins2 = result2[1]

fig, ax = plt.subplots()
ax.step(bins, distributions, label="SM")
ax.step(bins2, distributions2, label="$O_{T_0}$")
ax.set_xlabel('$y_i$', fontsize=15)
ax.set_ylabel('$1/N dN/0.05$', fontsize=15)
ax.legend()
plt.xlim((-1, 1))
plt.show()
# """