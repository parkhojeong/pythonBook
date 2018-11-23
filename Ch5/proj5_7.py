file = open("Cities2.txt",encoding="UTF-8")

citiesDict = {line.split(',')[0]:
            {"state":line.split(',')[1],"2000Amt":eval(line.split(',')[2]),"2010Amt":eval(line.split(',')[3].rstrip())}
        for line in file}
file.close()

print(citiesDict)

for key in citiesDict.keys():
    citiesDict[key]["increaseRate"] = citiesDict[key]["2010Amt"]/citiesDict[key]["2000Amt"]

writeFile = open("CitiesRes.txt","w")
for item in citiesDict.items():
    key = item[0]
    st = "{0:},{1:},{2:},{3:},{4:.2f}\n".format(key,citiesDict[key]["state"],citiesDict[key]["2000Amt"],citiesDict[key]["2010Amt"],citiesDict[key]["increaseRate"])
    # writeFile.write(key)
    # writeFile.write(",")
    # writeFile.write(citiesDict[key]["state"])
    # writeFile.write(",")
    # writeFile.write(str(citiesDict[key]["2000Amt"]))
    # writeFile.write(",")
    # writeFile.write(str(citiesDict[key]["2010Amt"]))
    # writeFile.write(",")
    # writeFile.write("{0:.2f}".format(citiesDict[key]["increaseRate"]))
    writeFile.write(st)