def cleanEgyptDataForWebSite() :
    lists = []
    confermidCasesInEgypt = []
    deadCasesInEgypy = []
    recoveredCasesInEgypt = []
    datesOfCasesInEgypt = []
    with open('cleanedEgyptData.csv') as f: 
        temp = f.read().splitlines()
    for i in temp :
        lists.append(i.split())
    f.close()
    for i in range(len(lists)) :
        z = str(lists[i])
        z = z[2:-2].split(',')
        confermidCasesInEgypt.append(int(z[5]))
        deadCasesInEgypy.append(int(z[6]))
        recoveredCasesInEgypt.append(int(z[7]))
        t = z[4].split("/")
        datesOfCasesInEgypt.append(t[1] + "/" + t[0] + "/" + "2020")
    # print(datesOfCasesInEgypt)
    # print(confermidCasesInEgypt)
    # print(deadCasesInEgypy)
    # print(recoveredCasesInEgypt)

    f = open('js/data/EgyptData.js','w')
    f.write("let confermidCasesInEgypt = " + str(confermidCasesInEgypt) + ";\n") 
    f.write("let deadCasesInEgypy = " + str(deadCasesInEgypy) + ";\n")
    f.write("let recoveredCasesInEgypt = " + str(recoveredCasesInEgypt) + ";\n")
    f.write("let datesOfCasesInEgypt = " + str(datesOfCasesInEgypt) + ";\n")
    f.close() 