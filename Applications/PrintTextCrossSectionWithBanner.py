from Interfaces.UsefulFunctions import BannerReader

filename = "../_DataFolder/qkmeans/jllvv/full/jjllall-{}-banner.txt"

paramlst = []
cslst = []
for i in range(11):
    res = BannerReader(filename.format(i), "fgt0")
    cslst.append(res[0])
    paramlst.append(res[1])

print(paramlst)
print(cslst)