import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/aqgc/ansatz/")

smscore1 = np.loadtxt("validationsm-1500-l8.csv", delimiter=',')
ft0score1 = np.loadtxt("validationft0-1500-l8.csv", delimiter=',')
smscore2 = np.loadtxt("validationsm-1500-ae-128half.csv", delimiter=',')
ft0score2 = np.loadtxt("validationft0-1500-ae-128half.csv", delimiter=',')
smscore3 = np.loadtxt("validationsm-1500-l5.csv", delimiter=',')
ft0score3 = np.loadtxt("validationft0-1500-l5.csv", delimiter=',')
smscore4 = np.loadtxt("validationsm-1500-l6.csv", delimiter=',')
ft0score4 = np.loadtxt("validationft0-1500-l6.csv", delimiter=',')

def rate(sm, ft0, scorev):
    smcount = len(sm[sm > scorev])
    ft0count = len(ft0[ft0 > scorev])
    return smcount / ft0count

contrate1 = []
contrate2 = []
contrate3 = []
contrate4 = []
for score in range(200, 500):
    contrate1.append(rate(smscore1, ft0score1, score))
    contrate2.append(rate(smscore2, ft0score2, score))
    contrate3.append(rate(smscore3, ft0score3, score))
    contrate4.append(rate(smscore4, ft0score4, score))

plt.plot(contrate1, color='red')
plt.plot(contrate2, color='blue')
plt.plot(contrate3, color='green')
plt.plot(contrate4, color='black')
plt.show()