import pickle
def fileOpen(fileName):
    file = open(fileName ,'rb')
    dictOb = pickle.load(file)
    file.close()
    return dictOb

def viewGeneral(dictOb):
    print("{0:30}{1:20,d}{2:20,d}".format("Study area",1981,2010))
    for key in dictOb.keys():
        print("{0:30}{1:20,d}{2:20,d}".format(key,dictOb[key][0],dictOb[key][1]))

def viewRate(dictOb):
    ratedictOb = {key: dictOb[key][1]/dictOb[key][0]for key in dictOb.keys()}
    sorted(ratedictOb.items(),key= lambda k : k[1], reverse=True)
    for key in ratedictOb.keys():
        print("{0:30}{1:20.1%}".format(key, ratedictOb[key]))

def viewAmt(di):
    di = dict(sorted(di.items(),key=lambda k:k[1][1]))
    for key in di.keys():
        print("{0:30}{1:,d}".format(key,di[key][1]))

dictOb = fileOpen("DegreesDict.dat")
selectMenu = '0'
while selectMenu != '4':
    if selectMenu == '1':
        viewGeneral(dictOb)
    elif selectMenu == '2':
        viewRate(dictOb)
    elif selectMenu == '3':
        viewAmt(dictOb)
    print()
    selectMenu = input("Enter a menuNum: ")

