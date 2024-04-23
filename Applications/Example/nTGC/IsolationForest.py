import numpy as np
from matplotlib import pyplot as plt

from Applications.IsolationForest.IsolationTree4 import Split


"""
These are events of p p > j j a
Run datapreparation.py first to generate sm.csv and np.csv
"""
smData = np.loadtxt("sm.csv", delimiter=',')
npData = np.loadtxt("np.csv", delimiter=',')

"""
The cross-section is 8.4e4 pb for SM and 2.8e-3 pb for NP
so, after number cuts, the cross-section is 3.0e4pb for SM and 2.1e-3pb for NP

assume the coefficient for nTGC is 300TeV-4, then it was
3.0e4pb for SM and 1.9e2pb for NP

so the number of events are 3500:22, when L=0.116pb-1, assume the luminosity is .116pb-1, we pick 3500 events from SM and 22 events from NP
"""
combinedList = np.hstack((np.vstack((smData[0:3500], npData[0:22])), np.zeros((3522, 2))))

"""
Build 100 isolation forest trees, and find the average depth of the leaves
"""
averageDepth = np.zeros(3522)

averageDepthOfFirstPoint = 0
averageDepthOfLastPoint = 0
averageDepthListSM = []
averageDepthListNP = []
for i in range(100):
    resSet = Split(combinedList, 12, -1)
    averageDepth = averageDepth + resSet[:, 13]
    averageDepthOfFirstPoint = averageDepthOfFirstPoint + resSet[0, 13]
    averageDepthOfLastPoint = averageDepthOfLastPoint + resSet[3521, 13]
    averageDepthListSM.append(averageDepthOfFirstPoint / (i + 1))
    averageDepthListNP.append(averageDepthOfLastPoint / (i + 1))
averageDepth = averageDepth / 100

"""
Normalize it to anomaly score:
2^{-L/c}
where L is average depth
c(N) = 2H(N-1) - 2(N-1)/N
where H(n) is harmonic number
"""
harmonicNumber = 0
for i in range(3521):
    harmonicNumber = harmonicNumber + (1.0 / (i + 1))

cn = 2*harmonicNumber - 2.0*3521/3522
anomalyScore = np.power(2, -averageDepth / cn)

"""
Depict the anomaly score distribution for SM and NP
"""
fig, ax = plt.subplots()
ax.hist(anomalyScore[0:3500], label="SM", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
ax.hist(anomalyScore[3500:3522], label="NP", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
ax.legend()
ax.set_xlabel('a', fontsize=20)
ax.set_ylabel('1/N dN/{0:.3f}'.format((max(anomalyScore) - min(anomalyScore)) / 10), fontsize=20)
plt.show()

fig, ax = plt.subplots()
ax.plot(averageDepthListSM, label="SM")
ax.plot(averageDepthListNP, label="NP")
ax.legend()
ax.set_xlabel('number of trees', fontsize=20)
ax.set_ylabel('average depth', fontsize=20)
plt.show()
