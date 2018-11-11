import pickle
def main():
    presDict =createDictFromBinaryFile("USpresStatesDict.dat")
    firstName = inputName()
    findPresName(presDict,firstName)

def createDictFromBinaryFile(filename):
    infile = open(filename,"rb")
    presDict = pickle.load(infile)
    return presDict

def inputName():
    return input("Enter a first name: ")

def findPresName(presDict, firstName):
    printFlag = False

    for item in presDict.items():
        if item[0][1].startswith(firstName):
            print(item[0][1],item[0][0])
            printFlag = True

    if printFlag == False:
        print(firstName,"is not Exist.")

main()