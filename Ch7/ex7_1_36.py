class Register:
    def __init__(self):
        self.num = 0
        self.money = 0
    def enterVehicle(self,type):
        self.num += 1
        if type.lower() == "car":
            self.money +=1
        elif type.lower() =="truck":
            self.money += 2
    def getNum(self):
        return self.num
    def getMoney(self):
        return self.money

def main():
    enterFlag = True
    r = Register()
    while enterFlag == True:
        type = input("Enter type of vehicle(car/truck): ")
        r.enterVehicle(type)
        print("Number of vehicles: {}".format(r.getNum()))
        print("Money Collected: ${0:.2f}".format(r.getMoney()))

        isMore= input("Do you want to enter more vehicles (Y/N)? ")
        if isMore.upper() == 'Y':
            enterFlag= True
        else:
            enterFlag = False
            print("Have a good day.")

main()