li = input("Enter an ISBN: ").split(sep="-")
str = "".join(li)
sum = 0
for i in range(len(str)):
    k = 10 - i
    if str[i].upper() == 'X':
        sum += 10*k
    else:
        sum+= int(str[i])*k

if sum %11 == 0 :
    print("The number is valid.")
else:
    print("The number is not valid.")
