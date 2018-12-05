list1 = []
list2 = []
list3 = []
phrase = input("Enter a word or phrase: ").upper()
list1 = [item for item in list(phrase) if 65<=ord(item) <=90 ]
list2 = [x.upper() for x in phrase if x.isalpha()]

print(list1)
print(list2)


# list comprehension
# set, object oriented
# not ordered list일 때 == sign
# binary file 저장하고 읽어들이는거 시험
