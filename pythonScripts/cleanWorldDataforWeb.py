def cleanWorldDataForWebSite () :
    world = []
    dates = []
    dates2 = []
    confirmedSum = []
    deathsSum = []
    recoveredSum = []
    with open('covid_19_clean_complete.csv') as f: 
        temp = f.read().splitlines()
    for i in range(1,len(temp)) :
        world.append(temp[i].split())
    f.close()

    for i in world :
        data = str(i).split(",")
        date = data[-4]
        if date not in dates :
            dates.append(date)
            confirmedSum.append(int(data[-3]))
            deathsSum.append(int(data[-2]))
            recoveredSum.append(int(data[-1][:-2]))
            t = str(dates[-1])
            t = t.split("/")
            # print(t)
            dates2.append(t[1] + "/" + t[0] + "/" + "2020")
        else :
            confirmedSum[-1] += int(data[-3])
            deathsSum[-1]    += int(data[-2])
            recoveredSum[-1] += int(data[-1][:-2])
    # print(dates)
    # print(confirmedSum)
    # print(deathsSum)
    # print(recoveredSum)
    f = open('js/data/worldData.js','w')
    f.write("let confermidCasesInTheWorld = " + str(confirmedSum) + ";\n") 
    f.write("let deadCasesInTheWorld = " + str(deathsSum) + ";\n")
    f.write("let recoveredCasesInTheWorld = " + str(recoveredSum) + ";\n")
    f.write("let datesOfCasesInTheWorld = " + str(dates2) + ";\n")
    f.close()
