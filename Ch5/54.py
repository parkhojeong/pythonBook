import pickle
def main():
    Dict = createDictFromBinaryFile("JusticesDict.dat")
    printAbbr(Dict)

def createDictFromBinaryFile(filename):
    infile = open(filename,'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

def printAbbr(Dict):
    resDict = {}
    for key in Dict.keys():
        state = Dict[key]["state"]
        resDict[state] = 0

    for key in Dict.keys():
        state = Dict[key]["state"]
        resDict[state] = resDict[state]+1

    print(len(resDict)," states have produced justices.")
    for key in sorted(resDict):
        print(key,":",resDict[key])
main()