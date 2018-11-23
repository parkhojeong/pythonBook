def main():
    list1 = fileRead("table.txt")
    arr,timeArr = dayParser(list1)
    teamList = fileRead("teamList.txt")
    teamList = teamParser(teamList)
    teamA,teamB,teamC,teamD,teamE = teamSeparte(arr,teamList)

    printTeam(teamA,"A",timeArr)
    printTeam(teamB,"B",timeArr)
    printTeam(teamC,"C",timeArr)
    printTeam(teamD, "D",timeArr)
    printTeam(teamE, "E",timeArr)
    # i = 0
    # for row in arr:
    #     print("{0:20s}".format(timeArr[i]), end=" ")
    #     print(sorted(row))
    #     i += 1

def fileRead(filename):
    file = open(filename,encoding="utf-8")
    list = [line.rstrip() for line in file]
    return list

def teamParser(teamList):
    tList = [item.split() for item in teamList]
#    print(tList)
    return tList

def dayParser(list1):
    arr = []
    time = []
    row = 0

    for line in list1:
        rowList = []
        items = line.split('"')
        time.append(items[0])
        col = 1

        while True:
             appendFlag = True
             tempList = []
             if col == len(items)-1:
                 break
             if items[col] == '\t':
                 appendFlag = False
                 pass
             else:
                 tempList.append(items[col])
             if appendFlag == True:
                 rowList.append(tempList)
             col += 1
        arr.append(rowList)
        row += 1

    i = 0
    arr2 =[]
    row2 = []
    for row in arr[:]:
        i+=1
        row2=[]
        for item in row:
            it = str(item[0]).split(", ")
            row2.append(it)
        arr2.append(row2)

    return arr2,time

def teamSeparte(arr,teamList):
    teamA= teamList[0]
    teamB= teamList[1]
    teamC =teamList[2]
    teamD =teamList[3]
    teamE =teamList[4]

    teamA = checkTeam(arr, teamList[0])
    teamB = checkTeam(arr,teamList[1])
    teamC = checkTeam(arr,teamList[2])
    teamD = checkTeam(arr, teamList[3])
    teamE = checkTeam(arr, teamList[4])

    return teamA, teamB, teamC, teamD, teamE

def checkTeam(arr,team):
    teamArr = []
    col = []
    row = []
    specialTime = []

    # for col in arr[0]:
    #     print(col)
    for rows in arr:
        row = []
        for col in rows:
            specialTime = []
            for id in col:
                if id in team:
                    specialTime.append(id)
            row.append(specialTime)
        teamArr.append(row)

    # for row in teamArr:
    #     print(sorted(row[:-1]))

    return teamArr

def printTeam(teamArr, teamname,timeArr):
    print(teamname)

    i = 0
    for row in teamArr:
        print(timeArr[i], end="  ")
        for col in row:

            print(sorted(col),end="   ")
        print()
        i += 1
    print()
main()