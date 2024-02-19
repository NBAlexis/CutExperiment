import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/gqgc/")

smscore1 = np.loadtxt("res/gqgcsm1500l1.csv")
ft0score1 = np.loadtxt("res/gqgcft01500l1.csv")
smscore2 = np.loadtxt("res/gqgcsm1500l2.csv")
ft0score2 = np.loadtxt("res/gqgcft01500l2.csv")
smscore3 = np.loadtxt("res/gqgcsm1500l3.csv")
ft0score3 = np.loadtxt("res/gqgcft01500l3.csv")
smscore4 = np.loadtxt("res/gqgcsm1500l4.csv")
ft0score4 = np.loadtxt("res/gqgcft01500l4.csv")

def rate(sm, ft0, scorev):
    smcount = len(sm[sm > score])
    ft0count = len(ft0[ft0 > score])
    return smcount / ft0count

contrate1 = []
contrate2 = []
contrate3 = []
contrate4 = []
for score in range(100, 800):
    contrate1.append(rate(smscore1, ft0score1, score))
    contrate2.append(rate(smscore2, ft0score2, score))
    contrate3.append(rate(smscore3, ft0score3, score))
    contrate4.append(rate(smscore4, ft0score4, score))

# plt.plot(contrate1, color='red')
plt.plot(contrate2, color='blue')
plt.plot(contrate3, color='green')
plt.plot(contrate4, color='black')
plt.show()