import os

import numpy as np

os.chdir("../../_DataFolder/SVM/E1500T0")

trainingcount = 500
validationcount = 1000
testcount = 1000

def normalizev(v):
    lens = np.sqrt(np.dot(v, v))
    return v / lens

"""
training
"""
smdata = np.loadtxt("sm.csv", delimiter=',')
ft0data = np.loadtxt("ft0.csv", delimiter=',')

trainingsetsm = smdata[0:500, :]
trainingsetft0 = ft0data[0:500, :]

trainingset = np.vstack((trainingsetsm, trainingsetft0))
mintraining = np.min(trainingset, axis=0)
maxtraining = np.max(trainingset, axis=0)
averagetraububg = np.mean(trainingset, axis=0)

# trainingset = trainingset - averagetraububg
# trainingset = 2 * trainingset / (maxtraining - mintraining)
# trainingset = np.hstack((trainingset, np.ones((1000, 1))))

# afternormalize = []
# for i in range(0, 1000):
#     afternormalize.append(normalizev(trainingset[i]))

# afternormalize = np.array(afternormalize)
# np.savetxt("training.csv", afternormalize, delimiter=',')



"""
validation

validationsetsm = smdata[500:1500, :]
validationsetft0 = ft0data[500:1500, :]

validationset = np.vstack((validationsetsm, validationsetft0))
validationset = validationset - averagetraububg
validationset = 2 * validationset / (maxtraining - mintraining)
validationset = np.hstack((validationset, np.ones((2000, 1))))

afternormalize = []
for i in range(0, 2000):
    afternormalize.append(normalizev(validationset[i]))

afternormalize = np.array(afternormalize)
np.savetxt("validation.csv", afternormalize, delimiter=',')
"""

"""
test
"""
for i in range(0, 11):
    testdata = np.loadtxt("ft0-{}.csv".format(i), delimiter=',')
    testset = testdata[0:1000, :]

    testset = testset - averagetraububg
    testset = 2 * testset / (maxtraining - mintraining)
    testset = np.hstack((testset, np.ones((1000, 1))))

    afternormalize = []
    for j in range(0, 1000):
        afternormalize.append(normalizev(testset[j]))

    afternormalize = np.array(afternormalize)
    np.savetxt("testft0-{}.csv".format(i), afternormalize, delimiter=',')
