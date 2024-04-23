
"""
These are events of p p > tau tau~ + invisible
Run datapreparation-mssm.py first to generate sm-mssm.csv and np-mssm.csv
"""
import numpy as np
from matplotlib import pyplot as plt

smData = np.loadtxt("sm-mssm.csv", delimiter=',')
npData = np.loadtxt("np-mssm.csv", delimiter=',')

"""
The PCA must be calculated after decenteralization
Z-score standardize first
"""
means = np.mean(smData, axis=0)
stds = np.std(smData, axis=0)
for i in range(0, len(smData[0])):
    smData[:, i] = (smData[:, i] - means[i]) / stds[i]
    npData[:, i] = (npData[:, i] - means[i]) / stds[i]

"""
Find the projection vectors for background 
"""
scatt = np.dot(np.transpose(smData), smData)
_, eig_vec = np.linalg.eig(scatt)
features = eig_vec[:, 0]

"""
Find the distances for background 
"""
smPrinciple = np.dot(smData, features)
smDistance = np.sqrt(np.sum(smData * smData, axis=1) - smPrinciple * smPrinciple)

"""
Find the distances for NP 
"""
npPrinciple = np.dot(npData, features)
npDistance = np.sqrt(np.sum(npData * npData, axis=1) - npPrinciple * npPrinciple)

"""
Show the histogram 
"""
fig, ax = plt.subplots()
minDistance = min([min(smDistance), min(npDistance)])
maxDistance = max([max(smDistance), max(npDistance)])
ax.hist(smDistance, label="SM", histtype="step", range=[minDistance, maxDistance], bins=20, density=True)
ax.hist(npDistance, label="NP", histtype="step", range=[minDistance, maxDistance], bins=20, density=True)
ax.legend()
ax.set_xlabel('d', fontsize=20)
ax.set_ylabel('1/N dN/{0:.3f}'.format((maxDistance - minDistance) / 20), fontsize=20)
plt.show()
