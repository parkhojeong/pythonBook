file = open("Senate113.txt")
senateDict = {line.split(',')[0]:{"state":line.split(',')[1],"group":line.split(',')[2].rstrip()}
            for line in file}
file.close()

file = open("NewSen.txt")
newSenDict = {line.split(',')[0]:{"state":line.split(',')[1],"group":line.split(',')[2].rstrip()}
            for line in file}
file.close()

file = open("Retiredsen.txt")
retiredSenDict = {line.split(',')[0]:{"state":line.split(',')[1],"group":line.split(',')[2].rstrip()}
            for line in file}
file.close()

for key in senateDict:
    if key in newSenDict.keys():
        del senateDict[key]
senateDict.update(retiredSenDict)
rSum = dSum = iSum = 0
for key in senateDict:
    if senateDict[key]["group"] == 'R':
        rSum +=1
    elif senateDict[key]["group"] == 'D':
        dSum+=1
    else:
        iSum +=1

print("(b) Party Affiliations:","  Republicans: {}".format(rSum)
      ,"  Democrats: {}".format(dSum) ,"  Independents: {}".format(iSum),sep="\n")

twoStateSum = 0
twoStateSumDict = {}
prevState = senateDict[key]["state"]
# print(dict(sorted(senateDict.items(),key=lambda k:k[1]["state"])))
for key in dict(sorted(senateDict.items(),key=lambda k:k[1]["state"])):
    if twoStateSumDict.get(senateDict[key]["state"],-1) == -1:
        twoStateSumDict[senateDict[key]["state"]] = 1
    else:
        twoStateSumDict[senateDict[key]["state"]] += twoStateSumDict[senateDict[key]["state"]]
# print(sorted(twoStateSumDict.items()))
for key in twoStateSumDict:
    if twoStateSumDict[key] == 2 :
        twoStateSum +=1
print("\n(c) state number that has two person is {} states ".format(twoStateSum))

print("\n(d) ",end="")
stateName = input("Enter the name of a state: ")
for key in senateDict:
    if senateDict[key]["state"] == stateName:
        print(key)
