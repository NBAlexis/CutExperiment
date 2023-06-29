
"""

"""
import os

from Applications.jjvvgqgc.jjvvfunctions import PTMissing1500, PTMissing
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import JetNumberCut
from CutAndExport.FilterFunctions import Mjj2Filter, Yjj2Filter
from CutAndExport.Histogram import HistogramWithMinMax
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../_DataFolder/jjvv/Feature")

sm_1500 = LoadLHCOlympics("sm15000.lhco")
fgt0_1500 = LoadLHCOlympics("FgT0-15000.lhco")
fgt1_1500 = LoadLHCOlympics("FgT1-15000.lhco")
fgt2_1500 = LoadLHCOlympics("FgT2-15000.lhco")
fgt3_1500 = LoadLHCOlympics("FgT3-15000.lhco")

print(sm_1500.GetEventCount())
print(fgt0_1500.GetEventCount())
print(fgt1_1500.GetEventCount())
print(fgt2_1500.GetEventCount())
print(fgt3_1500.GetEventCount())

jetnumberCut = JetNumberCut(1, [2])

CutEvents(sm_1500, jetnumberCut)
CutEvents(fgt0_1500, jetnumberCut)
CutEvents(fgt1_1500, jetnumberCut)
CutEvents(fgt2_1500, jetnumberCut)
CutEvents(fgt3_1500, jetnumberCut)

print(sm_1500.GetEventCount())
print(fgt0_1500.GetEventCount())
print(fgt1_1500.GetEventCount())
print(fgt2_1500.GetEventCount())
print(fgt3_1500.GetEventCount())

"""
==============================================
mjj
==============================================
"""

sm_1500_mjj = HistogramWithMinMax(sm_1500, Mjj2Filter, [0, 15000], 50)
fgt0_1500_mjj = HistogramWithMinMax(fgt0_1500, Mjj2Filter, [0, 15000], 50)
fgt1_1500_mjj = HistogramWithMinMax(fgt1_1500, Mjj2Filter, [0, 15000], 50)
fgt2_1500_mjj = HistogramWithMinMax(fgt2_1500, Mjj2Filter, [0, 15000], 50)
fgt3_1500_mjj = HistogramWithMinMax(fgt3_1500, Mjj2Filter, [0, 15000], 50)

print(sm_1500_mjj.listCount)
print(fgt0_1500_mjj.listCount)
print(fgt1_1500_mjj.listCount)
print(fgt2_1500_mjj.listCount)
print(fgt3_1500_mjj.listCount)

"""
==============================================
yjj
==============================================
"""

sm_1500_yjj = HistogramWithMinMax(sm_1500, Yjj2Filter, [0, 6], 50)
fgt0_1500_yjj = HistogramWithMinMax(fgt0_1500, Yjj2Filter, [0, 6], 50)
fgt1_1500_yjj = HistogramWithMinMax(fgt1_1500, Yjj2Filter, [0, 6], 50)
fgt2_1500_yjj = HistogramWithMinMax(fgt2_1500, Yjj2Filter, [0, 6], 50)
fgt3_1500_yjj = HistogramWithMinMax(fgt3_1500, Yjj2Filter, [0, 6], 50)

print(sm_1500_yjj.listCount)
print(fgt0_1500_yjj.listCount)
print(fgt1_1500_yjj.listCount)
print(fgt2_1500_yjj.listCount)
print(fgt3_1500_yjj.listCount)

"""
==============================================
pt missing
==============================================
"""

sm_1500_ptm = HistogramWithMinMax(sm_1500, PTMissing, [0, 12000], 50)
fgt0_1500_ptm = HistogramWithMinMax(fgt0_1500, PTMissing, [0, 12000], 50)
fgt1_1500_ptm = HistogramWithMinMax(fgt1_1500, PTMissing, [0, 12000], 50)
fgt2_1500_ptm = HistogramWithMinMax(fgt2_1500, PTMissing, [0, 12000], 50)
fgt3_1500_ptm = HistogramWithMinMax(fgt3_1500, PTMissing, [0, 12000], 50)

