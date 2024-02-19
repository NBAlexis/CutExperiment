import os

import numpy as np
import matplotlib.pyplot as plt

os.chdir("../../_DataFolder/SVM/E1500T0")

wb = np.loadtxt('wb.csv', delimiter=',')
w = wb[0:16]
w = np.reshape(w, (16, 1))
b = wb[16]
validationset = np.loadtxt('validation.csv', delimiter=',')
print(np.shape(validationset))
validationset = np.hstack((
    np.transpose(np.array([validationset[:, 0] + validationset[:, 1] * 1j])),
    np.transpose(np.array([validationset[:, 2] + validationset[:, 3] * 1j])),
    np.transpose(np.array([validationset[:, 4] + validationset[:, 5] * 1j])),
    np.transpose(np.array([validationset[:, 6] + validationset[:, 7] * 1j])),
    np.transpose(np.array([validationset[:, 8] + validationset[:, 9] * 1j])),
    np.transpose(np.array([validationset[:, 10] + validationset[:, 11] * 1j])),
    np.transpose(np.array([validationset[:, 12] + validationset[:, 13] * 1j])),
    np.transpose(np.array([validationset[:, 14] + validationset[:, 15] * 1j]))
))
print(np.shape(validationset))
w = np.array([
    w[0, :] + w[1, :] * 1j,
    w[2, :] + w[3, :] * 1j,
    w[4, :] + w[5, :] * 1j,
    w[6, :] + w[7, :] * 1j,
    w[8, :] + w[9, :] * 1j,
    w[10, :] + w[11, :] * 1j,
    w[12, :] + w[13, :] * 1j,
    w[14, :] + w[15, :] * 1j
])

ayk = np.abs(np.dot(validationset, np.conjugate(w)))
print(np.shape(ayk))
ayk = ayk.flatten()
ayk = ayk + b

# """
result = np.histogram(ayk[0:100000], range=[-1, 1], bins=52)
distributions = result[0] / 100000
distributions = np.hstack((np.array([distributions[0]]), distributions))
bins = result[1]

result2 = np.histogram(ayk[100000:200000], range=[-1, 1], bins=52)
distributions2 = result2[0] / 100000
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
