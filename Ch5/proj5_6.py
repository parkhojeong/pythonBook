inputList = [[line.split(',')[0],eval(line.split(',')[1].rstrip())] for line in open("Mileage.txt") ]
resDict ={}
print(inputList)
for i in range(len(inputList)):
    item = inputList[i] # 한줄 씩 item으로 저장 후 사용
    key = item[0]
    if resDict.get(key,-1) == -1:
        resDict[key] = (1,item[1])
    else:
        resDict[key]= (resDict[key][0]+1,resDict[key][1]+item[1] )


print(resDict)
for item in sorted(resDict.items(), key=lambda k: k[1][0]*100/k[1][1], reverse=True):
    MPG= item[1][0]*100/item[1][1]
    print("{0:<15s}{1:<15.2f}".format(item[0], MPG))
