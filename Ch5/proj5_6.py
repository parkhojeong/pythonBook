file = open("Mileage.txt")
mDict = [[line.split(',')[0],eval(line.split(',')[1].rstrip())] for line in file ]
resDict ={}


print(mDict)
for i in range(len(mDict)):
    item = mDict[i]
    key = item[0]
    if resDict.get(key,-1) == -1:
        resDict[key] = (1,mDict[i][1])
    else:
        sumGallon = resDict[key][0] * resDict[key][1]+ mDict[i][1]
        cnt = resDict[key][0]+1
        avgGallon = sumGallon /cnt
        resDict[key] = (cnt,avgGallon)

print("{0:<15}{1:<15}".format("Model","MPG"))
for item in sorted(resDict.items(),key = lambda k : k[1][1],reverse= True):
    key = item[0]
    print("{0:<15s}{1:<15.2f}".format(key,resDict[key][1]))