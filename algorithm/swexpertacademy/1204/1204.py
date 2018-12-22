file = open("input.txt")
lines = [line.rstrip() for line in file]
numSet = set()
numSet = {i for i in range(0,101)}


#arr = [line.split(' ') for line in lines if len(line) >10]
k = 0
for line in lines:

    dict1 = {i: 0 for i in numSet}
    arr = line.split(' ')
#    print(arr)
    if len(arr) >10:
        for i in arr:
            i = int(i)
            dict1[i] = dict1[i]+1
        sortedList = sorted(dict1.items(), key = lambda k: k[1])
        print("#{0:} {1}".format(k, sortedList[-1][0]))
        k +=1
    else:
        pass
