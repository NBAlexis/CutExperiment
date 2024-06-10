import os

import numpy as np

from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../../_DataFolder/qkmeans/jllvv/")


def findLargestTwoPhotons(events: EventSet, missE: float):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        plp = event.GetParticle(lps[0]).momentum
        plm = event.GetParticle(lms[0]).momentum
        ret.append([
            pj.values[0],
            pj.values[1],
            pj.values[2],
            pj.values[3],

            plp.values[0],
            plp.values[1],
            plp.values[2],
            plp.values[3],

            plm.values[0],
            plm.values[1],
            plm.values[2],
            plm.values[3],

            pm.values[0],
            pm.values[1],
            pm.values[2]
        ])
    return np.array(ret)

# lhcoevent = LoadLHCOlympics("features/ft0.lhco")
# lhcoevent = LoadLHCOlympics("features/jllvvsm1-1.lhco")
# lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm1-2.lhco"))
lhcoevent = LoadLHCOlympics("features/jllvvsm2-1.lhco")
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-2.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-3.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-4.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-5.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-6.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvsm2-7.lhco"))
lhcoevent.AddEventSet(LoadLHCOlympics("features/jjll1.lhco"))
# lhcoevent = LoadLHCOlympics("features/jllvvtt1.lhco")
# lhcoevent.AddEventSet(LoadLHCOlympics("features/jllvvtt2.lhco"))
print(len(lhcoevent.events))
filtered = findLargestTwoPhotons(lhcoevent, 50)
print(len(filtered))
# np.savetxt("featurecsv/ft0.csv", filtered, delimiter=',')
# np.savetxt("featurecsv/sm.csv", filtered, delimiter=',')
np.savetxt("featurecsv/jjll.csv", filtered, delimiter=',')
# np.savetxt("featurecsv/tt.csv", filtered, delimiter=',')

"""
ETMissing = 50

ft0  : 520482/902883
SM   : 543214/2000000
jjll : 55076/6056073
tt   : 500288/2000000

"""