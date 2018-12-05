inputList = [[line.split(',')[0],eval(line.split(',')[1].rstrip())] for line in open("Mileage.txt") ]
resDict ={}
print(inputList)
for i in range(len(inputList)):
    item = inputList[i] # 한줄 씩 item으로 저장 후 사용
    key = item[0]
    if resDict.get(key,-1) == -1:
        resDict[key] = {"cnt":1,"sumGallon":item[1]}
    else:
        resDict[key]["cnt"]+=1
        resDict[key]["sumGallon"] = resDict[key]["sumGallon"]+item[1]

    resDict[key]["MPG"] = resDict[key]["cnt"] * 100 / resDict[key]["sumGallon"]

print("{0:<15}{1:<15}".format("Model","MPG"))
for item in sorted(resDict.items(),key = lambda k : k[1]["MPG"],reverse= True):
    key = item[0]
    print("{0:<15s}{1:<15.2f}".format(key,resDict[key]["MPG"]))