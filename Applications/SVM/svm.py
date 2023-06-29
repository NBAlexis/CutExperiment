import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter


class SMOStruct:
    def __init__(self, X, Y, C, xi):
        self.X = X
        self.Y = Y
        self.C = C
        self.xi = xi
        self.m = self.X.shape[0]
        self.alphas = np.zeros(self.m)
        self.b = 0
        self.eCaches = np.zeros((self.m, 2))


def SelectJdown(i, m):
    j = i
    while (j == i):
        j = np.random.randint(0, m)
    return j


def CaculateEi(object, i):
    g_xi = np.multiply(object.alphas, object.Y).T @ (object.X @ object.X[i, :].T) + object.b
    return g_xi - object.Y[i]


def UpdateEk(object, k):
    Ek = CaculateEi(object, k)
    object.eCaches[k] = [k, Ek]


def ClipAlpha(aj, H, L):
    if (aj < L):
        aj = L
    if (aj > H):
        aj = H
    else:
        aj = aj
    return aj


def SelectJ(object, i, Ei):
    j = -1
    maxDelta = 0
    object.eCaches[i] = [i, Ei]
    validCacheList = np.where(object.eCaches[:, 0] != 0)[0]
    if (len(validCacheList) > 1):
        for k in validCacheList:
            if (i == k):
                continue
            Ek = CaculateEi(object, k)
            delta = abs(Ei - Ek)
            if (delta > maxDelta):
                maxDelta = delta
                j = k
        return j
    else:
        return SelectJdown(i, object.m)


def CaculateW(X, Y, alphas):
    m = X.shape[0]
    w = np.zeros(X.shape[1])
    for i in range(0, m):
        w += Y[i] * alphas[i] * X[i]

    return w


def InnerLoop(object, i):
    Ei = CaculateEi(object, i)
    if ((object.Y[i] * Ei < -object.xi) and (object.alphas[i] < object.C)):
        j = SelectJ(object, i, Ei)
        Ej = CaculateEi(object, j)
        i_old = object.alphas[i].copy()
        j_old = object.alphas[j].copy()

        if (object.Y[i] != object.Y[j]):
            L = max(0, j_old - i_old)
            H = min(object.C, object.C + j_old - i_old)
        else:
            L = max(0, i_old + j_old - object.C)
            H = min(object.C, i_old + j_old)
        if L == H:
            return 0

        eta = object.X[i] @ object.X[i].T + object.X[j] @ object.X[j] - 2 * object.X[i] @ object.X[j].T
        if eta == 0:
            return 0

        object.alphas[j] += object.Y[j] * (Ei - Ej) / eta
        object.alphas[j] = ClipAlpha(object.alphas[j], H, L)
        UpdateEk(object, j)

        if abs(object.alphas[j] - j_old) < 0.0001:
            return 0

        object.alphas[i] += object.Y[i] * object.Y[j] * (j_old - object.alphas[j])
        UpdateEk(object, i)
        b1 = - Ei - object.Y[i] * object.X[i] @ object.X[i].T * (object.alphas[i] - i_old) - object.Y[j] * object.X[
            j] @ object.X[i].T * (object.alphas[j] - j_old) + object.b
        b2 = - Ej - object.Y[i] * object.X[i] @ object.X[j].T * (object.alphas[i] - i_old) - object.Y[j] * object.X[
            j] @ object.X[
                 j].T * (object.alphas[j] - j_old) + object.b
        if object.alphas[i] > 0 and object.alphas[i] < object.C:
            object.b = b1
        elif object.alphas[j] > 0 and object.alphas[j] < object.C:
            object.b = b2
        else:
            object.b = (b1 + b2) / 2
        return 1

    return 0


def SMO(X, Y, C, xi, maxIter):
    object = SMOStruct(X, Y, C, xi)
    iters = 0
    changed = 0
    while iters < maxIter:
        changed = 0
        for i in range(0, object.m):
            changed += InnerLoop(object, i)
        if changed == 0:
            iters += 1
    return [object.alphas, object.b]


def loadtxtmethod(test_sample, test_sample_label):
    X = np.loadtxt(test_sample, dtype=np.float32, delimiter=' ')
    Y = np.loadtxt(test_sample_label, dtype=np.float32, delimiter=' ')
    return X, Y


# if __name__ == "__main__":
#     X, Y = loadtxtmethod('D:/CutExperiment/SVM/test_sample.txt', 'D:/CutExperiment/SVM/test_sample_label.txt')


"""
X = np.array(
        [[0,2,3],[2,0,4],[4.5,0,5],[4.5,3,4],[3,4.5,2],[2,1,6],
             [1.5,3,7],[4,4,8],[0,3.5,6],[3,2.5,4],[-1,-1,-2],[-3,-4.5,-4],
             [-2,-3,-6],[-4,-4,-4],[0,-2.5,7],[-1,-3.5,5],[-3.5,-1,-4],
             [0,-3.5,-5],[-3,-1,-3],[-4,0,5]])
print(X)
Y = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Y = Y.T
alphas, b = SMO(X, Y, 0.6, 0.0005, 40)
w = CaculateW(X, Y, alphas)

def figureSVM(X, Y, w, b, alphas, xi):
    class_1x = X[np.where(Y == 1)]
    class_2x = X[np.where(Y != 1)]

    plt.scatter(class_1x[:, 0].flatten(), class_1x[:, 1].flatten(), class_1x[:, 2].flatten())
    plt.scatter(class_2x[:, 0].flatten(), class_2x[:, 1].flatten(), class_2x[:, 1].flatten())
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(class_1x[:, 0].flatten(), class_1x[:, 1].flatten(), class_1x[:, 2].flatten(), color="red")
    ax.scatter3D(class_2x[:, 0].flatten(), class_2x[:, 1].flatten(), class_2x[:, 2].flatten(), color="green")

    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    x,y= np.meshgrid(x, y)
    z1=(-w[0] * x-w[1]*y- b) /w[2]

    surf = ax.plot_surface(x, y, z1,
                           linewidth=0, antialiased=False,)

    # Customize the z axis.
    ax.set_zlim(-6, 8)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, aspect=5)



    plt.title("SVM plot")
    plt.show()
  
    x = np.arange(-4, 4, 0.1)
    y = np.arange(-4, 4, 0.1)
    z = np.arange(-4, 4, 0.1)
    yy1 = (-w[0] * xx - b) / w[1]
    yy2 = (-w[0] * xx - b - 1 - xi) / w[1]
    yy3 = (-w[0] * xx - b + 1 + xi) / w[1]
    plt.plot(xx, yy1.T,color=np.array([0,1,2])/5.)
    plt.plot(xx, yy2.T,'k--')
    plt.plot(xx, yy3.T,'k--')

    plt.show()





figureSVM(X, Y, w, b, alphas, 0.0005)
"""
