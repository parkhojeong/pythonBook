def main():
    ## Display the countries in a specifed continent.
    continent = input("Enter the name of a continent: ")
    continent = continent.title()   # Allow for all lowercase letters.
    if continent != "Antarctica":
        infile = open("UN.txt", 'r')
        # for line in infile:
        #     data = line.split(',')
        #     if data[1] == continent:
        #         print(data[0])
        #
        [print(line.split(',')[0]) for line in infile if line.split(',')[1] == continent]
    else:
        print("There are no countries in Antarctica.")
        
main()                 



