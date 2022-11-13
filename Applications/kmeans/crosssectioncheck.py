import os
import numpy as np

#################################################################
from matplotlib import pyplot as plt

k = 50
energy = "15000"
readfileName = "FT0"
cutdist = 9000
#################################################################

os.chdir("../../")
dim = 12
eventnumber = []

for n in range(0, 11):
    dist = np.loadtxt("_DataFolder/kmeans/distances/E{0}/{1}/{1}-{0}-{2}-{3}-meandist.csv".format(energy, readfileName, k, n), delimiter=',')
    eventnumber.append(len(dist[dist > cutdist]))

print(eventnumber)
plt.plot(eventnumber)
plt.show()


