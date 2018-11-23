file = open("ALE.txt")
teamDict = {line.split(',')[0]:{"win":eval(line.split(',')[1]) ,"lost":eval(line.split(',')[2].rstrip())}
            for line in file}

teamDict = dict(sorted(teamDict.items(),key = lambda k: k[1]["win"],reverse=True))
print(teamDict)

for key in teamDict.keys():
    teamDict[key]["rate"]= teamDict[key]["win"]/(teamDict[key]["win"]+teamDict[key]["lost"])

print("{0:20}{1:10}{2:10}{3:10}".format("TEAM","WIN","LOST","RATE"))
for key in teamDict:
    print("{0:20}{1:<10}{2:1<0}{3:12.3f}"
          .format(key, teamDict[key]["win"],teamDict[key]["lost"] , teamDict[key]["rate"]))