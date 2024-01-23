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

# print("dual coef")
# print(clf.dual_coef_)
# print(clf.intercept_)

print("number of support vector = ", len(clf.support_))

sv = trainingset[clf.support_]
w = np.dot(clf.dual_coef_, sv).flatten()

lenw = np.sqrt(np.dot(w, w))
w = w / lenw
b = clf.intercept_ / lenw
print(w)
print(b)

np.savetxt("wb.csv", np.array(w.tolist() + b.tolist()), delimiter=',')
