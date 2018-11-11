import pickle
def main():
    Dict = createDictFromBinaryFile("JusticesDict.dat")
    state = inputName()
    printAbbr(Dict,state)

def createDictFromBinaryFile(filename):
    infile = open(filename,'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def inputName():
    return input("Enter a state abbreviation: ")

def printAbbr(Dict,state):
    for key in Dict.keys():
        if Dict[key]["state"] == state:
            print("{0:20s}{1:d}".format(key,Dict[key]["yrAppt"]))

main()