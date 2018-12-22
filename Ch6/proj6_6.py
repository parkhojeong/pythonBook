
def main():
    n = int(input("Enter a nonnegative integer: "))
    print("Row {}: ".format(n),end="")
    for i in range(n+1):
        res = paskal(n,i)
        print(res,end=" ")



def paskal(i,j):
    if(i==0 and j ==0):
        return 1
    elif i==0 and j!=0:
        return 0
    else:
        return paskal(i-1,j-1)+paskal(i-1,j)

main()
