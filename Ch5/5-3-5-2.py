import pickle

def main():
    ## Display the data for an individual country.
    nations = getDictionary("UNdict.dat")
    writeData(nations)

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    nations = pickle.load(infile)
    infile.close()
    return nations

def writeData(nations):
    outfile = open("output.txt",'w')
    s = "{0:<45s}{1:<20s}{2:<20s}{3:<20s}\n"
    outfile.write(s.format("Nation","Continent","Population","Area"))
    for nation in nations:
        cont = nations[nation]["cont"]
        popl = nations[nation]["popl"]
        area = nations[nation]["area"]
        outfile.write('\n')
        outfile.write("{0:<45s}{1:<20s}{2:<20.2f}{3:<20.2f}".format(nation,cont,popl,area))

main()

