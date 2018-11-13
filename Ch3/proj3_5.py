deposit1 = 0
deposit2 = 0
amt1 = 0
amt2 = 0
r = 0.04
for i in range(15):
    deposit1 = deposit1 * (1 + r)
    deposit1 += 5000
    amt1 += 5000


deposit1 = deposit1*(1+r)**33


for i in range(33):
    deposit2 = deposit2 * (1 + r)
    deposit2 += 5000
    amt2 += 5000

print("{0:^40}".format("AMOUNTS DEPOSITED"))
print("Earl: ${0:<20,.2f} Larry: ${1:<20,.2f}".format(amt1,amt2))
print("{0:^40s}".format("AMOUNTS IN IRA UPON RETIREMENT"))
print("Earl: ${0:<20,.2f} Larry: ${1:<20,.2f}".format(deposit1,deposit2))