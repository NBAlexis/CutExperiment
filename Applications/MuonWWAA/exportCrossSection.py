from Applications.MuonWWAA.exportFunctions import findLogTxt

folder1 = "../../_DataFolder/wwaa/crosssection/"
folder3 = "../../_DataFolder/wwaa/"

energies = ["3TeV", "10TeV", "14TeV", "30TeV"]
folderpostfix = ["3TeV", "10TeV", "14", "30"]
filepostfix = ["3", "10", "14", "30"]
energiesnumber = [3000.0, 10000.0, 14000.0, 30000.0]
combined = [False, False, False, True]

names = ["m2", "m3", "m4", "t0", "t1", "t2", "t5", "t6", "t7"]
paramNames = ["fm2", "fm3", "fm4", "ft0", "ft1", "ft2", "ft5", "ft6", "ft7"]

for i in range(len(energies)):
    # infoList = []
    # infoList.append(["filename", "n1", "n2", "cs", "coeff"])
    for j in range(len(names)):
        for k in range(11):
            eventToLoad = folder1 + "{}/{}-{}/{}-{}-{}.lhco".format(energies[i], names[j], folderpostfix[i], names[j], filepostfix[i], k + 1)
            print(eventToLoad)
            print("dealing with " + eventToLoad + " ......")
        if not combined[i]:
            lstA, lstB = findLogTxt(folder1 + "{}/{}-{}/scan_run_[01-11].txt".format(energies[i], names[j], folderpostfix[i]))
            print(lstA)
            print(lstB)
        else:
            lstA, lstB = findLogTxt(
                folder1 + "{}1/{}-{}/scan_run_[01-11].txt".format(energies[i], names[j], folderpostfix[i]))
            print(lstA)
            print(lstB)
            lstA, lstB = findLogTxt(
                folder1 + "{}2/{}-{}/scan_run_[01-11].txt".format(energies[i], names[j], folderpostfix[i]))
            print(lstA)
            print(lstB)

    # file = open(folder3 + "csv/" + energies[i] + "/" + "bgsignal/info.txt", 'w')
    # file.write("n1=event number before particle number cut\nn2=event number after particle number cut\ncs=cross-section before particle number cut(pb)\n")
    # file.write(str(np.array(infoList)))
    # file.close()




