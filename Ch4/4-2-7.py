names = ["Dennis Ritchie", "Alan Kay", "John Backus", "James Gosling"]
names.sort(key=lambda name: name.split()[-1])
#lamda 함수명: 함수
nameString = ", ".join(names)
print(nameString)

