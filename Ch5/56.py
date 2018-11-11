import pickle

def main():
    list = createListFromTextFile("Rosebowl.txt")
    fun(list)

def createListFromTextFile(filename):
    infile = open("Rosebowl.txt","r")
    list = [line.rstrip() for line in infile]
    return list

def fun(list):
    teamDict = {}
    for value in list:
        teamDict[value] = 0
    for value in list:
        teamDict[value] = teamDict[value]+1
    print("Teams with four or more Rose Bowl wins as of 2014:")

    for nation in sorted(teamDict.items(),key=lambda k: k[1], reverse=True):
        print(nation[0], ": ",nation[1] , sep="")

def compareInt(number):
    return number

main()
