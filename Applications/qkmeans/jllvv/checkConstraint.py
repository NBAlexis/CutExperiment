import os

import numpy as np
from scipy.optimize import curve_fit

thresh = 0.15

ft0 = [-0.2 + 0.04 * i for i in range(0, 11)]
cstest = [1.152163, 1.150112, 1.148062, 1.147658, 1.147078, 1.146779, 1.14749, 1.148202, 1.148693, 1.150775, 1.152588]
cstest = np.array(cstest) * 1000
testcounts = [13940, 13570, 12953, 12686, 12637, 12180, 12297, 12671, 13067, 13612, 14383]
validationcounts = [30000, 8328, 5542, 30000, 7482, 2655, 1499, 41, 696, 482, 38, 30000, 9326, 15, 2, 13, 4839, 8, 384]
ttnjcountall = [5100000, 1147221, 256974, 100000]
L = 137

"""
trainset = ["ft0", "sm", "tt", "jjllvv"]
validationset = ["ttj", "ttjj", "ttjjj", "jll", "jjll", "jjjll", "jjjjll", "jlllv", "jlllvb", "pplpv", "jlpv", "ppll", "lllv", "llll", "allvv"]

ft0    : 520482/902883                 501223/902883                447927/902883           16384
SM     : 543214/2000000                160345/2000000 (88fb)        24712/2000000 (13fb)    16384
jjllvv : 656796/2000000 (0.26pb)       260768/2000000 (100fb)       51630/2000000 (21fb)    16384
tt     : 500288/2000000 (0.33pb)       157358/2000000 (100fb)       21926 / 5100000  0.10828809036275493 / 25.187871059475057 (*23%^2 = 5.7fb) 16384

validation:
ttj    :                                                            7482 / 1147221   0.1852382791248389 / 28.40273239987661 (*23%^2 = 9.8fb)
ttjj   :                                                            2655 / 256974    0.21674342419215695 / 20.978314383561333
ttjjj  :                                                            1499 / 100000    0.18453767254380798 / 12.310718648686324

jll    : 2762/1000000   (1.38pb)       233/1000000    (120fb)       41 / 3000000     0.006696064422222223 / 489.95593333333335
jjll   : 73432/8056073  (1.88pb)       7932/8056073   (200fb)       696 / 8056073    0.01785620313900667 / 206.68229309003863
jjjll  : 18096/1000000  (1.54pb)       2305/1000000   (200fb)       482 / 2000000    0.020308679510154505 / 84.26837971018466
jjjjll :                                                            38 / 100000      0.012294925410330204 / 32.355066869290006

jlllvb :                                                            9326 / 1001000   0.0006544285950270425 / 0.07024265747609582
jlllv  :                                                            40740 / 2501000  0.00172817791297052 / 0.10609162887430708

not considered:

pplpv (about 23720pb)                                                             1/7200000      0.00164639274691358 / 11854.027777777777
jlpv  (about 6000pb)                                                              2 / 4800000    0.0013449217447916667 / 3227.8121875
ppll  (1660.1875pb)    964/2000000    (0.8pb)        60/2000000     (50fb)        13 / 8000000   0.00269771125 / 1660.13

lllv                                                                              4839 / 1200000 0.0004722522505553229 / 0.11711153144583333
llll                                                                              8 / 100000     1.967086448e-06 / 0.0245885806
allvv  :                                                                          384 / 101484   8.83803777300739e-05 / 0.02335727670197609

jllll  :                                                                          0 / 2001       0.0 / 0.012674003232000039 < 0.006fb
"""
css = [0,
       13, # SM
       108.28809036275493 * 0.23 * 0.23,  # tt
       720.1 * 51630 / 2000000,  # jjllvv
       0,  # ttj
       0,  # ttjj
       0,  # ttjjj
       6.696064422222223,  # jll
       17.85620313900667,  # jjll
       20.308679510154505,  # jjjll
       12.294925410330204,  # jjjjll
       1.72817791297052,  # jlllv
       0.6544285950270425,  # jlllvb
       1.64639274691358,  # pplpv
       1.3449217447916667,  # jlpv
       2.69771125,  # ppll
       0.4722522505553229,  # lllv
       1.967086448e-03,  # llll
       8.83803777300739e-02  # allvv
       ]
css = np.array(css)
os.chdir("../../../_DataFolder/qkmeans/jllvv/")

testres = np.loadtxt("wf/test-16384-l5.csv", delimiter=',')
validationres = np.loadtxt("wf/validation-16384-l2.csv", delimiter=',')

testrest = []
nstart = 0
for c in testcounts:
    s = testres[nstart:nstart+c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    testrest.append(sAbove)
    nstart = nstart + c
testrest = np.array(testrest)

validationrest = []
validationrestratio = []
nstart = 0
for c in validationcounts:
    s = validationres[nstart:nstart+c]
    sAbove = len(s[s[:, 0] > thresh, 0])
    validationrest.append(sAbove)
    validationrestratio.append(sAbove / c)
    nstart = nstart + c
validationrest = np.array(validationrest)
validationrestratio = np.array(validationrestratio)

# find lowest cut efficiency for tt+Nj
print("tt + Nj")
tttowb = 12.310718648686324 / 249.25127345975994
print(tttowb * 888000 * 0.23 * 0.23 * validationrest[2] / ttnjcountall[0])
print(tttowb * 888000 * 0.23 * 0.23 * validationrest[4] / ttnjcountall[1])
print(tttowb * 888000 * 0.23 * 0.23 * validationrest[5] / ttnjcountall[2])
print(tttowb * 888000 * 0.23 * 0.23 * validationrest[6] / ttnjcountall[3])

ttall = tttowb * 888000 * 0.23 * 0.23 * validationrest[2] / ttnjcountall[0]
validationrestratio = validationrestratio * css
print("other backgrounds")
print(validationrestratio)

csothersidx = np.array([4, 8, 9, 10, 11, 12, 13])
# csothersidx = np.array([4, 9, 10, 12, 13])
allotherbg = ttall + np.sum(validationrestratio[csothersidx])
print("all other backgrounds")
print(allotherbg)

alltestcs = testrest * cstest / 1000000
print(alltestcs)

alltestcs = allotherbg + alltestcs
print(alltestcs)

def csfunc(x, a, b, c):
    return a + b * x + c * x * x

popt, _ = curve_fit(csfunc, ft0, alltestcs)
csbg = popt[0]
cssint = popt[1]
csssq = popt[2]
ss=2
left=(-cssint-np.sqrt(cssint**2+(2*csssq*(ss**2+np.sqrt(4 * csbg * L * ss**2+ss**4)))/L))/(2*csssq)
right=(-cssint+np.sqrt(cssint**2+(2*csssq*(ss**2+np.sqrt(4 * csbg * L * ss**2+ss**4)))/L))/(2*csssq)

print(left)
print(right)

print((1/(16*right))**(0.25))

