str= input("Enter word to translate: ")
index = [i for i in range(len(str)) if str[i] in "aeiou" ]
print(index[0])

