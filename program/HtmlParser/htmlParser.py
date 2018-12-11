def main():
    infile = open("page.txt",'rt', encoding='UTF8')
    parser(infile)

def parser(infile):
    printFlag = False
    list = [line.rstrip() for line in infile]
    brFlag = True
    openBr = False
    newLineFlag =False

    for line in list:
        if line.endswith("<h2>수업소개</h2>"):
            printFlag = True


        if printFlag == True:
            for item in line.split():
                newLineFlag = False
                brFlag = False

                if item.startswith("<") or item.startswith(">"):
                    brFlag = True
                if item.endswith("."):
                    newLineFlag = True

                if newLineFlag == False:
                    print(item,end=" ")
                else :
                    print(item)

        if line.endswith("후원금</a>으로 사용됩니다.&nbsp;</p>"):
            printFlag = False




main()

