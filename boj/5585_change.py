coinList = [500,100,50,10,5,1]
total = 1000-eval(input())
coinList= sorted(coinList)

resCoinList = []
cnt = 0
resSet = set()
order = len(coinList)-1
leftMoney = total
while order >= 0 :
    if (leftMoney - coinList[order]) >=0 :
        cnt += leftMoney // coinList[order]
        leftMoney = leftMoney%coinList[order]
        # resSet.add(coinList[order])
        # if coinList[order] <= leftMoney:

    else:
        order -=1


print(cnt)
