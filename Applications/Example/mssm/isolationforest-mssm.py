import numpy as np
from matplotlib import pyplot as plt

from Applications.IsolationForest.IsolationTree4 import Split


"""
These are events of p p > tau tau~
Run datapreparation-mssm.py first to generate sm-mssm.csv and np-mssm.csv
"""
smData = np.loadtxt("sm-mssm.csv", delimiter=',')
npData = np.loadtxt("np-mssm.csv", delimiter=',')

"""
The cross-section is 836.38 pb for SM and 0.02614 pb for NP
so when we have 10000 SM events, we can use Nsm:Nnp = 10000:0.32
to use isolation forest, we need much more SM events.
We use Nsm:Nnp = 10000:32 just for test
"""
combinedList = np.hstack((np.vstack((smData[0:10000], npData[0:32])), np.zeros((10032, 2))))

"""
Build 100 isolation forest trees, and find the average depth of the leaves
"""
averageDepth = np.zeros(10032)

averageDepthOfFirstPoint = 0
averageDepthOfLastPoint = 0
averageDepthListSM = []
averageDepthListNP = []
for i in range(100):
    resSet = Split(combinedList, 8, -1)
    averageDepth = averageDepth + resSet[:, 9]
    averageDepthOfFirstPoint = averageDepthOfFirstPoint + resSet[0, 9]
    averageDepthOfLastPoint = averageDepthOfLastPoint + resSet[10031, 9]
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
for i in range(10031):
    harmonicNumber = harmonicNumber + (1.0 / (i + 1))

cn = 2*harmonicNumber - 2.0*10031/10032
anomalyScore = np.power(2, -averageDepth / cn)

"""
Depict the anomaly score distribution for SM and NP
"""
fig, ax = plt.subplots()
ax.hist(anomalyScore[0:10000], label="SM", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
ax.hist(anomalyScore[10000:10032], label="NP", histtype="step", range=[min(anomalyScore), max(anomalyScore)], bins=10, density=True)
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
