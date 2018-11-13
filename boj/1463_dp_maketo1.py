def main():
    n = eval(input())
    res = fun(n)
    print(res)

def fun(n):
    cnt = 0
    arr = [0,1]
    arr.insert(2,1)
    arr.insert(3, 1)
    i = 4
    while i<=n:
        n3 = i//3
        n2 = i//2
        if i % 3 == 0 and i % 2 == 0:
            arr.insert(i, min(arr[n3], arr[n2], arr[i - 1]) + 1)
        elif i%3 == 0 and i%2 !=0:
            arr.insert(i,min(arr[n3],arr[i-1])+1)
        elif i%3 !=0 and i%2 ==0:
            arr.insert(i,min(arr[n2],arr[i-1])+1)
        else:
            arr.insert(i, arr[i - 1] + 1)
        i +=1

    return arr[n]

def min(a,b,c=10000):
    if a <=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else :
        return c

main()