import os

import numpy as np

from Applications.qkmeans.jllvv.jllvvUsefullFunctions import findJetAndTwoLeptons
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/jllvv/")

counts = []
for i in range(11):
    lhcoevent = LoadLHCOlympics("full/ft0-{}.lhco".format(i))
    print("full/ft0-{}.lhco loaded".format(i))
    # print(len(lhcoevent.events))
    filtered = findJetAndTwoLeptons(lhcoevent, 200, -1, -1)
    # print(len(filtered))
    counts.append(len(filtered))
    np.savetxt("fullcsv/ft0-{}.csv".format(i), filtered, delimiter=',')

print(counts)

"""
[13940, 13570, 12953, 12686, 12637, 12180, 12297, 12671, 13067, 13612, 14383]
"""
