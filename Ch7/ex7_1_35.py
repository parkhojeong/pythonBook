class Cart:
    def __init__(self):
        self.article = input("Enter description of article: ")
        self.price = float(input("Enter price of article: "))
        self.quantity = int(input("Enter quantity of article: "))

    def __str__(self):
        return "{0:10s}${1:<10.2f}{2:^10d}".format(self.article, self.price, self.quantity)

class Purchase:
    def __init__(self):
        self.cartList=[]
    def appendCart(self):
        c = Cart()
        self.cartList.append(c)
    def getCartList(self):
        return self.cartList
    def printCartList(self):
        print("{0:10}{1:<10}{2:^10}".format("ARTICLE","PRICE","QUANTITY"))
        for item in self.cartList:
            print(item)
def main():
    inputFlag = 'Y'
    p = Purchase()
    while inputFlag.upper() == 'Y':
        p.appendCart()
        inputFlag= input("Do you want to enter more articles (Y/N)? ")
    p.printCartList()
main()

