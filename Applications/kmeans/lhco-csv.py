import os

from Applications.kmeans.kmeansfunctions import ChooseEventWithStratege
from Applications.kmeans.lhcoexport import SaveCSVFile
from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut
from DataStructure.EventSet import EventSet
from DataStructure.Particles import ParticleType
from Interfaces.LHCOlympics import LoadLHCOlympics

os.chdir("../../")





testEvent1 = LoadLHCOlympics("_DataFolder/triphoton/SM-7000.lhco")
testEvent2 = LoadLHCOlympics("_DataFolder/triphoton/FT0-7000.lhco")

PhotonNumberCut = PhotonNumberCut(1, [3])

CutEvents(testEvent1, PhotonNumberCut)
CutEvents(testEvent2, PhotonNumberCut)

resultList = ChooseEventWithStratege(testEvent1, 600000, 0)
resultList = resultList + ChooseEventWithStratege(testEvent2, 30000, 1)
SaveCSVFile("_DataFolder/kmeans/FT0-7000.csv", resultList)
print("FT0-7000.csv", " saved!")
