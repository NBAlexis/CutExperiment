import numpy as np

from Interfaces.UsefulFunctions import HistogramStrict
counts = [335921, 335685, 335456, 335308, 334127, 334087, 334122, 333365, 333196, 333238, 333214, 333308, 333059, 333233, 333647, 333347, 334312, 334141, 334981, 335459, 336396, 320828]
crosses = [8.748779, 8.662495, 8.571247, 8.499948, 8.445656, 8.37835, 8.327999, 8.292839, 8.273086, 8.251527, 8.249646, 8.238043, 8.257455, 8.282612, 8.322343, 8.373476, 8.403988, 8.46645, 8.529048, 8.608382, 8.689725]

leftV = -0.05
rightV = 0.05
anomV = 0.65
distV = 1500
leftAll = []
rightAll = []
anomalAll = []
distAll = []
sumAll = []
crossAll = []
acsAll = []
gradientAll = []
leftV1 = [-0.08 + 0.002 * i for i in range(0, 35)]
for i in range(0, 21):
    if i == 10:
        fileName1 = "G:\\nTGCIF\\Trees\\sm-025-1-std.csv"
        fileName2 = "G:\\nTGCIF\\Trees\\s025-10-std.csv"
        mapFileName = "G:\\nTGCIF\\Maps\\sm-025-1-idx.csv"
        mapdistFileName = "G:\\nTGCIF\\Maps\\sm-025-1-dist.csv"
        denorm = [24.6036968911978, 24.602291307219588, 24.60092646932307, 24.60004389493471, 24.59298720108968,
                  24.59274775719783, 24.592957272170857, 24.588420859084493, 24.58740669983976, 24.587658787440535,
                  24.587514741273683, 24.588078862845617, 24.58658419316407, 24.587628778677978, 24.590111980647652,
                  24.588312866589945, 24.594094256351024, 24.59307099967978, 24.598092500607233, 24.600944355317736,
                  24.606522935296173]
        # 24.587292649771754, 24.585280698009036
        cn1 = 24.585280698009036
        cn2 = denorm[10]
    else:
        fileName1 = "G:\\nTGCIF\\Trees\\s025-{}-std.csv".format(i)
        fileName2 = "G:\\nTGCIF\\Trees\\s025-10-std.csv"
        mapFileName = "G:\\nTGCIF\\Maps\\s025-{}-idx.csv".format(i)
        mapdistFileName = "G:\\nTGCIF\\Maps\\s025-{}-dist.csv".format(i)
        denorm = [24.6036968911978, 24.602291307219588, 24.60092646932307, 24.60004389493471, 24.59298720108968,
                  24.59274775719783, 24.592957272170857, 24.588420859084493, 24.58740669983976, 24.587658787440535,
                  24.587514741273683, 24.588078862845617, 24.58658419316407, 24.587628778677978, 24.590111980647652,
                  24.588312866589945, 24.594094256351024, 24.59307099967978, 24.598092500607233, 24.600944355317736,
                  24.606522935296173]
        # 24.587292649771754, 24.585280698009036
        cn1 = denorm[i]
        # cnsm0 = 24.587292649771754
        cn2 = denorm[10]
    scoreData1 = np.loadtxt(fileName1, delimiter=',')
    scoreData2 = np.loadtxt(fileName2, delimiter=',')
    mapdData = np.loadtxt(mapFileName, delimiter=',').astype(int)
    mapddstData = np.loadtxt(mapdistFileName, delimiter=',')
    print("csv loaded :", i)
    scorefunc1 = lambda a: 2 ** (-a / cn1)
    vscorefunc1 = np.vectorize(scorefunc1)
    scorefunc2 = lambda a: 2 ** (-a / cn2)
    vscorefunc2 = np.vectorize(scorefunc2)
    smallp = mapdData[mapddstData > distV]
    print("dist > ", distV, " :", len(smallp))
    distAll.append(len(smallp))
    score1 = vscorefunc1(scoreData1[:, 1])
    score2 = vscorefunc1(scoreData2[:, 1])
    anSrc1 = score1[score1 > anomV]
    print(len(anSrc1))
    # anSrc2 = score2[score2 > 0.65]
    # print(len(anSrc2))
    anomalAll.append(len(anSrc1))
    diff = []
    for j in range(0, len(score1)):
        # print("{}/{}", i, len(score1))
        scoreMap = score1[j] - score2[mapdData[j]]
        diff.append(scoreMap)
    diffar = np.array(diff)
    gradient = []
    for th in leftV1:
        leftv = diffar[diffar < th]
        gradient.append(len(leftv) * 1000 * crosses[i] / 500000.0)
    gradientAll.append(gradient)
    # binmin = -0.1
    # binmax = 0.1
    # binsep = 40
    # histres1 = HistogramStrict(diff, binmin, binmax, binsep)
    # print(histres1.minMax)
    # print(histres1.listCount)
    # print(len(diff))
    print(np.mean(diffar))
    leftC = diffar[diffar < leftV]
    rightC = diffar[diffar > rightV]
    print(len(leftC), len(rightC))
    leftAll.append(len(leftC))
    rightAll.append(len(rightC))
    sumAll.append(len(leftC) + len(rightC))
    crossAll.append(1000.0 * len(leftC) * crosses[i] / 500000.0)
    acsAll.append(1000.0 * len(anSrc1) * crosses[i] / 500000.0)

