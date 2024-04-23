import numpy as np

from Applications.IsolationForest.IsolationTree4 import Split

smevents = np.loadtxt("../../../_DataFolder/jjvv/csv/Features/SM-1500.csv", delimiter=',')
npevents = np.loadtxt("../../../_DataFolder/jjvv/csv/Features/FgT0-1500.csv", delimiter=',')

smevents = smevents[0:5000, :]
npevents = npevents[0:50, :]

smevents = np.hstack((smevents, np.zeros((5000, 1))))
npevents = np.hstack((npevents, np.ones((50, 1))))

combined = np.vstack((smevents, npevents))
combined = np.hstack((combined, np.zeros((5050, 1))))

resSet = Split(combined, 8, -1)

print(resSet[:, 9])
