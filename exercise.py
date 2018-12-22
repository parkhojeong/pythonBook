di = {"a":1,"b":2}
print(di.keys())
print(di.items())
print(list(di))
print(tuple(di))


outfile = open("output.txt","w")
outfile.writelines(",".join({"a","b"}))

print("\t\n".isspace())
print("abc".index("a"))

class a:
    def __str__(self):
        return ['a','b']

aob = a()
print(aob)

