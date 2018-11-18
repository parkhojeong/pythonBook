class employee:
    def __init__(self):
        self._name =  input("Enter person's name: ")
        self._workHours = float(input("Enter number of hours worked: "))
        self._wage = float(input("Enter hourly wage: "))
    def payForWeek(self):
        if self._workHours < 40:
            self._pay = self._workHours*self._wage
        else:
            self._pay = 40*self._wage + (self._workHours-40)*1.5*self._wage
    def __str__(self):
        return "Pay for Alice: ${0:.2f}".format(self._pay)

def main():
    e = employee()
    e.payForWeek()
    print(e)

main()