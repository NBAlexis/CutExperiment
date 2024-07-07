import os

import numpy as np

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

trainset = ["ft0", "ggwwnp", "ajllvvnp", "sm",
            "tt", "jjllvv", "ttj", "ttjj",
            "ttjjj", "jll", "jjll", "jjjll",
            "jjjjll", "jlllv", "jlllvb", "ajll",
            "ajjll", "ajllvv"]

savefix = 16384
VALIDATIONCOUNT = 30000
trainpick = [12288, 16384, 4096, 8192,
             8192, 16384, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0]

for VERSION in [4]:
    countlist = []
    trainPointSet = None
    validationPointSet = None

    for i in range(len(trainset)):
        s = np.loadtxt("featurecsvv{}/{}.csv".format(VERSION, trainset[i]), delimiter=',')
        if trainpick[i] > 0 or len(s) > VALIDATIONCOUNT:
            np.random.shuffle(s)
        if trainpick[i] > 0:
            if trainPointSet is None:
                trainPointSet = s[0:trainpick[i]]
            else:
                trainPointSet = np.vstack((trainPointSet, s[0:trainpick[i]]))
        tobeadd = None
        if len(s) > (trainpick[i] + VALIDATIONCOUNT):
            tobeadd = s[trainpick[i]:trainpick[i] + VALIDATIONCOUNT]
        else:
            tobeadd = s[trainpick[i]:]
        if validationPointSet is None:
            validationPointSet = tobeadd
        else:
            validationPointSet = np.vstack((validationPointSet, tobeadd))
        countlist.append(len(tobeadd))
    print(len(trainPointSet))
    traingsetmean = np.mean(trainPointSet, axis=0)
    traingsetstd = np.std(trainPointSet, axis=0) + 1.0e-18

    trainPointSet = (trainPointSet - traingsetmean) / traingsetstd
    np.savetxt("wfv{}/trainv{}se-{}.csv".format(VERSION, VERSION, savefix), trainPointSet / 4, delimiter=',')
    trainPointSet = np.hstack((trainPointSet, np.ones((len(trainPointSet), 1))))
    traingsetnorm = np.sqrt(np.sum(trainPointSet * trainPointSet, axis=1))
    trainPointSet = np.transpose(np.transpose(trainPointSet) / traingsetnorm)

    validationPointSet = (validationPointSet - traingsetmean) / traingsetstd
    np.savetxt("wfv{}/validationv{}se-{}.csv".format(VERSION, VERSION, savefix), validationPointSet / 4, delimiter=',')
    validationPointSet = np.hstack((validationPointSet, np.ones((len(validationPointSet), 1))))
    validationsetnorm = np.sqrt(np.sum(validationPointSet * validationPointSet, axis=1))
    validationPointSet = np.transpose(np.transpose(validationPointSet) / validationsetnorm)

    np.savetxt("wfv{}/trainv{}-{}.csv".format(VERSION, VERSION, savefix), trainPointSet, delimiter=',')
    np.savetxt("wfv{}/validationv{}-{}.csv".format(VERSION, VERSION, savefix), validationPointSet, delimiter=',')

    print("{}-{}:".format(VERSION, savefix))
    print(traingsetmean)
    print(traingsetstd)
    print(countlist)

