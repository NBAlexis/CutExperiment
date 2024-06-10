import os

import numpy as np

from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

TRAININGCOUNT = 16384
VALIDATIONCOUNT = 30000


os.chdir("../../../_DataFolder/qkmeans/jllvv/")

s1 = np.loadtxt("featurecsv/ft0.csv", delimiter=',')
s2 = np.loadtxt("featurecsv/sm.csv", delimiter=',')
s3 = np.loadtxt("featurecsv/jjll.csv", delimiter=',')
s4 = np.loadtxt("featurecsv/tt.csv", delimiter=',')
np.random.shuffle(s1)
np.random.shuffle(s2)
np.random.shuffle(s3)
np.random.shuffle(s4)

traingset = np.vstack((s1[0:TRAININGCOUNT], s2[0:TRAININGCOUNT], s3[0:TRAININGCOUNT], s4[0:TRAININGCOUNT]))
traingsetmean = np.mean(traingset, axis=0)
traingsetstd = np.std(traingset, axis=0)

traingset = (traingset - traingsetmean) / traingsetstd
traingset = np.hstack((traingset, np.ones((4 * TRAININGCOUNT, 1))))
traingsetnorm = np.sqrt(np.sum(traingset * traingset, axis=1))
traingset = np.transpose(np.transpose(traingset) / traingsetnorm)

validationset = np.vstack((s1[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s2[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s3[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s4[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT]))

validationset = (validationset - traingsetmean) / traingsetstd
validationset = np.hstack((validationset, np.ones((4 * VALIDATIONCOUNT, 1))))
validationsetnorm = np.sqrt(np.sum(validationset * validationset, axis=1))
validationset = np.transpose(np.transpose(validationset) / validationsetnorm)

np.savetxt("wf1/train-{}.csv".format(TRAININGCOUNT), traingset, delimiter=',')
np.savetxt("wf1/validation-{}.csv".format(VALIDATIONCOUNT), validationset, delimiter=',')