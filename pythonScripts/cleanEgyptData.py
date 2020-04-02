def GetEgyptData() :
    """
    this function is only responsible for collecting Egypt data from covid_19_clean_complete.csv 
    and save thim in cleanedData.csv
    """
    lists = []
    with open('covid_19_clean_complete.csv') as f: 
        temp = f.read().splitlines()
    for i in temp :
        lists.append(i.split())
    f.close()
    n = 0
    f = open('cleanedEgyptData.csv','w') 
    for i in range(len(lists)) :
        z = str(lists[i])
        if ',Egypt' in z :
            if n > 22 :
                f.write(str (n-23) + z[2:-2] + "\n")
            n += 1
    f.close() 

