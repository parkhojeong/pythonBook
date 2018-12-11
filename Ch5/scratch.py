list = ["raa","rbb","aa"]
for i in range(len(list)-1,-1,-1):
    if 'r' in list[i]:
        del list[i]
print(list)

list = ["raa","rbb","aa"]
for item in reversed(list):
    if 'r' in item:
        list.remove(item)
print(list)

list = ["raa","rbb","aa"]
for item in list:
    if 'r' in item:
        list.remove(item)
print(list)

list = ["raa","rbb","aa"]
for item in set(list):
    if 'r' in item:
        list.remove(item)
print(list)

list = ["raa","rbb","aa"]
i=0
cnt = 0
while cnt < len(list):
    cnt+=1
    if 'r' in list[i]:
        del list[i]
    else:
        i+=1
        pass
print(list)

file = [1,1,2,3]

print({i:i**2 for i in file}.items())


b = [print(i) for i in range(1000,10000) if str(4*i) == str(i)[ : :-1]]
