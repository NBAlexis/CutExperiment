import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir("../../../_DataFolder/qkmeans/gqgc/")

allscore = np.loadtxt("res/gqgctest1500-Comb-16384-ad-25000-150.csv")
smscore = allscore[0:100000]
ft0score = allscore[100000:200000]
ft1score = allscore[200000:300000]
ft2score = allscore[300000:400000]
ft3score = allscore[400000:500000]

scorecut = 375
print([len(smscore[smscore > scorecut]), len(ft0score[ft0score > scorecut]), len(ft1score[ft1score > scorecut]), len(ft2score[ft2score > scorecut]), len(ft3score[ft3score > scorecut])])
