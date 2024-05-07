import numpy as np

for energy in ["1500", "5000", "7000", "15000"]:
    sm = np.loadtxt('../Features/SM-{}.csv'.format(energy), delimiter=',')
    ft0 = np.loadtxt('../Features/FgT0-{}.csv'.format(energy), delimiter=',')
    ft1 = np.loadtxt('../Features/FgT1-{}.csv'.format(energy), delimiter=',')
    ft2 = np.loadtxt('../Features/FgT2-{}.csv'.format(energy), delimiter=',')
    ft3 = np.loadtxt('../Features/FgT3-{}.csv'.format(energy), delimiter=',')
    # np.random.shuffle(sm)
    train = sm[0:400000]
    validation = sm[400000:500000]
    test = sm[500000:]
    meantrain = np.mean(train, axis=0)
    stdtrain = np.std(train, axis=0)
    train = (train - meantrain) / stdtrain
    validation = (validation - meantrain) / stdtrain
    test = (test - meantrain) / stdtrain
    ft0 = (ft0 - meantrain) / stdtrain
    ft1 = (ft1 - meantrain) / stdtrain
    ft2 = (ft2 - meantrain) / stdtrain
    ft3 = (ft3 - meantrain) / stdtrain
    np.savetxt('../datas/NoShuffleSMTrain-{}.csv'.format(energy), train, delimiter=',')
    np.savetxt('../datas/NoShuffleSMValidation-{}.csv'.format(energy), validation, delimiter=',')
    np.savetxt('../datas/NoShuffleSMTest-{}.csv'.format(energy), test, delimiter=',')
    np.savetxt('../datas/NoShuffleFgT0-{}.csv'.format(energy), ft0, delimiter=',')
    np.savetxt('../datas/NoShuffleFgT1-{}.csv'.format(energy), ft1, delimiter=',')
    np.savetxt('../datas/NoShuffleFgT2-{}.csv'.format(energy), ft2, delimiter=',')
    np.savetxt('../datas/NoShuffleFgT3-{}.csv'.format(energy), ft3, delimiter=',')




