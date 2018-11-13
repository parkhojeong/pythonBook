str = (input("Enter a credit card number: "))
numList = [int(item) for item in str]

oddNumList  = []
evenNumList = []
i = 0
for num in numList[::2]:
    doubleNum = num*2
    if doubleNum < 10:
        oddNumList.append(doubleNum)
    else :
        oddNumList.append(doubleNum-9)

for num in numList[1::2]:
    evenNumList.append(num)

sumOfTwoList = sum(oddNumList)+sum(evenNumList)
if sumOfTwoList%10 == 0 :
    print("The number is valid")
else:
    print ("The number isn't valid")