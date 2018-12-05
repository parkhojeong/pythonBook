infile = open("Senate113.txt", 'r')
infile2 = open("RetiredSen.txt", 'r')
infile3 = open("NewSen.txt", 'r')
outfile = open("Senate114a", 'w')

a = {line for line in infile}
b = {line for line in infile2}
c = {line for line in infile3}
set4 = { item.rstrip() for item in (a.difference(b)).union(c)}
outfile.writelines(set4)

dict1 =[ item.split(',') for item in set4]
dict1.sort(key=lambda x: x[1])
list1 = [ x[2] == y[2] for x, y in zip(dict1[::2], dict1[1::2])]
# list1 = [ x[2] == y[2] for x in dict1[::2] for y in dict1[1::2]
# -> 2중 for loop
list2 = zip(dict1[::2], dict1[1::2])
for item in list2:
    print(item)
print("the number of states with same party affiliation is ", sum(list1))

d1 = {'D':0, 'R':0, 'I':0}

for item in d1.keys():
    list2 = [ x[2] == item for x in dict1]
    print(list2)
    d1[item]=sum(list2)
print(d1)
