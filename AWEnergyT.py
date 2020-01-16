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
ft0file = LoadLesHouchesEvent("wa/energyScale/{}tevft0.lhe".format(es))
ft1file = LoadLesHouchesEvent("wa/energyScale/{}tevft1.lhe".format(es))
ft2file = LoadLesHouchesEvent("wa/energyScale/{}tevft2.lhe".format(es))
ft5file = LoadLesHouchesEvent("wa/energyScale/{}tevft5.lhe".format(es))
ft6file = LoadLesHouchesEvent("wa/energyScale/{}tevft6.lhe".format(es))
ft7file = LoadLesHouchesEvent("wa/energyScale/{}tevft7.lhe".format(es))
ft0file.AddEventSet(ft1file)
ft0file.AddEventSet(ft2file)
ft0file.AddEventSet(ft5file)
ft0file.AddEventSet(ft6file)
ft0file.AddEventSet(ft7file)

photonMomentum = LorentzVector()
WMomentum = LorentzVector()
energyList = []

for event in ft0file.events:
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
    print(i, sum(frequency_each[0:i]) / 60000)
