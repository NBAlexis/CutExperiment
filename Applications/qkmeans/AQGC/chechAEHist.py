import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/aqgc/ansatz/")

ressm = np.loadtxt("validationsm-1500-l50.csv", delimiter=',')
resft0 = np.loadtxt("validationft0-1500-l50.csv", delimiter=',')

plt.hist(ressm, bins=20)
plt.show()

plt.hist(resft0, bins=20)
plt.show()