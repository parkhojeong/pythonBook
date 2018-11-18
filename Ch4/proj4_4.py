def main():
    name = input("Enter name of item purchased: ")
    purYear = int(input("Enter year purchased: "))
    cost = float(input("Enter cost of item: "))
    life = int(input("Enter estimated life of item (in years): "))
    type = input("Enter method of depreciation (SL or DDB): ")

    print("Description:", name)
    print("Year of purchase:", purYear)
    print("Cost: ${0:,.2f}".format(cost))
    print("Estimated life: {} years".format(life))
    if type.upper() == "SL":
        print("Method of depreciation: straight-line.")
        print("{0:10}{1:>20s}{2:>20s}{3:>20s}".format("","Value at","Amt Deprec","Total Depreciation"))
        print("{0:10}{1:>20s}{2:>20s}{3:>20s}".format("", "Beg of Yr.", "During Yr.","to End of Yr."))
        SL(purYear, cost, life)
    elif type.upper() == "DDB":
        print("Method of depreciation: double-declining balance.")
        print("{0:10}{1:>20s}{2:>20s}{3:>20s}".format("", "Value at", "Amt Deprec", "Total Depreciation"))
        print("{0:10}{1:>20s}{2:>20s}{3:>20s}".format("", "Beg of Yr.", "During Yr.", "to End of Yr."))

        DDB(purYear, cost, life)

def SL(purYear,cost,life):
    r = 1/life
    curAmt = cost
    deSum = 0
    for year in range(purYear,purYear+life):
        deAmt = cost*r
        deSum +=  deAmt
        print("{0:10}{1:>20,.2f}{2:>20,.2f}{3:>20,.2f}".format(year,curAmt,deAmt,deSum))
        curAmt -= deAmt

def DDB(purYear,cost,life):
    r = 2/life
    curAmt = cost
    deSum = 0
    for year in range(purYear,purYear+life):
        if year == purYear+life-1:
            deAmt = curAmt
        else:
            deAmt = curAmt*r
        deSum +=  deAmt
        print("{0:10}{1:>20,.2f}{2:>20,.2f}{3:>20,.2f}".format(year, curAmt, deAmt, deSum))
        curAmt -= deAmt

main()