"""
65536
4-16384:
4-16384:
[ 6.83452592e+02  7.88062820e-02  7.77852660e-01 -1.78214735e-01
  2.65376435e+02  1.96746823e-01 -6.24724261e-02 -5.71246181e-01
  1.12559091e+02 -2.58567758e-01 -3.17167872e-01  3.18812838e-01
  4.50516115e+02 -1.12276237e-01 -1.64387516e+00  2.90966649e+00
  4.40493430e+02  1.07718251e+00  1.91826674e-01 -1.28825180e+00
  7.62317317e+02  5.77269203e+02  5.59341431e-01  5.67825317e-01
  4.73303734e+02 -9.89347884e-01  1.22663769e+00  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
[5.18547454e+02 2.29354941e+02 2.30545860e+02 7.93034804e+02
 2.37599506e+02 1.24677553e+02 1.22719878e+02 3.09474827e+02
 1.30123688e+02 6.52765588e+01 6.49630533e+01 1.44698237e+02
 5.33400086e+02 3.72805435e+02 3.72141954e+02 4.58252887e+02
 5.37613509e+02 3.69624667e+02 3.71619262e+02 4.56439058e+02
 6.87605819e+02 6.58695269e+02 4.96466106e-01 4.95378367e-01
 3.45855518e+02 4.13789285e+02 4.15220915e+02 1.00000000e-18
 1.00000000e-18 1.00000000e-18 1.00000000e-18]
[30000, 30000, 15008, 16262, 12277, 30000, 6546, 20075, 887, 141, 1256, 814, 258, 13628, 9363, 26, 167, 19265]
65536
5-16384:
[ 6.86344350e+02  1.92279149e-01 -2.66291460e-01 -5.59731960e-01
  2.67037657e+02  3.81365306e-01 -6.64673999e-02  1.39336980e+00
  1.13091251e+02  1.62199114e-01  8.65330329e-02 -5.18228968e-02
  4.52559324e+02 -2.56110265e+00 -3.45349419e-01  1.22458439e+00
  4.37099082e+02  1.65377232e+00 -1.50134022e+00  5.09533526e-01
  5.35415008e+01 -1.05167673e-01  3.95618552e-01 -3.19840643e-01
  4.73331767e+02  5.48453075e-01  2.12538100e+00  5.61676025e-01
  5.63232422e-01  2.98282182e+02  0.00000000e+00]
[5.20557318e+02 2.31016178e+02 2.32983700e+02 7.95624696e+02
 2.39270085e+02 1.24095749e+02 1.24339153e+02 3.11758679e+02
 1.29468387e+02 6.43521323e+01 6.54838497e+01 1.44700831e+02
 5.37135366e+02 3.73146449e+02 3.73296621e+02 4.63387007e+02
 5.32417918e+02 3.67856195e+02 3.67916995e+02 4.51484325e+02
 2.72413370e+02 1.49295943e+02 1.53243134e+02 1.76925775e+02
 3.46745158e+02 4.15589094e+02 4.14193255e+02 4.96181487e-01
 4.95985545e-01 2.34806237e+02 1.00000000e-18]
[30000, 30000, 13472, 16245, 12272, 30000, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697]
65536
6-16384:
[ 6.86731920e+02 -1.69283190e-01  1.07985059e+00  3.52239852e+00
  2.66714631e+02  3.87693396e-02  9.86711411e-01 -2.08673937e-01
  1.13250706e+02  1.39139768e-01  2.14674029e-01 -9.25937967e-01
  4.54788752e+02 -1.11468728e+00 -1.51171715e+00  2.92139285e+00
  4.39231952e+02  1.02622892e+00 -2.53312441e+00 -5.54957036e-01
  5.20965541e+01 -1.62875382e-01 -1.39572592e-01 -1.12263276e+00
  4.71439722e+02  2.53593338e-01  1.84156459e+00  5.65277100e-01
  5.65231323e-01  0.00000000e+00  0.00000000e+00]
[5.22385403e+02 2.28539927e+02 2.32043892e+02 7.98146684e+02
 2.37784511e+02 1.24176047e+02 1.24473706e+02 3.10261318e+02
 1.30288638e+02 6.45507771e+01 6.48136015e+01 1.45769052e+02
 5.38448661e+02 3.74880702e+02 3.74711529e+02 4.64546478e+02
 5.35899337e+02 3.72716818e+02 3.66301480e+02 4.54983980e+02
 2.63631188e+02 1.47574694e+02 1.45324330e+02 1.71221193e+02
 3.45249691e+02 4.14833568e+02 4.11536650e+02 4.95720587e-01
 4.95726613e-01 1.00000000e-18 1.00000000e-18]
[30000, 30000, 13472, 16245, 12272, 30000, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697]
65536
7-16384:
[6.81887522e+02 2.30170524e+02 2.65302277e+02 1.16877644e+02
 4.53349414e+02 3.29552131e+02 4.41613143e+02 3.21911810e+02
 5.23921412e+01 3.96526715e+01 4.73212444e+02 5.63201904e-01
 5.68328857e-01 0.00000000e+00 0.00000000e+00]
[5.14466582e+02 2.29801079e+02 2.36489577e+02 1.29433161e+02
 5.41543001e+02 4.15382852e+02 5.38567346e+02 4.16677712e+02
 2.64973092e+02 2.07051159e+02 3.47748005e+02 4.95989435e-01
 4.95309163e-01 1.00000000e-18 1.00000000e-18]
[30000, 30000, 13472, 16245, 12272, 30000, 6543, 20071, 887, 139, 1256, 813, 257, 13520, 9307, 22, 163, 18697]

Process finished with exit code 0


"""
