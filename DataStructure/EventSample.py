import math

from DataStructure.Particles import Particle, ParticleStatus, ParticleType


class EventSample:
    def __init__(self):
        self.particles = []

    def AddParticle(self, particle: Particle):
        self.particles.append(particle)

    def GetParticleCount(self) -> int:
        return len(self.particles)

    def GetLeptonCount(self) -> int:
        leptonCount = 0
        for particle in self.particles:
            if 1 <= particle.particleType <= 3:
                leptonCount += 1
        return leptonCount

    def GetJetCount(self) -> int:
        jetCount = 0
        for particle in self.particles:
            if 4 == particle.particleType:
                jetCount += 1
        return jetCount

    def GetPTMissing2d(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return [ptx, pty]

    def GetETMissing(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTMissingAzimuth(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Invisible == particle.status:
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def GetPTLepton(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTLeptonAzimuth(self) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                ptx += particle.momentum.values[1]
                pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def GetPTLeptonPM(self, bPM: bool) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                if bPM and particle.PGDid < 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
                elif (not bPM) and particle.PGDid > 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
        return math.sqrt(ptx * ptx + pty * pty)

    def GetPTLeptonAzimuthPM(self, bPM: bool) -> float:
        ptx = 0.0
        pty = 0.0
        for particle in self.particles:
            if ParticleStatus.Outgoing == particle.status and \
                    (ParticleType.Electron == particle.particleType
                     or ParticleType.Muon == particle.particleType
                     or ParticleType.Tau == particle.particleType):
                if bPM and particle.PGDid < 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
                elif (not bPM) and particle.PGDid > 0:
                    ptx += particle.momentum.values[1]
                    pty += particle.momentum.values[2]
        return math.atan2(pty, ptx)

    def DebugPrint(self) -> str:
        ret = "PID  PGDID  ST  T  ---MASS(GeV)---  MOMENTUM_T(GeV)  MOMENTUM_X(GeV)  MOMENTUM_Y(GeV)  MOMENTUM_Z(GeV)  ----HECILITY---\n"
        for i in range(len(self.particles)):
            ret += self.particles[i].DebugPrint() + "\n"
        return ret
