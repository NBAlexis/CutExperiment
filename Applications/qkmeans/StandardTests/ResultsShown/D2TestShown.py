import os

import matplotlib.pyplot as plt
import numpy as np

os.chdir("../../../../_DataFolder/qkmeans/knn2d/")

res = np.loadtxt("d2test-100.csv", delimiter=',')
res = res[:, 1:4]
res = np.reshape(res, (100, 100, 3))
plt.imshow(res)
plt.show()
