p = -1
r = -1
n = -1

while p< 0:
    p = float(input("Enter the amount of the loan: "))
while not 0<= r <= 100:
    r = float(input("Enter the interest rate: "))
while n <0:
    n = int(input("Enter the duration in months: "))

r = r/1200

mPay = p*r/(1-(1+r)**-n)
tInterest = n*mPay-p

print("Monthly payment: ${0:.2f}".format(mPay))
print("Total interest paid: ${0:.2f}".format(tInterest))