print(sm_1500_ptm.listCount)
print(fgt0_1500_ptm.listCount)
print(fgt1_1500_ptm.listCount)
print(fgt2_1500_ptm.listCount)
print(fgt3_1500_ptm.listCount)

"""
1500 data:

1000000
300000
300000
300000
300000
832056
299961
297833
299347
298200

0-2500
[36636, 754264, 24361, 5448, 2875, 1869, 1226, 859, 695, 558, 445, 356, 284, 250, 191, 183, 148, 137, 105, 93, 92, 68, 58, 50, 58, 49, 29, 40, 37, 30, 30, 35, 29, 25, 25, 19, 18, 17, 22, 12, 29, 16, 21, 21, 16, 14, 21, 23, 23, 19]
[83, 381, 658, 877, 1139, 1398, 1572, 1781, 1910, 2145, 2346, 2722, 3242, 3972, 4584, 5237, 6022, 6729, 7632, 8345, 9038, 9919, 10704, 11264, 11834, 11808, 12120, 12173, 12223, 11847, 11557, 11011, 10689, 10345, 9723, 8947, 8327, 7483, 6940, 6368, 5699, 5007, 4396, 3851, 3169, 2601, 2113, 1704, 1262, 1057]
[102, 411, 851, 1369, 2105, 3003, 3908, 4699, 5231, 5550, 5880, 6265, 6594, 6813, 7308, 7556, 8025, 8389, 8878, 9096, 9406, 9531, 9973, 9943, 10094, 9957, 9692, 9866, 9549, 9256, 8748, 8587, 8078, 7662, 7168, 6743, 6206, 5793, 5229, 4873, 4358, 3922, 3396, 3122, 2761, 2427, 2055, 1797, 1452, 1164]
[70, 368, 665, 1021, 1293, 1763, 2139, 2524, 2835, 2993, 3284, 3627, 4130, 4557, 5128, 5617, 6261, 6820, 7522, 8085, 9001, 9481, 9889, 10490, 10638, 11040, 11001, 11206, 11277, 11068, 10708, 10424, 9910, 9440, 9081, 8325, 7984, 7414, 6806, 6254, 5628, 5132, 4471, 3978, 3544, 3061, 2686, 2082, 1741, 1370]
[60, 350, 717, 1194, 1870, 2742, 3427, 4339, 4647, 4955, 5204, 5629, 6060, 6458, 6798, 7274, 7549, 8110, 8432, 9031, 9449, 9634, 9872, 9894, 10101, 10289, 10209, 10353, 10087, 9618, 9341, 8886, 8422, 8238, 7580, 7015, 6754, 6255, 5637, 5201, 4733, 4135, 3741, 3326, 2942, 2452, 1993, 1692, 1478, 1197]
0-6
[88259, 88793, 88057, 89042, 87331, 79598, 68711, 55970, 44536, 35942, 27798, 21554, 16080, 11631, 8452, 5816, 4193, 2847, 1953, 1256, 823, 581, 414, 357, 278, 218, 213, 174, 150, 150, 118, 107, 94, 81, 65, 63, 47, 49, 33, 36, 28, 31, 13, 17, 10, 18, 9, 14, 6, 6]
[19655, 19448, 19345, 19189, 18471, 17806, 16946, 15695, 14863, 13797, 12710, 12084, 10855, 9977, 9194, 8487, 7654, 6610, 6051, 5462, 4753, 4156, 3748, 3360, 2904, 2452, 2226, 1930, 1601, 1418, 1212, 1073, 839, 720, 596, 514, 441, 353, 254, 215, 161, 160, 130, 101, 77, 56, 47, 46, 27, 25]
[15047, 15347, 15484, 16266, 16935, 16258, 15805, 15048, 14291, 13864, 13174, 12612, 11929, 11029, 10206, 9131, 8609, 7863, 7059, 6343, 5723, 5129, 4594, 4138, 3713, 3103, 2722, 2374, 2117, 1836, 1595, 1355, 1160, 994, 876, 746, 553, 499, 393, 339, 297, 242, 226, 195, 117, 117, 85, 73, 45, 38]
[15961, 15930, 15955, 16534, 16550, 16363, 15474, 14900, 14248, 13655, 12882, 12298, 11578, 10872, 9940, 9446, 8545, 7783, 7104, 6586, 5818, 5267, 4581, 4143, 3657, 3307, 2910, 2513, 2219, 1882, 1651, 1394, 1205, 1063, 849, 711, 660, 551, 435, 376, 315, 230, 188, 165, 133, 119, 91, 72, 63, 40]
[18214, 18085, 18208, 18662, 18661, 17792, 17045, 15689, 14708, 13835, 12598, 11837, 10833, 10068, 9277, 8375, 7557, 6827, 6112, 5480, 4897, 4369, 3828, 3457, 3042, 2590, 2330, 2038, 1798, 1538, 1287, 1142, 971, 870, 703, 605, 454, 445, 392, 302, 225, 213, 161, 164, 118, 74, 69, 59, 43, 34]
0-1000
[55025, 98968, 101859, 88628, 74701, 65034, 56152, 48458, 41224, 35757, 30226, 25492, 21497, 17899, 14185, 11343, 8774, 6751, 5100, 3633, 2803, 2154, 1615, 1296, 971, 794, 642, 491, 383, 340, 262, 218, 169, 169, 128, 111, 98, 78, 58, 59, 51, 50, 31, 29, 24, 16, 20, 22, 20, 12]
[1115, 2926, 4333, 5573, 6671, 7330, 7921, 8280, 8489, 8531, 8654, 8565, 8576, 8354, 8225, 8087, 8021, 7927, 7646, 7551, 7223, 7040, 6992, 6918, 6538, 6503, 6277, 6083, 5909, 5729, 5562, 5364, 5229, 4999, 4846, 4705, 4466, 4314, 4053, 3912, 3815, 3592, 3233, 3201, 3086, 2761, 2578, 2437, 2203, 2148]
[752, 2051, 3295, 4315, 5035, 5506, 5913, 6152, 6250, 6332, 6222, 6066, 6101, 6011, 5956, 5791, 5719, 5530, 5556, 5341, 5292, 5432, 5036, 5120, 4973, 4962, 4794, 4958, 4907, 4799, 4842, 4788, 4709, 4826, 4558, 4576, 4582, 4644, 4520, 4491, 4428, 4492, 4342, 4258, 4301, 4174, 4149, 4015, 3916, 3866]
[1007, 2946, 4607, 5891, 6965, 7380, 7995, 8244, 8423, 8241, 8273, 8115, 8040, 7878, 7694, 7414, 7176, 7038, 6800, 6725, 6699, 6378, 6157, 5998, 5875, 5712, 5569, 5383, 5306, 5158, 5092, 4873, 4664, 4429, 4515, 4410, 4287, 4056, 3936, 3836, 3764, 3538, 3486, 3443, 3273, 3104, 2981, 2809, 2615, 2578]
[712, 1945, 3231, 4217, 5122, 5790, 6025, 6248, 6473, 6501, 6491, 6517, 6293, 6441, 6181, 6230, 6097, 6041, 5867, 5800, 5631, 5414, 5509, 5467, 5297, 5317, 5304, 5209, 5095, 5132, 4950, 5009, 4813, 4832, 4726, 4691, 4589, 4601, 4527, 4529, 4243, 4276, 4272, 4266, 4064, 4045, 3812, 3800, 3842, 3665]

Process finished with exit code 0


5000：

1000000
300000
300000
300000
300000
819281
299996
298704
299683
298940
0-4000
[247966, 552298, 7278, 3439, 2008, 1337, 928, 704, 500, 423, 344, 235, 226, 205, 166, 129, 122, 101, 83, 92, 69, 63, 57, 45, 33, 35, 30, 28, 24, 19, 17, 18, 31, 13, 9, 7, 6, 5, 8, 10, 6, 14, 9, 14, 5, 7, 4, 2, 3, 6]
[33, 110, 206, 244, 335, 331, 320, 383, 406, 448, 450, 497, 546, 527, 610, 617, 668, 704, 760, 788, 875, 959, 1068, 1194, 1268, 1426, 1504, 1556, 1759, 1858, 2142, 2245, 2400, 2574, 2728, 2847, 3118, 3394, 3386, 3694, 3790, 4127, 4290, 4470, 4588, 4879, 4979, 4991, 5188, 5321]
[31, 105, 171, 272, 328, 396, 427, 502, 606, 725, 841, 997, 1134, 1340, 1406, 1632, 1603, 1667, 1746, 1754, 1924, 2008, 1985, 2003, 2127, 2177, 2210, 2360, 2351, 2550, 2676, 2755, 2790, 2887, 3038, 2978, 3268, 3255, 3459, 3610, 3630, 3556, 3834, 3996, 4030, 4118, 4196, 4169, 4455, 4434]
[28, 115, 173, 272, 293, 325, 318, 398, 414, 477, 509, 614, 663, 713, 750, 776, 803, 834, 869, 951, 1083, 1113, 1156, 1197, 1322, 1370, 1435, 1590, 1690, 1843, 1933, 2045, 2201, 2384, 2466, 2579, 2825, 2937, 3234, 3273, 3407, 3599, 3762, 3816, 3982, 4113, 4274, 4403, 4542, 4619]
[24, 90, 175, 221, 290, 348, 415, 459, 535, 593, 741, 875, 1029, 1134, 1241, 1400, 1491, 1473, 1631, 1548, 1679, 1760, 1794, 1886, 2000, 1960, 2157, 2191, 2259, 2369, 2494, 2608, 2739, 2796, 2823, 2976, 3174, 3265, 3468, 3469, 3757, 3787, 3781, 3937, 4035, 4152, 4249, 4318, 4479, 4506]
0-6
[88225, 87776, 88369, 91063, 87415, 79532, 66919, 54532, 43095, 34218, 26185, 19820, 14728, 10715, 7519, 5342, 3693, 2567, 1732, 1156, 809, 614, 425, 364, 290, 278, 211, 198, 184, 161, 146, 113, 104, 106, 101, 93, 58, 62, 50, 41, 38, 40, 29, 24, 18, 21, 16, 13, 16, 10]
[19187, 19153, 18714, 18742, 18191, 17503, 16543, 15650, 14573, 13701, 12698, 11756, 10816, 10004, 9259, 8354, 7496, 6792, 6202, 5471, 4948, 4344, 3775, 3436, 2900, 2660, 2279, 1986, 1861, 1565, 1383, 1211, 1070, 880, 704, 645, 598, 468, 395, 330, 276, 241, 217, 182, 131, 110, 124, 83, 79, 54]
[12653, 12933, 13152, 13712, 14137, 14186, 13557, 13648, 13341, 13123, 12828, 12287, 11953, 11346, 10830, 10311, 9517, 8635, 8173, 7447, 6910, 6302, 5569, 4982, 4534, 4136, 3592, 3214, 2828, 2519, 2252, 1923, 1680, 1476, 1281, 1136, 1035, 809, 765, 672, 567, 397, 385, 305, 278, 230, 215, 157, 150, 106]
[14527, 14465, 14619, 14944, 14842, 14759, 14421, 14093, 13627, 13343, 12801, 12216, 11412, 11056, 10262, 9776, 8853, 8284, 7736, 6953, 6503, 5648, 5330, 4685, 4270, 3777, 3429, 3023, 2617, 2334, 2050, 1787, 1535, 1421, 1207, 1011, 936, 777, 642, 564, 462, 448, 357, 277, 262, 221, 196, 149, 136, 144]
[15818, 16064, 16034, 16389, 16568, 16032, 15113, 14425, 13647, 13299, 12724, 11894, 11221, 10619, 9690, 9110, 8241, 7697, 7042, 6537, 5805, 5208, 4756, 4264, 3711, 3342, 2987, 2643, 2325, 2057, 1811, 1598, 1396, 1265, 1075, 948, 795, 715, 620, 536, 435, 393, 346, 316, 222, 211, 171, 136, 115, 112]
0-4000
[322270, 190803, 111413, 60034, 25451, 9943, 4284, 2123, 1155, 629, 375, 219, 169, 121, 81, 55, 37, 23, 27, 24, 16, 14, 9, 12, 10, 5, 6, 7, 2, 4, 2, 4, 6, 2, 1, 3, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[4872, 11908, 15780, 16502, 16479, 16000, 14814, 13782, 13004, 11914, 10976, 10153, 9551, 9018, 8371, 7828, 7376, 6906, 6524, 6163, 5971, 5647, 5378, 4962, 4653, 4510, 4146, 3954, 3722, 3480, 3348, 3166, 2966, 2786, 2646, 2407, 2276, 2020, 1858, 1762, 1492, 1380, 1222, 1081, 1012, 823, 673, 622, 494, 398]
[4193, 10240, 13000, 13791, 13350, 12792, 11791, 11044, 10069, 9307, 8450, 8190, 7437, 7067, 6636, 6454, 6050, 5771, 5514, 5307, 5160, 4963, 4861, 4703, 4580, 4419, 4415, 4131, 4196, 4087, 4161, 4009, 3965, 3832, 3739, 3612, 3617, 3492, 3506, 3384, 3249, 3169, 3146, 2971, 2739, 2670, 2734, 2432, 2253, 2161]
[5195, 12625, 16194, 17171, 16768, 15583, 14762, 13610, 12364, 11225, 10434, 9730, 8746, 8386, 7557, 7237, 6662, 6339, 5998, 5707, 5344, 5106, 4798, 4595, 4434, 4148, 3882, 3670, 3594, 3406, 3236, 3081, 2867, 2888, 2742, 2512, 2398, 2312, 2073, 2051, 1856, 1809, 1635, 1623, 1469, 1294, 1217, 1080, 1022, 928]
[3961, 10277, 13051, 14226, 13952, 13294, 12283, 11251, 10512, 9910, 9061, 8436, 7837, 7497, 6799, 6644, 6293, 6116, 5880, 5439, 5268, 5109, 4912, 4760, 4611, 4507, 4531, 4271, 4146, 4016, 3962, 3795, 3684, 3738, 3557, 3489, 3403, 3435, 3211, 3072, 3069, 2864, 2851, 2492, 2581, 2422, 2280, 2129, 2001, 1905]

Process finished with exit code 0


7000:

1000000
300000
300000
300000
300000
817751
300000
298891
299706
299063
0-8000
[797512, 11245, 3496, 1700, 1038, 678, 464, 332, 239, 178, 130, 124, 80, 61, 61, 54, 33, 40, 35, 33, 22, 21, 18, 13, 9, 9, 13, 11, 9, 9, 7, 8, 4, 3, 2, 3, 3, 4, 2, 4, 4, 1, 2, 0, 3, 1, 0, 1, 4, 3]
[92, 271, 392, 444, 495, 539, 544, 596, 710, 730, 817, 877, 938, 1035, 1249, 1403, 1538, 1789, 1966, 2232, 2582, 2844, 3150, 3605, 3976, 4424, 4711, 5192, 5680, 5910, 6394, 6547, 6928, 7255, 7622, 7837, 7919, 8185, 8171, 8284, 8416, 8274, 8352, 8296, 7983, 7819, 7919, 7558, 7389, 7148]
[66, 230, 375, 483, 618, 775, 900, 1218, 1327, 1610, 2021, 2164, 2308, 2346, 2486, 2523, 2582, 2769, 2960, 3063, 3228, 3527, 3717, 3970, 4222, 4268, 4474, 4780, 4874, 5085, 5188, 5530, 5710, 5769, 6060, 6388, 6326, 6569, 6678, 6677, 6868, 6751, 6623, 6691, 6720, 6693, 6578, 6409, 6371, 6286]
[69, 228, 377, 405, 476, 553, 623, 707, 761, 934, 964, 1157, 1116, 1252, 1411, 1475, 1585, 1789, 2102, 2141, 2430, 2667, 2931, 3116, 3414, 3766, 4019, 4367, 4663, 5079, 5281, 5758, 5825, 6338, 6550, 6596, 7138, 7099, 7397, 7314, 7624, 7415, 7505, 7583, 7642, 7312, 7347, 7147, 7219, 6977]
[75, 215, 362, 422, 552, 660, 850, 994, 1198, 1537, 1684, 1855, 2014, 2114, 2309, 2375, 2454, 2575, 2771, 2943, 3120, 3330, 3518, 3771, 4029, 4084, 4492, 4711, 4988, 5262, 5432, 5739, 5963, 6128, 6270, 6540, 6509, 6803, 6858, 6937, 7021, 6993, 7091, 6976, 6717, 6756, 6678, 6655, 6557, 6403]
0-6
[88608, 88585, 88283, 91395, 87811, 79557, 67277, 54088, 42965, 33542, 25767, 19302, 14050, 10254, 7269, 5315, 3542, 2428, 1711, 1166, 878, 609, 445, 344, 285, 285, 258, 216, 188, 148, 145, 112, 105, 119, 90, 88, 64, 70, 47, 42, 47, 29, 29, 28, 28, 21, 23, 11, 13, 6]
[19331, 19278, 18794, 18495, 17955, 17238, 16766, 15566, 14444, 13799, 12658, 11708, 10766, 9892, 9059, 8355, 7535, 6947, 5976, 5437, 5049, 4429, 3857, 3469, 2981, 2744, 2371, 2033, 1822, 1590, 1385, 1228, 1006, 888, 794, 671, 548, 494, 402, 392, 296, 244, 232, 189, 146, 116, 97, 82, 79, 66]
[12093, 12007, 12584, 13123, 13622, 13804, 13586, 13520, 13231, 12963, 12788, 12391, 11884, 11380, 10906, 10204, 9802, 9132, 8350, 7586, 7242, 6446, 5951, 5210, 4664, 4232, 3785, 3302, 3036, 2523, 2277, 2041, 1759, 1599, 1353, 1294, 1070, 911, 761, 725, 599, 500, 392, 357, 314, 262, 235, 173, 155, 140]
[14244, 14304, 14566, 14588, 14720, 14341, 14151, 13988, 13649, 12793, 12569, 12052, 11567, 10891, 10393, 9714, 9011, 8523, 7898, 7137, 6407, 5915, 5344, 4818, 4428, 3791, 3312, 3143, 2862, 2513, 2109, 1955, 1626, 1411, 1255, 1040, 943, 845, 728, 625, 565, 462, 351, 349, 298, 227, 205, 171, 156, 135]
[15562, 15488, 15563, 15929, 15754, 15487, 14850, 14289, 13671, 13002, 12701, 12070, 11132, 10498, 9961, 9361, 8637, 7787, 7065, 6588, 5984, 5357, 4878, 4418, 4086, 3549, 3200, 2831, 2479, 2248, 1982, 1810, 1390, 1346, 1153, 1015, 852, 771, 640, 596, 444, 408, 338, 298, 231, 245, 186, 161, 134, 106]
0-6000
[411238, 182576, 72094, 19355, 5489, 2037, 938, 436, 257, 167, 100, 65, 63, 39, 29, 14, 14, 8, 6, 6, 9, 6, 3, 4, 1, 1, 3, 1, 2, 1, 1, 2, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[7449, 16829, 20118, 20287, 18742, 17289, 15798, 14324, 13079, 11903, 10932, 9866, 9117, 8586, 7753, 7321, 6880, 6292, 5986, 5723, 5321, 4956, 4800, 4428, 4215, 3987, 3513, 3447, 3255, 3046, 2787, 2576, 2425, 2152, 2024, 1838, 1678, 1496, 1245, 1142, 953, 849, 721, 659, 555, 426, 336, 270, 226, 144]
[6346, 14397, 16957, 17032, 15828, 14138, 12883, 11603, 10433, 9407, 8479, 7979, 7354, 6888, 6512, 6151, 5839, 5524, 5368, 4932, 4860, 4597, 4572, 4573, 4318, 4260, 4181, 3968, 4119, 3945, 3806, 3711, 3651, 3662, 3449, 3339, 3281, 3228, 3181, 3078, 2862, 2767, 2572, 2528, 2291, 2226, 1966, 1837, 1659, 1477]
[7805, 17366, 20650, 20326, 18961, 17010, 15632, 13985, 12636, 11232, 10243, 9414, 8486, 7894, 7294, 6828, 6352, 5914, 5493, 5166, 4829, 4545, 4438, 4038, 3873, 3613, 3395, 3320, 3159, 3030, 2804, 2631, 2486, 2350, 2258, 2058, 1987, 1821, 1670, 1598, 1423, 1310, 1199, 1147, 1007, 848, 746, 674, 630, 523]
[6336, 14740, 17371, 17571, 16033, 14564, 13337, 12053, 10935, 10156, 9204, 8362, 7734, 7305, 6775, 6417, 5963, 5702, 5505, 5159, 4933, 4833, 4616, 4442, 4266, 4127, 3980, 4034, 3836, 3876, 3695, 3608, 3472, 3336, 3145, 3088, 2930, 2891, 2759, 2664, 2530, 2469, 2254, 2164, 2042, 1883, 1733, 1493, 1445, 1234]

Process finished with exit code 0


15000:

1000000
300000
300000
300000
300000
812332
299999
299170
299801
299355
0-15000
[801878, 5921, 1900, 873, 513, 317, 217, 152, 113, 82, 56, 48, 32, 32, 27, 20, 14, 13, 8, 11, 13, 17, 9, 7, 3, 3, 3, 6, 2, 3, 2, 0, 1, 2, 4, 2, 0, 0, 2, 1, 3, 2, 1, 1, 1, 0, 3, 0, 1, 1]
[86, 210, 311, 357, 392, 389, 404, 470, 488, 555, 565, 611, 627, 719, 765, 830, 989, 1042, 1315, 1335, 1542, 1741, 1939, 2207, 2451, 2784, 2911, 3137, 3538, 3704, 4151, 4350, 4578, 4963, 5273, 5512, 5798, 5995, 6435, 6384, 6622, 6784, 6854, 7025, 7150, 7219, 7334, 7245, 7254, 7239]
[75, 226, 313, 421, 445, 503, 566, 661, 809, 983, 1036, 1267, 1328, 1523, 1517, 1577, 1705, 1835, 1861, 1963, 2061, 2241, 2286, 2497, 2563, 2715, 2811, 3075, 3179, 3352, 3559, 3648, 3925, 4088, 4127, 4326, 4590, 4713, 4913, 5052, 5085, 5373, 5451, 5572, 5603, 5651, 5766, 5874, 6045, 5909]
[73, 200, 251, 315, 328, 390, 424, 434, 499, 547, 566, 653, 695, 746, 874, 871, 1028, 1098, 1185, 1287, 1427, 1542, 1684, 1895, 2016, 2295, 2503, 2600, 2869, 3074, 3344, 3566, 3810, 4100, 4308, 4596, 4840, 5125, 5187, 5411, 5581, 5877, 5948, 6116, 6240, 6359, 6502, 6546, 6616, 6458]
[65, 185, 277, 340, 368, 427, 479, 591, 696, 837, 983, 1161, 1205, 1333, 1390, 1424, 1537, 1686, 1706, 1819, 1931, 2044, 2282, 2376, 2510, 2706, 2795, 2968, 3117, 3341, 3567, 3699, 3945, 4128, 4465, 4475, 4692, 4990, 5036, 5233, 5390, 5555, 5729, 5860, 6027, 5962, 6228, 6164, 6081, 6093]
0-6
[89931, 89152, 89834, 93074, 88689, 79503, 66658, 52504, 41271, 31983, 24397, 18269, 13154, 9672, 6822, 4698, 3311, 2212, 1602, 1094, 791, 517, 408, 322, 332, 266, 211, 219, 177, 165, 134, 125, 110, 91, 99, 77, 52, 60, 37, 44, 33, 32, 36, 24, 23, 18, 16, 14, 5, 6]
[19320, 18956, 18463, 18748, 17757, 17395, 16251, 15508, 14495, 13382, 12564, 11714, 10771, 9877, 9209, 8273, 7514, 6836, 6080, 5534, 4990, 4364, 3976, 3517, 3094, 2759, 2434, 2071, 1961, 1645, 1388, 1266, 1177, 928, 839, 673, 639, 565, 482, 410, 352, 262, 238, 192, 173, 147, 143, 104, 86, 66]
[11198, 11142, 11747, 12202, 12550, 12829, 12791, 12856, 12746, 12613, 12634, 12235, 12041, 11607, 11204, 10524, 10004, 9351, 8694, 7940, 7456, 6901, 6169, 5745, 5151, 4623, 4018, 3725, 3300, 2825, 2610, 2309, 1978, 1749, 1596, 1374, 1186, 1057, 951, 796, 634, 648, 576, 467, 352, 313, 277, 222, 209, 172]
[13863, 13694, 13802, 14171, 14243, 13809, 13877, 13703, 13185, 12844, 12486, 12066, 11454, 11148, 10561, 9765, 9159, 8730, 7979, 7297, 6787, 5995, 5631, 4987, 4555, 4041, 3586, 3206, 2960, 2529, 2305, 2041, 1784, 1575, 1374, 1176, 988, 876, 769, 678, 634, 522, 436, 384, 316, 279, 255, 199, 183, 145]
[14664, 14577, 14740, 15008, 14985, 14641, 14306, 13781, 13551, 13015, 12309, 12079, 11320, 10684, 10179, 9652, 8689, 8069, 7606, 6808, 6389, 5714, 5321, 4633, 4316, 3841, 3470, 3085, 2716, 2475, 2129, 1906, 1724, 1524, 1283, 1111, 962, 865, 725, 657, 564, 472, 414, 363, 295, 271, 219, 196, 168, 149]
0-12000
[536177, 84050, 7536, 1505, 542, 244, 135, 74, 32, 33, 16, 12, 16, 5, 6, 9, 2, 1, 7, 2, 2, 3, 2, 2, 0, 1, 0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[11233, 22115, 24355, 22717, 20064, 18214, 15886, 14113, 12840, 11371, 10146, 9097, 8298, 7627, 7021, 6368, 5990, 5502, 5101, 4908, 4371, 4206, 4075, 3770, 3476, 3218, 3015, 2838, 2717, 2469, 2428, 2142, 1985, 1772, 1747, 1571, 1477, 1282, 1199, 1084, 1010, 823, 761, 637, 601, 480, 376, 331, 316, 226]
[9603, 19461, 21097, 19483, 17424, 15649, 13463, 12037, 10500, 9609, 8506, 7719, 6935, 6503, 6102, 5756, 5241, 4947, 4580, 4465, 4144, 4001, 3867, 3702, 3672, 3562, 3421, 3302, 3256, 3107, 3082, 2984, 2874, 2843, 2833, 2750, 2609, 2522, 2525, 2423, 2321, 2285, 2297, 2087, 1930, 1878, 1791, 1631, 1596, 1468]
[11146, 22507, 24205, 22639, 20629, 18028, 16037, 14090, 12164, 10873, 9548, 8762, 7987, 7156, 6697, 6048, 5534, 5252, 4861, 4404, 4136, 3852, 3648, 3480, 3228, 3057, 2897, 2754, 2562, 2509, 2363, 2167, 1949, 1947, 1731, 1668, 1651, 1517, 1462, 1376, 1252, 1260, 1091, 977, 902, 790, 768, 696, 624, 529]
[9706, 19483, 21348, 19987, 18189, 16094, 14126, 12378, 11088, 9720, 8661, 8116, 7133, 6695, 6216, 5895, 5495, 5078, 4826, 4500, 4355, 4096, 3985, 3842, 3643, 3411, 3414, 3212, 3120, 3036, 2939, 2862, 2876, 2594, 2655, 2488, 2437, 2373, 2237, 2141, 2169, 1982, 1874, 1832, 1760, 1674, 1541, 1428, 1303, 1271]

Process finished with exit code 0


"""