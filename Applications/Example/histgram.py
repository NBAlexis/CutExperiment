import matplotlib.pyplot as plt
import numpy as np


lst = np.exp(-np.random.uniform(0, 1, 50000))

result = np.histogram(lst, range=[0.36, 1.0], bins=40)
distributions = result[0]/50000
distributions = np.hstack((np.array([distributions[0]]), distributions))
bins = result[1]

lst2 = np.log(1+2.0*np.random.uniform(0, 1, 50000))
result2 = np.histogram(lst2, range=[0.36, 1.0], bins=40)
distributions2 = result2[0]/50000
distributions2 = np.hstack((np.array([distributions2[0]]), distributions2))
bins2 = result2[1]

fig, ax = plt.subplots()
ax.step(bins, distributions, label="SM")
ax.step(bins2, distributions2, label="$O_{T_0}$")
ax.set_xlabel('$p_T\\;({\\rm GeV})$', fontsize=15)
ax.set_ylabel('$1/N dN/0.016\\;{\\rm GeV}$', fontsize=15)
ax.legend()
plt.xlim((0.36, 1))
plt.show()
plt.savefig("test.eps")