print(leftAll)
print(rightAll)
# print(anomalAll)
# print(sumAll)
print(distAll)
print(crossAll)
print("anomal cs: ", acsAll)

print(gradientAll)

"""
7:
107
[-0.1, 0.1]
[0, 0, 1, 2, 4, 7, 9, 22, 42, 93, 143, 288, 594, 1158, 2476, 5450, 12524, 26759, 48429, 67320, 65648, 46679, 26865, 13809, 6877, 3403, 1900, 1052, 613, 380, 258, 151, 125, 89, 66, 50, 27, 10, 12, 11]
333365
0.0005116911809309878
2 17

8:
134
[-0.1, 0.1]
[0, 0, 2, 4, 2, 11, 6, 26, 44, 72, 140, 245, 480, 1019, 2085, 4671, 10632, 23686, 44905, 65602, 67884, 49934, 29898, 15650, 7544, 3798, 1979, 1070, 610, 423, 257, 157, 96, 83, 51, 43, 28, 23, 7, 9]
333196
0.0013281873016066665
1 19

9:
126
[-0.1, 0.1]
[0, 1, 0, 2, 3, 6, 10, 19, 44, 68, 135, 276, 474, 963, 1944, 4253, 9898, 22244, 43404, 64312, 68730, 51876, 31291, 16206, 7952, 4007, 2047, 1127, 656, 407, 288, 197, 117, 90, 55, 42, 24, 26, 15, 10]
333238
0.001716688202654305
1 18

sm:
139
[-0.1, 0.1]
[0, 1, 0, 1, 6, 7, 7, 13, 51, 66, 134, 279, 511, 1006, 2207, 4920, 11528, 25388, 47363, 67088, 66136, 48098, 28163, 14512, 7069, 3647, 1909, 1136, 677, 433, 267, 181, 106, 79, 53, 37, 29, 23, 16, 8]
333177
0.0009169533716780992
0 22

11:
137
136
[-0.1, 0.1]
[1, 1, 1, 1, 1, 2, 14, 26, 42, 69, 142, 242, 493, 960, 1975, 4242, 9869, 22065, 42742, 63953, 68806, 52642, 31697, 16309, 7856, 3932, 2013, 1185, 673, 452, 292, 196, 126, 93, 51, 47, 33, 24, 17, 7]
333308
0.0017866285897602207
1 15

12:
125
136
[-0.1, 0.1]
[0, 1, 0, 1, 5, 2, 11, 31, 53, 77, 121, 250, 521, 1026, 2048, 4706, 10848, 23766, 44976, 65284, 67172, 50536, 29663, 15153, 7537, 3794, 2121, 1187, 770, 470, 274, 202, 146, 97, 59, 50, 33, 27, 15, 6]
333059
0.0013686778452680541
1 19

13:
123
136
[-0.1, 0.1]
[0, 0, 0, 3, 5, 7, 6, 21, 31, 56, 158, 281, 492, 984, 2103, 4557, 10775, 24076, 45166, 65416, 67133, 49843, 29900, 15825, 7485, 3805, 2086, 1099, 677, 423, 254, 188, 130, 72, 48, 39, 28, 21, 17, 11]
333233
0.0013340571148983738
1 11

"""