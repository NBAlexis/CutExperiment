import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

meantrain = [6.78584320e+02, 2.31165051e+02, 2.63492076e+02, 1.16571357e+02, 4.52016673e+02, 3.27568690e+02, 4.38689274e+02, 3.20442652e+02, 5.21396200e+01, 3.96600435e+01, 4.72441508e+02, 5.59036255e-01, 5.64498901e-01, 0.00000000e+00, 0.00000000e+00]
meantrain = np.array(meantrain)
stdtrain = [5.13638574e+02, 2.31957130e+02, 2.35013341e+02, 1.30111931e+02, 5.35387859e+02, 4.11400423e+02, 5.32438056e+02, 4.14060661e+02, 2.65500602e+02, 2.07677155e+02, 3.45580664e+02, 4.96502488e-01, 4.95822440e-01, 1.00000000e-18, 1.00000000e-18]
stdtrain = np.array(stdtrain)

testpointset = None
for i in range(11):
    ld = np.loadtxt("fullcsv/ft0-{}.csv".format(i), delimiter=',')
    if testpointset is None:
        testpointset = ld
    else:
        testpointset = np.vstack((testpointset, ld))

for i in range(11):
    testpointset = np.vstack((testpointset, np.loadtxt("fullcsv/jjll-{}.csv".format(i), delimiter=',')))

for i in range(11):
    testpointset = np.vstack((testpointset, np.loadtxt("fullcsv/ajll-{}.csv".format(i), delimiter=',')))

print(np.shape(testpointset))

testpointset = (testpointset - meantrain) / stdtrain
np.savetxt("wfv9/testv9-16384se.csv", testpointset, delimiter=',')
testpointset = np.hstack((testpointset, np.ones((len(testpointset), 1))))
testsetnorm = np.sqrt(np.sum(testpointset * testpointset, axis=1))
testpointset = np.transpose(np.transpose(testpointset) / testsetnorm)

print(np.shape(testpointset))
np.savetxt("wfv9/testv9-16384.csv", testpointset, delimiter=',')

"""
[6.78584320e+02 2.31165051e+02 2.63492076e+02 1.16571357e+02
 4.52016673e+02 3.27568690e+02 4.38689274e+02 3.20442652e+02
 5.21396200e+01 3.96600435e+01 4.72441508e+02 5.59036255e-01
 5.64498901e-01 0.00000000e+00 0.00000000e+00]
[5.13638574e+02 2.31957130e+02 2.35013341e+02 1.30111931e+02
 5.35387859e+02 4.11400423e+02 5.32438056e+02 4.14060661e+02
 2.65500602e+02 2.07677155e+02 3.45580664e+02 4.96502488e-01
 4.95822440e-01 1.00000000e-18 1.00000000e-18]
 
ft0:
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
[13722, 13385, 12787, 12524, 12501, 12069, 12170, 12538, 12902, 13429, 14171]


jjll
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
[26980, 26327, 25420, 24889, 24362, 24673, 25165, 25176, 25572, 26241, 27357]


ajjvv
[89787, 100000, 100000, 100000, 100000, 100000, 100000, 37846, 100000, 100000, 100000]
[2685, 2587, 2289, 2131, 1925, 1786, 1914, 828, 2219, 2581, 3067]

"""