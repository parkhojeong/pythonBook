a = 0

while a == 0:
    a = float(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = b**2-4*a*c
if D > 0:
    res1 = (-b+(D)**0.5)/2*a
    res2 = (-b-(D)**0.5)/2*a
    print("Solutions: {} and {}".format(res1,res2))
elif D == 0:
    res = -b/2*a
    print("Solution: {}".format(res))
else:
    print("Solution does not exist.")
