def main():
    p = float(input("Enter the principal: "))
    r = float(input("Enter the annual rate of integer: "))
    pmt = float(input("Enter the monthly payment: "))
    n = int(input("Enter the number of monthly payments made: "))

    res = balance(p,pmt,r,n)
    print("The amount sill owed is ${0:,.2f}.".format(res))

def balance(p,pmt,r,n):
    if n ==0 :
        return p
    else:
        return (1+r/1200)*balance(p,pmt,r,n-1)-pmt

main()