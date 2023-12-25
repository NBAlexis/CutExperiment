import random
import numpy as np

dataCount = 16384

folderHeader = "../../../_DataFolder/qkmeans/standard/"

def generateEvents(min, max, maxd, dataNumber, folder, fileOrignal, fileNormalized):
    p1 = np.array([[random.uniform(min, max) for _ in range(0, maxd)] for _ in range(0, dataNumber)])
    np.savetxt(folder + fileOrignal, p1, delimiter=',')
    d1 = np.transpose(np.array([np.sqrt(np.sum(p1 * p1, axis=1))]))
    p2 = np.hstack((p1, d1))
    m2 = np.mean(p2, axis=0)
    std2 = np.std(p2, axis=0)
    p3 = (p2 - m2) / std2
    n3 = np.sqrt(np.sum(p3 * p3, axis=1))
    p3 = np.transpose(p3)
    p3 = p3 / n3
    p3 = np.transpose(p3)
    np.savetxt(folder + fileNormalized, p3, delimiter=',')


generateEvents(-1.0, 1.0, 3, dataCount, folderHeader, "p3.csv", "q4.csv")
generateEvents(-1.0, 1.0, 7, dataCount, folderHeader, "p7.csv", "q8.csv")
generateEvents(-1.0, 1.0, 15, dataCount, folderHeader, "p15.csv", "q16.csv")
generateEvents(-1.0, 1.0, 31, dataCount, folderHeader, "p31.csv", "q32.csv")
generateEvents(-1.0, 1.0, 63, dataCount, folderHeader, "p63.csv", "q64.csv")
generateEvents(-1.0, 1.0, 127, dataCount, folderHeader, "p127.csv", "q128.csv")
generateEvents(-1.0, 1.0, 255, dataCount, folderHeader, "p255.csv", "q256.csv")
generateEvents(-1.0, 1.0, 511, dataCount, folderHeader, "p511.csv", "q512.csv")
generateEvents(-1.0, 1.0, 1023, dataCount, folderHeader, "p1023.csv", "q1024.csv")
