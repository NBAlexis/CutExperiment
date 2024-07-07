import numpy as np

from CutAndExport.CutFunctions import FindHardestParticlesByType, FindHardestParticlesByTypes
from DataStructure.EventSample import EventSample
from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType


def jetCount(event: EventSample) -> float:
    count = 0.0
    for particle in event.particles:
        if ParticleType.Jet == particle.particleType:
            if particle.momentum.values[0] > 0.0:
                count = count + 1.0
    return count


def findJetAndTwoLeptons(events: EventSet, missE: float, jetE: float, leptonE: float):
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
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
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


def findJetAndTwoLeptonsV2(events: EventSet, missE: float, jetE: float, leptonE: float):
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
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        pj3 = LorentzVector(0, 0, 0, 0)
        plp2 = LorentzVector(0, 0, 0, 0)
        plm2 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        if len(jets) > 2:
            pj3 = event.GetParticle(jets[2]).momentum
        if len(lps) > 1:
            plp2 = event.GetParticle(lps[1]).momentum
        if len(lms) > 1:
            plm2 = event.GetParticle(lms[1]).momentum
        ret.append([
            pj.values[0],
            pj.values[1],
            pj.values[2],
            pj.values[3],

            pj2.values[0],
            pj2.values[1],
            pj2.values[2],
            pj2.values[3],

            pj3.values[0],
            pj3.values[1],
            pj3.values[2],
            pj3.values[3],

            plp.values[0],
            plp.values[1],
            plp.values[2],
            plp.values[3],

            plp2.values[0],
            plp2.values[1],
            plp2.values[2],
            plp2.values[3],

            plm.values[0],
            plm.values[1],
            plm.values[2],
            plm.values[3],

            plm2.values[0],
            plm2.values[1],
            plm2.values[2],
            plm2.values[3],

            pm.values[0],
            pm.values[1],
            pm.values[2]
        ])
    return np.array(ret)


def findJetAndTwoLeptonsV3(events: EventSet, missE: float, jetE: float, leptonE: float, jetcount: int):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        if len(lps) > 1 or len(lms) > 1:
            continue
        if len(jets) > jetcount:
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        pj3 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        if len(jets) > 2:
            pj3 = event.GetParticle(jets[2]).momentum
        pjall = LorentzVector(0, 0, 0, 0)
        for jetidx in jets:
            pjall = pjall + event.GetParticle(jetidx).momentum
        plall = plp + plm
        plpf = 0.0 if ParticleType.Electron == event.GetParticle(lps[0]).particleType else 1.0
        plmf = 0.0 if ParticleType.Electron == event.GetParticle(lms[0]).particleType else 1.0
        ret.append([
            pj.values[0],
            pj.Pt(),

            pj2.values[0],
            pj2.Pt(),

            pj3.values[0],
            pj3.Pt(),

            plp.values[0],
            plp.Pt(),

            plm.values[0],
            plm.Pt(),

            pm.Pt(),

            pjall.Mass(),
            plall.Mass(),

            plpf,
            plmf
        ])
    return np.array(ret)


# V4 is the best for now
def findJetAndTwoLeptonsV4(events: EventSet, missE: float, jetE: float, leptonE: float, jetcount: int):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        if len(lps) > 1 or len(lms) > 1:
            continue
        if len(jets) > jetcount:
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        pj3 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        if len(jets) > 2:
            pj3 = event.GetParticle(jets[2]).momentum
        pjall = LorentzVector(0, 0, 0, 0)
        for jetidx in jets:
            pjall = pjall + event.GetParticle(jetidx).momentum
        plall = plp + plm
        plpf = 0.0 if ParticleType.Electron == event.GetParticle(lps[0]).particleType else 1.0
        plmf = 0.0 if ParticleType.Electron == event.GetParticle(lms[0]).particleType else 1.0
        ret.append([
            pj.values[0],
            pj.values[1],
            pj.values[2],
            pj.values[3],

            pj2.values[0],
            pj2.values[1],
            pj2.values[2],
            pj2.values[3],

            pj3.values[0],
            pj3.values[1],
            pj3.values[2],
            pj3.values[3],

            plp.values[0],
            plp.values[1],
            plp.values[2],
            plp.values[3],

            plm.values[0],
            plm.values[1],
            plm.values[2],
            plm.values[3],

            pjall.Mass(),
            plall.Mass(),
            plpf,
            plmf,

            pm.values[0],
            pm.values[1],
            pm.values[2],

            0,
            0,
            0,
            0
        ])
    return np.array(ret)


