import os

import numpy as np

from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

TRAININGCOUNT = 4096
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

traingset = (traingset - traingsetmean) / traingsetstd / 2

validationset = np.vstack((s1[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s2[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s3[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT],
                           s4[TRAININGCOUNT:TRAININGCOUNT + VALIDATIONCOUNT]))

validationset = (validationset - traingsetmean) / traingsetstd / 2

np.savetxt("wf1/train2-{}.csv".format(TRAININGCOUNT), traingset, delimiter=',')
np.savetxt("wf1/validation2-{}.csv".format(VALIDATIONCOUNT), validationset, delimiter=',')