li = input("Enter a word or phrase: ").upper()
li2 = li[::-1]
checkList1 = []
for item in li:
    if 'A'<= item <='Z' :
        checkList1.append(item)
checkList2 = checkList1[::-1]

if checkList1 == checkList2:
    print(li,"is a palindrome.")
else:
    print(li,"is not a palindrome.")
