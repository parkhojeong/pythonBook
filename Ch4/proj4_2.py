def main():
    N = getInput()
    max,min = getPrime(N)
    print("Largest prime factor:",max)
    print("Smallest prime factor:",min)
def getPrime(N):
    F = 2
    pSet = set()
    while N >1:
        if N % F == 0 :
            pSet.add(F)
            N = N/F
        else:
            F +=1

    return max(pSet),min(pSet)

def getInput():
    posFlag= False
    while posFlag==False:
        N = int(input("Enter a positive integer (>1): "))
        posFlag = isValid(N)
    return N

def isValid(num):
    if num>1:
        return True
    else:
        return False

main()