def findJetAndTwoLeptonsV5(events: EventSet, missE: float, jetE: float, leptonE: float, jetcount: int):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        photons = FindHardestParticlesByType(event, ParticleType.Photon)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        if len(lps) > 1 or len(lms) > 1:
            continue
        if len(jets) > jetcount:
            continue
        if len(photons) > 1:
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        pj3 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        if len(jets) > 2:
            pj3 = event.GetParticle(jets[2]).momentum
        pa = LorentzVector(0, 0, 0, 0)
        if len(photons) > 0:
            pa = event.GetParticle(photons[0]).momentum
        pjall = LorentzVector(0, 0, 0, 0)
        for jetidx in jets:
            pjall = pjall + event.GetParticle(jetidx).momentum
        plall = plp + plm
        plpf = 0.0 if ParticleType.Electron == event.GetParticle(lps[0]).particleType else 1.0
        plmf = 0.0 if ParticleType.Electron == event.GetParticle(lms[0]).particleType else 1.0
        jetplus = LorentzVector.AngleBetween(pjall, plp)
        jetminus = LorentzVector.AngleBetween(pjall, plm)
        jetplush = (pj + plp).Mass()
        jetminush = (pj + plm).Mass()
        ret.append([
            pj.values[0],
            pj.values[1],
            pj.values[2],
            pj.values[3],

            pj2.values[0],
            pj2.values[1],
            pj2.values[2],
            pj2.values[3],

            pj3.values[0],
            pj3.values[1],
            pj3.values[2],
            pj3.values[3],

            plp.values[0],
            plp.values[1],
            plp.values[2],
            plp.values[3],

            plm.values[0],
            plm.values[1],
            plm.values[2],
            plm.values[3],

            pa.values[0],
            pa.values[1],
            pa.values[2],
            pa.values[3],

            pm.values[0],
            pm.values[1],
            pm.values[2],
            plpf,

            plmf,
            pjall.Pt(),
            0
        ])
    return np.array(ret)


def findJetAndTwoLeptonsV6(events: EventSet, missE: float, jetE: float, leptonE: float, jetcount: int):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        photons = FindHardestParticlesByType(event, ParticleType.Photon)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        if len(lps) > 1 or len(lms) > 1:
            continue
        if len(jets) > jetcount:
            continue
        if len(photons) > 1:
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        pj3 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        if len(jets) > 2:
            pj3 = event.GetParticle(jets[2]).momentum
        pa = LorentzVector(0, 0, 0, 0)
        if len(photons) > 0:
            pa = event.GetParticle(photons[0]).momentum
        pjall = LorentzVector(0, 0, 0, 0)
        for jetidx in jets:
            pjall = pjall + event.GetParticle(jetidx).momentum
        plall = plp + plm
        plpf = 0.0 if ParticleType.Electron == event.GetParticle(lps[0]).particleType else 1.0
        plmf = 0.0 if ParticleType.Electron == event.GetParticle(lms[0]).particleType else 1.0
        jetplus = LorentzVector.AngleBetween(pjall, plp)
        jetminus = LorentzVector.AngleBetween(pjall, plm)
        jetplush = (pj + plp).Mass()
        jetminush = (pj + plm).Mass()
        ret.append([
            pj.values[0],
            pj.values[1],
            pj.values[2],
            pj.values[3],

            pj2.values[0],
            pj2.values[1],
            pj2.values[2],
            pj2.values[3],

            pj3.values[0],
            pj3.values[1],
            pj3.values[2],
            pj3.values[3],

            plp.values[0],
            plp.values[1],
            plp.values[2],
            plp.values[3],

            plm.values[0],
            plm.values[1],
            plm.values[2],
            plm.values[3],

            pa.values[0],
            pa.values[1],
            pa.values[2],
            pa.values[3],

            pm.values[0],
            pm.values[1],
            pm.values[2],
            plpf,

            plmf,
            0,
            0
        ])
    return np.array(ret)


def findJetAndTwoLeptonsV7(events: EventSet, missE: float, jetE: float, leptonE: float, jetcount: int):
    ret = []
    for event in events.events:
        jets = FindHardestParticlesByType(event, ParticleType.Jet)
        photons = FindHardestParticlesByType(event, ParticleType.Photon)
        lps = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], 1)
        lms = FindHardestParticlesByTypes(event, [ParticleType.Electron, ParticleType.Muon], -1)
        mis = FindHardestParticlesByType(event, ParticleType.Missing)
        if 0 == len(jets) or 0 == len(lps) or 0 == len(lms) or 0 == len(mis):
            # print("indexes = {}, {}, {}, {}".format(len(jets), len(lps), len(lms), len(mis)))
            continue
        if len(lps) > 1 or len(lms) > 1:
            continue
        if len(jets) > jetcount:
            continue
        if len(photons) > 1:
            continue
        pm = event.GetParticle(mis[0]).momentum
        if pm.values[0] < missE:
            continue
        pj = event.GetParticle(jets[0]).momentum
        if pj.values[0] < jetE:
            continue
        plp = event.GetParticle(lps[0]).momentum
        if plp.values[0] < leptonE:
            continue
        plm = event.GetParticle(lms[0]).momentum
        if plm.values[0] < leptonE:
            continue
        pj2 = LorentzVector(0, 0, 0, 0)
        if len(jets) > 1:
            pj2 = event.GetParticle(jets[1]).momentum
        pa = LorentzVector(0, 0, 0, 0)
        if len(photons) > 0:
            pa = event.GetParticle(photons[0]).momentum
        pjall = LorentzVector(0, 0, 0, 0)
        for jetidx in jets:
            pjall = pjall + event.GetParticle(jetidx).momentum
        plpf = 0.0 if ParticleType.Electron == event.GetParticle(lps[0]).particleType else 1.0
        plmf = 0.0 if ParticleType.Electron == event.GetParticle(lms[0]).particleType else 1.0
        ret.append([
            pj.values[0],
            pj.Pt(),
            pj2.values[0],
            pj2.Pt(),
            plp.values[0],
            plp.Pt(),
            plm.values[0],
            plm.Pt(),
            pa.values[0],
            pa.Pt(),
            pm.Pt(),
            plpf,
            plmf,
            0,
            0
        ])
    return np.array(ret)
