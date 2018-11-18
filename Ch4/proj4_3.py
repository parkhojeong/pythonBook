def main():
    N = (getInput())
    numDict = verbalizeNumber(N)

    verDict = {}
    for item in numDict.items():
        k = item[0]
        v = item[1]
        if k == 0:
            verDict[0] = {"criteria": "", "amt": v}
        elif k==1:
            verDict[1] = {"criteria": "thousand","amt":v}
        elif k==2:
            verDict[2] = {"criteria": "million", "amt": v}
        elif k==3:
            verDict[3] = {"criteria": "billion", "amt": v}
        elif k==4:
            verDict[4] = {"criteria": "trillion", "amt": v}
        elif k==5:
            verDict[5] = {"criteria": "quadrillion", "amt": v}
        elif k==6:
            verDict[6] = {"criteria": "quintillion", "amt": v}
        elif k==7:
            verDict[7] = {"criteria": "sextillion", "amt": v}
        elif k==8:
            verDict[8] = {"criteria": "septillion", "amt": v}

    for i in reversed(list(verDict.keys())):
        print("{0:>3} {1}".format(verDict[i]["amt"],verDict[i]["criteria"]))

def verbalizeNumber(number):
    numDict = {}
    cnt = len(str(number))//3
    if len(str(number)) > cnt*3:
        cnt +=1
    for i in range(cnt):
        numDict[i] = number%1000
        number = number//1000
    return numDict

def getInput():
    file = open("num27.txt",'r')
    N = int(file.readline())
    posFlag= False
    while posFlag==False:
        posFlag = isValid(N)
    return N

def isValid(num):
    if num>0:
        return True
    else:
        return False

main()