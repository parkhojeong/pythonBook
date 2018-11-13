import pickle
def main():
    citiesDict = createDictFromBinaryFile("LargeCitiesDict.dat")
    stateName = inputStr()
    printLargeStates(citiesDict,stateName)

def createDictFromBinaryFile(filename):
    infile = open(filename,"rb")
    return pickle.load(infile)

def inputStr():
    return input("Enter the name of a state: ")

def printLargeStates(citiesDict, stateName):
    if citiesDict[stateName]:
        print("Large cities: ",end="")
        for item in citiesDict[stateName]:
            print(item,end=" ")
    else:
        print("There are no large cities in",stateName)

main()