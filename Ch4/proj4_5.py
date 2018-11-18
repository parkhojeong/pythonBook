def main():

    cntDict={1:"one",2:"two",3:"three",4:"four",5:"five",
             6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"}
    word = input("Enter a word: ")
    ordFlag,maxOrdCnt = isTripleconsecutive(word)
    if ordFlag == True:
        print(word,"contains",cntDict[maxOrdCnt],"successive letters in consecutive alphabetical order.")
    else:
        print(word, "doesn't contain successive letters in consecutive alphabetical order.")
def isTripleconsecutive(word):
    prevCh = word[0]
    ordCnt = 0
    maxOrdCnt = 0
    ordFlag = False
    for ch in word[1:]:
        curCh = ch
        if ord(curCh)-ord(prevCh) == 1:
            ordFlag = True
            ordCnt +=1
            if maxOrdCnt < ordCnt :
                maxOrdCnt = ordCnt
        else:
            ordCnt = 0
        prevCh = ch

    return ordFlag, maxOrdCnt+1

main()
