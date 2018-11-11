from math import sqrt
str = input("Enter the sentence:")
num = eval(str)
res = sqrt(num)

print("math.sqrt({0:}) is {1:.2f}".format(num,res))