import os

import numpy as np
from scipy.optimize import curve_fit

"""
based on v7 or v9
"""

thresh = 0.9

ft0 = [-0.2 + 0.04 * i for i in range(0, 11)]
# jllvv-all (ft0-all)
cstest1 = [1.152163, 1.150112, 1.148062, 1.147658, 1.147078, 1.146779, 1.14749, 1.148202, 1.148693, 1.150775, 1.152588]
cstest1 = np.array(cstest1) * 1000
# jjllvv-all
cstest2 = [0.6846642373968842, 0.6824569474439637, 0.6811922087311671, 0.6802828566259532, 0.6797656494744405,
           0.6792996460697598, 0.6800736018018549, 0.680606122905121, 0.6816499295578057, 0.6831803770023038,
           0.6856529196836619]
cstest2 = np.array(cstest2) * 1000
# ajjllvv-all
cstest3 = [0.01840014, 0.01817512, 0.01797186, 0.0178617, 0.01778247, 0.01771952, 0.0177596, 0.01781294, 0.01796576,
           0.01814595, 0.01838235]
cstest3 = np.array(cstest3) * 1000

testcounts1 = [13722, 13385, 12787, 12524, 12501, 12069, 12170, 12538, 12902, 13429, 14171]
testcounts2 = [26980, 26327, 25420, 24889, 24362, 24673, 25165, 25176, 25572, 26241, 27357]
testcounts3 = [2685, 2587, 2289, 2131, 1925, 1786, 1914, 828, 2219, 2581, 3067]

testcountsall1 = np.array(
    [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000])
testcountsall2 = np.array(
    [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000])
testcountsall3 = np.array([89787, 100000, 100000, 100000, 100000, 100000, 100000, 37846, 100000, 100000, 100000])

# validationcounts = [30000, 30000, 13472, 16245, 12272, 30000, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697] # v7
validationcounts = [30000, 30000, 13472, 16245, 12272, 8289, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697] # v9
ttnjcountall = [5100000, 1147221, 256974, 100000]
L = 140

tttowb = 888000 * 0.23 * 0.23 * 12.310718648686324 / 249.25127345975994
css = [70.33523769312358,  # ft0
       69.23430075477707,  # ggwwnp
       6.879493711020082,  # ajllvvnp

       14.014828715093419,  # SM
       tttowb * 20464 / 5100000,  # tt
       720.1 * 49787 / 2000000,  # jjllvv
       tttowb * 6543 / 1147221,  # ttj
       tttowb * 20071 / 2556974,  # ttjj
       tttowb * 887 / 100000,  # ttjjj

       7.2943596135588125,  # jll
       16.57523181827877,  # jjll
       17.130141879617266,  # jjjll
       10.392097581532946,  # jjjjll

       0.5735141233029315,  # jlllv
       0.21788534400341174,  # jlllvb

       6.28110723740789e-02,  # ajll
       0.23262742266023,  # ajjll
       0.3529662955632318  # ajllvv
       ]

includedtype = [
    1,  # ft0
    1,  # ggwwnp
    1,  # ajllvvnp

    0,  # SM
    2,  # tt

    0,  # jjllvv
    0,  # ttj
    0,  # ttjj
    0,  # ttjjj

    0,  # jll
    2,  # jjll
    2,  # jjjll
    2,  # jjjjll

    2,  # jlllv
    2,  # jlllvb

    2,  # ajll
    2,  # ajjll
    0  # ajllvv
]

trainset = ["ft0", "ggwwnp", "ajllvvnp", "sm",
            "tt", "jjllvv", "ttj", "ttjj",
            "ttjjj", "jll", "jjll", "jjjll",
            "jjjjll", "jlllv", "jlllvb", "ajll",
            "ajjll", "ajllvv"]

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

# testres = np.loadtxt("wfv7/test-16384-l15-5000-01.csv", delimiter=',')
# validationres = np.loadtxt("wfv7/validationv7-16384-l15-5000-01.csv", delimiter=',')
# testres = np.loadtxt("wfv9/testv9-16384-SCA-l15-5000-01.csv", delimiter=',')
# validationres = np.loadtxt("wfv9/validationv9-16384-SCA-l15-5000-01.csv", delimiter=',')
testres = np.loadtxt("wfv9/test-16384-classical-K1000-P.csv", delimiter=',')
validationres = np.loadtxt("wfv9/test-16384-classical-K1000-P.csv", delimiter=',')

