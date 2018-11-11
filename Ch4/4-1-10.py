def main():
    ## Demonstrate the scope of variables.
    x = 2
    print(str(x) + ": function main")
    trivial(x)
    print(str(x) + ": function main")

def trivial(item):
    item += 2
    print(str(item) + ": function trivial")
    return item
main()    
