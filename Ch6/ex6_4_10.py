def main():
    n = int(input("Enter a positive integer: "))
    res =fib(n)
    print("Fibonacci number:",res)
def fib(n):
    if n ==1 or n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)

main()