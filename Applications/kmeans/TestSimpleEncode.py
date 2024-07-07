"""


"""
import numpy as np

vtest = [-2.219428427064474574e-01,-2.080759378357706357e-02,9.842508935813076842e-02,1.096014891232260924e-01,-5.563325360209519371e-02,2.340083368805381814e-02,-8.668671161025723326e-02,-2.495999396951170124e-01,2.267926831618269079e-01,1.711864065389313849e-02,-8.363397026485545893e-02,-7.620323975045822928e-02]


def VectorToSimpleEncodeVector(v):
    theta = v[10] / 2
    phi = v[11] / 2
    ret = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j)] * 32 + [
        np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 32
    ret = np.array(ret)

    ret = np.reshape(ret, (4, 16))
    theta = v[8] / 2
    phi = v[9] / 2
    mul = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j), np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 2
    ret = np.transpose(np.transpose(ret) * np.array(mul))

    ret = np.reshape(ret, (8, 8))
    theta = v[6] / 2
    phi = v[7] / 2
    mul = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j), np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 4
    ret = np.transpose(np.transpose(ret) * np.array(mul))

    ret = np.reshape(ret, (16, 4))
    theta = v[4] / 2
    phi = v[5] / 2
    mul = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j), np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 8
    ret = np.transpose(np.transpose(ret) * np.array(mul))

    ret = np.reshape(ret, (32, 2))
    theta = v[2] / 2
    phi = v[3] / 2
    mul = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j), np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 16
    ret = np.transpose(np.transpose(ret) * np.array(mul))

    ret = np.reshape(ret, (64, 1))
    theta = v[0] / 2
    phi = v[1] / 2
    mul = [np.cos(theta * np.pi) * np.exp(-phi * np.pi * 1j), np.sin(theta * np.pi) * np.exp(phi * np.pi * 1j)] * 32
    ret = np.transpose(np.transpose(ret) * np.array(mul))

    ret = ret.flatten()
    return ret

vres = VectorToSimpleEncodeVector(vtest)
print(vres)
print(np.dot(np.conjugate(vres), vres))