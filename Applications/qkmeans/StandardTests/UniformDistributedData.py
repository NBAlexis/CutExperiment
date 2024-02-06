import random
import numpy as np

dataCount = 5000

folderHeader = "../../../_DataFolder/qkmeans/standard/"

def generateEvents(min, max, maxd, dataNumber, folder, fileOrignal, fileNormalized):
    p1 = np.array([[random.uniform(min, max) for _ in range(0, maxd)] for _ in range(0, dataNumber)])
    np.savetxt(folder + fileOrignal, p1, delimiter=',')
    m1 = np.mean(p1, axis=0)
    std1 = np.std(p1, axis=0)
    p2 = (p1 - m1) / std1
    p2 = np.hstack((p2, np.ones((dataNumber, 1))))
    n2 = np.sqrt(np.sum(p2 * p2, axis=1))
    p3 = np.transpose(p2)
    p3 = p3 / n2
    p3 = np.transpose(p3)
    np.savetxt(folder + fileNormalized, p3, delimiter=',')


generateEvents(-1.0, 1.0, 7, dataCount, folderHeader, "p7.csv", "q8.csv")
generateEvents(-1.0, 1.0, 15, dataCount, folderHeader, "p15.csv", "q16.csv")
generateEvents(-1.0, 1.0, 31, dataCount, folderHeader, "p31.csv", "q32.csv")
generateEvents(-1.0, 1.0, 63, dataCount, folderHeader, "p63.csv", "q64.csv")
generateEvents(-1.0, 1.0, 127, dataCount, folderHeader, "p127.csv", "q128.csv")
generateEvents(-1.0, 1.0, 255, dataCount, folderHeader, "p255.csv", "q256.csv")
generateEvents(-1.0, 1.0, 511, dataCount, folderHeader, "p511.csv", "q512.csv")
generateEvents(-1.0, 1.0, 1023, dataCount, folderHeader, "p1023.csv", "q1024.csv")
