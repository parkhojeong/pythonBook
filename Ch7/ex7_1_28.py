class Fraction:
    def __init__(self,M,N):
        self.M = M
        self.N = N

    def fun(self):
        while self.N != 0:
            T = self.N
            self.N = self.M % self.N
            self.M = T

    def __str__(self):
        self.fun()
        return str(self.M),str(self.M)

    def getM(self):
        return self.M

def main():
    N = int(input("Enter numerator of fraction: "))
    M = int(input("Enter denoinator of fraction: "))
    f = Fraction(N,M)
    f.fun()
    res = f.getM()
    print("Reduction to lowest terms:{0:.0f}/{1:.0f}".format((N/res),(M/res)))

main()

