import numpy as np

folderHeader = "../../../_DataFolder/qkmeans/knn2d/"

pts1 = np.loadtxt(folderHeader + "p2dk4traing.csv", delimiter=',')
pts2 = np.loadtxt(folderHeader + "p2dk4test.csv", delimiter=',')

ptsall = np.vstack((pts1, pts2))

mins = np.min(ptsall, axis=0)
maxs = np.max(ptsall, axis=0)

pts1 = (pts1 - mins) / (maxs - mins)
pts1[:, 0] = pts1[:, 0] * np.pi / 2
pts1[:, 1] = pts1[:, 1] * np.pi

r1 = np.cos(pts1[:, 1]) * np.cos(pts1[:, 0])
r2 = np.sin(pts1[:, 1]) * np.cos(pts1[:, 0])
r3 = np.cos(pts1[:, 1]) * np.sin(pts1[:, 0])
r4 = np.sin(-pts1[:, 1]) * np.sin(pts1[:, 0])

r1 = np.transpose(np.array([r1]))
r2 = np.transpose(np.array([r2]))
r3 = np.transpose(np.array([r3]))
r4 = np.transpose(np.array([r4]))

rps = np.hstack((r1, r2, r3, r4))

folderHeader = "../../../_DataFolder/qkmeans/ad/"
np.savetxt(folderHeader + "p2dk4set.csv", rps, delimiter=',')
