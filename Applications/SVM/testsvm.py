import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from Applications.SVM.svm import SMO, CaculateW

X = np.array(
        [[0,2,3],[2,0,4],[4.5,0,5],[4.5,3,4],[3,4.5,2],[2,1,6],
             [1.5,3,7],[4,4,8],[0,3.5,6],[3,2.5,4],[-1,-1,-2],[-3,-4.5,-4],
             [-2,-3,-6],[-4,-4,-4],[0,-2.5,7],[-1,-3.5,5],[-3.5,-1,-4],
             [0,-3.5,-5],[-3,-1,-3],[-4,0,5]])
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
"""   
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
"""




figureSVM(X, Y, w, b, alphas, 0.0005)