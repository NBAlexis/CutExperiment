import os

from CutAndExport.CutEvent import CutEvents
from CutAndExport.CutFunctions import PhotonNumberCut, ETMissingCount
from Interfaces.LHCOlympics import LoadLHCOlympics, SaveToLHCO

os.chdir("../../")
threePhotn = PhotonNumberCut(1, [3])

for ots in ["FT5", "FT6", "FT7", "FT8", "FT9", "SM"]:
    for egs in ["1500", "5000", "7000", "8000", "15000"]:
        testEventNp = LoadLHCOlympics("_DataFolder/triphoton/{}-{}.lhco".format(ots, egs))
        print(ots, egs, "before", testEventNp.GetEventCount())
        CutEvents(testEventNp, threePhotn)
        print(ots, egs, "after", testEventNp.GetEventCount())
        SaveToLHCO("_DataFolder/triphoton/AfterPhotonNumber/{}-{}.lhco".format(ots, egs), testEventNp)

