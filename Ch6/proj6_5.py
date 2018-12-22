arr = list("abc")
def main():
    global arr
    permutation(len(arr))

def permutation(size):
    global arr
    if(size == 0):
        print_arr()
        return

    for i in range(size-1,-1,-1):
        arr[i],arr[size-1] = arr[size-1],arr[i]
        permutation(size-1)
        arr[i], arr[size-1] = arr[size-1], arr[i]

def print_arr():
    for i in range(len(arr)):
        print(arr[i],end="")
    print()

main()