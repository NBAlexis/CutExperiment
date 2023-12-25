import re

from DataStructure.EventSet import EventSet
from DataStructure.LorentzVector import LorentzVector
from DataStructure.Particles import ParticleType


def selectLargestPhotons(events: EventSet, sqrts: float):
    retlist = []
    allmomentum = LorentzVector(sqrts, 0, 0, 0)
    for event in events.events:
        p1index = -1
        p2index = -1
        p1m = [-1, 0, 0, 0]
        p2m = [-1, 0, 0, 0]
        totalm = LorentzVector(0, 0, 0, 0)
        for particle in event.particles:
            if ParticleType.Photon == particle.particleType:
                if particle.momentum.values[0] > p1m[0]:
                    p2index = p1index
                    p2m = p1m
                    p1index = particle.index
                    p1m = particle.momentum.values
                elif particle.momentum.values[0] > p2m[0]:
                    p2index = particle.index
                    p2m = particle.momentum.values
            if ParticleType.Missing != particle.particleType:
                totalm = totalm + particle.momentum
        if p1index > 0 and p2index > 0:
            missm = allmomentum - totalm
            retlist.append(p1m + p2m + missm.values)
    return retlist


def findCS(fileName: str) -> str:
    with open(fileName) as f:
        bannertext = f.read()
        searchtext = re.search("""Integrated weight\s\(pb\)[\s]*\:[\s]*([\.\d+e\-]+)[\s]*""", bannertext)
        return float(searchtext.group(1))


def findCoff(fileName: str, paramName: str) -> str:
    with open(fileName) as f:
        bannertext = f.read()
        searchtext = re.search("""[\d]+[\s]+([\.\d+e\-]+)[\s]+\#[\s]+""" + paramName, bannertext)
        return float(searchtext.group(1))


def findLogTxt(fileName: str):
    lineNumber = 0
    lstA = []
    lstB = []
    with open(fileName) as f:
        for lines in f.readlines():
            lineNumber = lineNumber + 1
            if 1 == lineNumber:
                continue
            linesrep = re.sub("[\\s]+", " ", lines)
            contentList = linesrep.split(' ')
            if 3 <= len(contentList):
                lstA.append(float(contentList[1]))
                lstB.append(float(contentList[2]))
    return lstA, lstB
