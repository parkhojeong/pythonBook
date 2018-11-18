def main():
    list = [i for i in range(1,101)]
    res = sum(list)
    print(res)

def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[-1]+sum(list[:-1])

main()