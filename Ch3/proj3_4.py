def rule(r):
    return int(72/r)

def fun(r):
    n = 0
    c = 1
    while c <2:
        n +=1
        c = c*(1+r/100)
    return n

c1 = 1
n1 = 0

str = "{0:20s}{1:30s}{2:30s}"

print(str.format("Interest Rate","Rule of 72 Doubling Time","Actual Doubling Time(in years)"))
rates = [1,2,3,4,5]
for rate in rates:
    print("{0:<20.0%}{1:<30d}{2:<30d}".format(rate/100, rule(rate), fun(rate)))

