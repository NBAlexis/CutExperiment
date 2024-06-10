import os

import numpy as np
import matplotlib.pyplot as plt

from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

VALIDATIONCOUNT = 30000

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

res = np.loadtxt("wf1/validation-30000-16384-l5.csv", delimiter=',')
s1 = res[0:VALIDATIONCOUNT]
s2 = res[VALIDATIONCOUNT:VALIDATIONCOUNT * 2]
s3 = res[VALIDATIONCOUNT * 2:VALIDATIONCOUNT * 3]
s4 = res[VALIDATIONCOUNT * 3:VALIDATIONCOUNT * 4]

l1 = s1[:, 1:4]
l1 = np.sqrt(np.sum(l1 * l1, axis=1))
l2 = s2[:, 1:4]
l2 = np.sqrt(np.sum(l2 * l2, axis=1))
l3 = s3[:, 1:4]
l3 = np.sqrt(np.sum(l3 * l3, axis=1))
l4 = s4[:, 1:4]
l4 = np.sqrt(np.sum(l4 * l4, axis=1))

plt.hist(l1, bins=50, range=[0, 1], histtype="step")
plt.hist(l2, bins=50, range=[0, 1], histtype="step")
plt.hist(l3, bins=50, range=[0, 1], histtype="step")
plt.hist(l4, bins=50, range=[0, 1], histtype="step")
plt.show()

plt.hist(s1[:, 0], bins=50, range=[0, 1], histtype="step")
plt.hist(s2[:, 0], bins=50, range=[0, 1], histtype="step")
plt.hist(s3[:, 0], bins=50, range=[0, 1], histtype="step")
plt.hist(s4[:, 0], bins=50, range=[0, 1], histtype="step")
plt.show()

"""
plt.hist(s1[:, 1], bins=50, range=[0, 1], histtype="step")
plt.hist(s2[:, 1], bins=50, range=[0, 1], histtype="step")
plt.hist(s3[:, 1], bins=50, range=[0, 1], histtype="step")
plt.hist(s4[:, 1], bins=50, range=[0, 1], histtype="step")
plt.show()

plt.hist(s1[:, 2], bins=50, range=[0, 1], histtype="step")
plt.hist(s2[:, 2], bins=50, range=[0, 1], histtype="step")
plt.hist(s3[:, 2], bins=50, range=[0, 1], histtype="step")
plt.hist(s4[:, 2], bins=50, range=[0, 1], histtype="step")
plt.show()

plt.hist(s1[:, 3], bins=50, range=[0, 1], histtype="step")
plt.hist(s2[:, 3], bins=50, range=[0, 1], histtype="step")
plt.hist(s3[:, 3], bins=50, range=[0, 1], histtype="step")
plt.hist(s4[:, 3], bins=50, range=[0, 1], histtype="step")
plt.show()
"""