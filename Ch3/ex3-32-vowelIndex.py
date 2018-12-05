str= input("Enter word to translate: ")
index = [i for i in range(len(str)) if str[i] in ['a', 'e', 'i', 'o', 'u'] ]
print(index[0])

