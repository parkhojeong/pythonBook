file = open("Units.txt",'r')
fDict = {item.split(',')[0]:eval(item.split(',')[1].rstrip()) for item in file}


print("UNITS OF LENGTH")
i = 0
for key in fDict.keys():
    if (i)%3 ==0 and i!=0:
        print()
    print("{0:10s}".format(key),end="")
    i+=1
print()
unitFrom = input("Units to convert from: ")
unitTo = input("Units to convert to: ")
length = eval(input("Enter length in {}:".format(unitFrom)))
print("Length in {0:s}: {1:.4f}"
      .format(unitTo,fDict.get(unitFrom.lower(),1)*(1/fDict.get(unitTo.lower(),1))*length))