import os

import matplotlib.pyplot as plt
import numpy as np

os.chdir("../../../_DataFolder/qkmeans/knn2d")
res = np.loadtxt("validation-ae.csv", delimiter=',')

# """
type1 = np.argmax(res, axis=1)
type1 = np.reshape(type1, (200, 200))
plt.imshow(type1)
plt.show()
# """

"""
for k in range(16):
    type1 = res[:, k]
    type1 = np.reshape(type1, (200, 200))
    plt.imshow(type1)
    plt.show()
"""
