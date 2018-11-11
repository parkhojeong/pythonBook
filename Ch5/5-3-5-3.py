def main():
    nationSet = getDictionary("output.txt")
    printData(nationSet)

def getDictionary(fileName):
    infile = open(fileName, 'r')
    infile.readline()
    infile.readline()
    contList = getContList()

    nationSet = {}
    for line in infile:
        nation = ""
        list = line.split()
        i = 0
        area =list[-1]
        popl =list[-2]
        if list[-3]=="America":
            cont = list[-4]+" "+list[-3]
            i = -4
        else:
            cont = list[-3]
            i = -3
        for item in list[:i]:
            nation = nation+item+" "
        nationSet[nation]={"area":area,"popl":popl, "cont":cont}
    infile.close()
    return nationSet

def printData(nationSet):

    print("{0:<45s}{1:<20s}{2:<20s}{3:<20s}\n".format("Nation","Continent","Population","Area"))
    for nation in nationSet:
        cont = nationSet[nation]["cont"]
        popl = nationSet[nation]["popl"]
        area = nationSet[nation]["area"]
        print("{0:<45s}{1:<20s}{2:<20s}{3:<20s}".format(nation,cont,popl,area))

def getContList():
    return ["South","Europe","North","Africa","Asia","Australia/Oceania","North"]

main()

