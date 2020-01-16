import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import *
from CutAndExport.FilterFunctions import *
from CutAndExport.Histogram import *
from CutAndExport.SpecialTest import *
from Interfaces.LHCOlympics import LoadLHCOlympics
from Interfaces.LesHouchesEvent import LoadLesHouchesEvent

os.chdir("F:/PyworkingFolder/CutExperiment/_DataFolder")

es = 100
fm0file = LoadLesHouchesEvent("wa/energyScale/{}tevfm0.lhe".format(es))
fm1file = LoadLesHouchesEvent("wa/energyScale/{}tevfm1.lhe".format(es))
fm2file = LoadLesHouchesEvent("wa/energyScale/{}tevfm2.lhe".format(es))
fm3file = LoadLesHouchesEvent("wa/energyScale/{}tevfm3.lhe".format(es))
fm4file = LoadLesHouchesEvent("wa/energyScale/{}tevfm4.lhe".format(es))
fm5file = LoadLesHouchesEvent("wa/energyScale/{}tevfm5.lhe".format(es))
fm7file = LoadLesHouchesEvent("wa/energyScale/{}tevfm7.lhe".format(es))
fm0file.AddEventSet(fm1file)
fm0file.AddEventSet(fm2file)
fm0file.AddEventSet(fm3file)
fm0file.AddEventSet(fm4file)
fm0file.AddEventSet(fm5file)
fm0file.AddEventSet(fm7file)

photonMomentum = LorentzVector()
WMomentum = LorentzVector()
energyList = []

for event in fm0file.events:
    for particle in event.particles:
        if 22 == particle.PGDid:
            iphotonMomentum = particle.momentum
        if 24 == particle.PGDid:
            WMomentum = particle.momentum
    momentumSum = iphotonMomentum + WMomentum
    sq = momentumSum * momentumSum
    if sq > 0:
        sq = math.sqrt(sq)
    else:
        sq = 0
    energyList.append(sq)


import matplotlib.pyplot as plt

frequency_each, a, b = plt.hist(energyList, 100, range=[0, 60000])
plt.show()
print(frequency_each)

print("============")

for i in range(0, 100):
    print(i, sum(frequency_each[0:i]) / 70000)
