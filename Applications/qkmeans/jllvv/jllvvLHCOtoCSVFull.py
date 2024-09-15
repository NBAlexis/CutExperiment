import os

import numpy as np

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import findJetAndTwoLeptonsV7
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

beforecut = []
counts = []
for i in range(11):
    lhcoevent = LoadLHCOlympics("full/ajllvvall-{}.lhco".format(i))
    print("full/{}.lhco loaded".format(i))
    beforecut.append(len(lhcoevent.events))
    filtered = findJetAndTwoLeptonsV7(lhcoevent, 200, -1, -1, 6)
    # print(len(filtered))
    counts.append(len(filtered))
    np.savetxt("fullcsv/ajll-{}.csv".format(i), filtered, delimiter=',')

print(beforecut)
print(counts)

"""
ft0:
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
[13722, 13385, 12787, 12524, 12501, 12069, 12170, 12538, 12902, 13429, 14171]


jjll
[1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]
[26980, 26327, 25420, 24889, 24362, 24673, 25165, 25176, 25572, 26241, 27357]


ajjvv
[89787, 100000, 100000, 100000, 100000, 100000, 100000, 37846, 100000, 100000, 100000]
[2685, 2587, 2289, 2131, 1925, 1786, 1914, 828, 2219, 2581, 3067]

"""
