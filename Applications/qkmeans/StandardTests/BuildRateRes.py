import numpy as np
from matplotlib import pyplot as plt

folderHeader = "../../../_DataFolder/qkmeans/buildratetest/"

br1 = np.loadtxt(folderHeader + "br2multi.csv", delimiter=',')
br1 = np.reshape(br1, (101, 101))
plt.imshow(br1)
plt.show()

