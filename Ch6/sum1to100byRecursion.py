def main():
    res = sum(100)
    print(res)


def sum(n):
    if n <= 1:
        return 1
    else:
        n = n + sum(n-1)
    return n

9
main()
