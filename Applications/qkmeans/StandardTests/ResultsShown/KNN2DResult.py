import matplotlib
import matplotlib.pyplot as plt
import numpy as np

folderHeader = "../../../../_DataFolder/qkmeans/knn2d/"

testpoints = np.loadtxt(folderHeader + "d2testpoints.csv", delimiter=',')
clusters = np.loadtxt(folderHeader + "k2dtestres-32.csv", delimiter=',')

for i in range(0, 4):
    plt.scatter(testpoints[clusters==i,0], testpoints[clusters==i,1],
            s=1,
            color=matplotlib.colors.hsv_to_rgb([i / 4, 1.0, 1.0]))
plt.show()
