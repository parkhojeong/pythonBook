file = open("Exchrate.txt")
rateDict = {line.split(',')[0]:{"currency":line.split(',')[1],"rate":line.split(',')[2]}
                for line in file}
# print(rateDict)

countryName = input("(a) Enter the name of a country: ")
print("Currency: {0:s} \nExchange rate: {1:.4f}"
      .format(rateDict[countryName]["currency"],eval(rateDict[countryName]["rate"])))

sortedRateDict = sorted(rateDict.items(), key= lambda k: k[1]["rate"])
print("\n(b)")
for item in sortedRateDict:
    if eval(item[1]["rate"]) < 1:
        print(item[0])
# print(sortedRateDict)


firstCountryName = input("\n(c) Enter name of first country: ")
secondCountryName = input("Enter name of second country: ")
amtOfMoney = float(input("Amount of money to convert: "))
resMoney = (1/eval(rateDict[firstCountryName]["rate"]))*\
           eval(rateDict[secondCountryName]["rate"])*amtOfMoney

print("{0:.2f} {1:s}s from {2:} equals {3:,.2f} {4:}s from {5:}"
      .format(amtOfMoney, rateDict[firstCountryName]["currency"].lower(), firstCountryName
              , resMoney, rateDict[secondCountryName]["currency"].lower(), secondCountryName))