testrest1 = []
testrest2 = []
testrest3 = []
nstart = 0
for c in testcounts1:
    s = testres[nstart:nstart + c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    testrest1.append(sAbove)
    nstart = nstart + c
for c in testcounts2:
    s = testres[nstart:nstart + c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    testrest2.append(sAbove)
    nstart = nstart + c
for c in testcounts3:
    s = testres[nstart:nstart + c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    testrest3.append(sAbove)
    nstart = nstart + c

testrest1 = np.array(testrest1)
testrest1 = cstest1 * testrest1 / testcountsall1
testrest2 = np.array(testrest2)
testrest2 = cstest2 * testrest2 / testcountsall2
testrest3 = np.array(testrest3)
testrest3 = cstest3 * testrest3 / testcountsall3

print(testrest1)
print(testrest2)
print(testrest3)

allcs = []
bgcs = 0
nstart = 0
for i in range(len(validationcounts)):
    c = validationcounts[i]
    s = validationres[nstart:nstart + c]
    sAbove = None
    if len(np.shape(s)) > 1:
        sAbove = len(s[s[:, 0] > thresh, 0])
    else:
        sAbove = len(s[s > thresh])
    cs = css[i] * sAbove / c
    allcs.append(cs)
    if 2 == includedtype[i]:
        bgcs = bgcs + cs
    nstart = nstart + c

print(trainset)
print(css)
print(allcs)
print("background")
print(bgcs)

testrest = testrest1 + testrest2 + testrest3 + bgcs


def csfunc(x, a, b, c):
    return a + b * x + c * x * x


popt, _ = curve_fit(csfunc, ft0, testrest)
csbg = popt[0]
cssint = popt[1]
csssq = popt[2]

ss = 2
left = (-cssint - np.sqrt(cssint ** 2 + (2 * csssq * (ss ** 2 + np.sqrt(4 * csbg * L * ss ** 2 + ss ** 4))) / L)) / (
            2 * csssq)
right = (-cssint + np.sqrt(cssint ** 2 + (2 * csssq * (ss ** 2 + np.sqrt(4 * csbg * L * ss ** 2 + ss ** 4))) / L)) / (
            2 * csssq)

print(left)
print(right)

print((1 / (-16 * left)) ** (0.25))
print((1 / (16 * right)) ** (0.25))

"""
v7: l10 0.85
[0.38251812 0.29212845 0.19172635 0.09181264 0.03326526 0.02408236
 0.05622701 0.07922594 0.18723696 0.24166275 0.49330766]
[0.29372096 0.23681256 0.13215129 0.06326631 0.04010617 0.02445479
 0.03740405 0.05649031 0.12269699 0.23364769 0.35448256]
[0.05840534 0.04089402 0.0280361  0.01286042 0.00462344 0.00212634
 0.00568307 0.01741475 0.02299617 0.04355028 0.06617646]
['ft0', 'ggwwnp', 'ajllvvnp', 'sm', 'tt', 'jjllvv', 'ttj', 'ttjj', 'ttjjj', 'jll', 'jjll', 'jjjll', 'jjjjll', 'jlllv', 'jlllvb', 'ajll', 'ajjll', 'ajllvv']
[70.33523769312357, 69.23430075477707, 6.879493711020082, 14.014828715093419, 9.309685480444585, 17.92580935, 13.232578834619499, 18.211988057378374, 20.579663901430397, 7.294359613558813, 16.57523181827877, 17.130141879617266, 10.392097581532946, 0.5735141233029315, 0.21788534400341175, 0.0628110723740789, 0.23262742266023, 0.3529662955632318]
[14.034224427701258, 13.202981153935987, 1.8541747078914725, 0.023293344124809007, 0.002275835759561095, 0.02091344424166667, 0.0, 0.004536891051113142, 0.0, 0.15743222187537007, 0.013196840619648702, 0.04214057042956277, 0.0, 0.00016967873470500933, 0.00016387637348489118, 0.0, 0.00142716210221, 0.0028506129662538376]
background
0.05937396401917247
-0.06497657226463704
0.05760231333522678
0.9903319833278178
1.0206104788566381

v9: l15 0.85
[0.40210489 0.30592979 0.19287442 0.09984625 0.03441234 0.03096303
 0.05393203 0.08496695 0.17804742 0.27043213 0.48869731]
[0.3293235  0.25250907 0.13351367 0.07687196 0.04690383 0.02377549
 0.04012434 0.07486667 0.14314649 0.25345992 0.36819562]
[0.06168423 0.04289328 0.0280361  0.01286042 0.00444562 0.00194915
 0.00586067 0.01553208 0.02461309 0.04536488 0.0648897 ]
['ft0', 'ggwwnp', 'ajllvvnp', 'sm', 'tt', 'jjllvv', 'ttj', 'ttjj', 'ttjjj', 'jll', 'jjll', 'jjjll', 'jjjjll', 'jlllv', 'jlllvb', 'ajll', 'ajjll', 'ajllvv']
[70.33523769312357, 69.23430075477707, 6.879493711020082, 14.014828715093419, 9.309685480444585, 17.92580935, 13.232578834619499, 18.211988057378374, 20.579663901430397, 7.294359613558813, 16.57523181827877, 17.130141879617266, 10.392097581532946, 0.5735141233029315, 0.21788534400341175, 0.0628110723740789, 0.23262742266023, 0.3529662955632318]
[14.474991917244832, 13.574538567986622, 1.9251552323742362, 0.021567911226675007, 0.002275835759561095, 0.03460163464832911, 0.002022402389518493, 0.004536891051113142, 0.0, 0.10495481458358004, 0.03959052185894611, 0.0, 0.0, 0.0005514558877912803, 0.00016387637348489118, 0.0, 0.0, 0.0032092993659811413]
background
0.04258168987978338
-0.06176872693021466
0.05640369547373934
1.0029466722004075
1.0259899685409104

"""