import os

import numpy as np
from sklearn import svm

os.chdir("../../_DataFolder/SVM/E1500T0")

kernelres = np.loadtxt('quantumrestrainig.csv', delimiter=',')

def my_kernel(X, Y):
    return kernelres


trainingset = np.loadtxt('training.csv', delimiter=',')
y = np.vstack((-np.ones((500, 1)), np.ones((500, 1))))
clf = svm.SVC(kernel=my_kernel)
clf.fit(trainingset, y)

print("dual coef")
print(clf.dual_coef_)
print(clf.intercept_)
aysave = np.array(clf.dual_coef_)[0].tolist()
aysave.append(clf.intercept_[0])
np.savetxt("ay.csv", np.array(aysave), delimiter=',')

print("number of support vector = ", len(clf.support_))
print(clf.support_)
np.savetxt("sv.csv", trainingset[clf.support_], delimiter=',')
