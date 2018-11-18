import random
class dice:
    def __init__(self):
        self._N1 = -1
        self._N2 = -1
        self.numbers = ['1','2','3','4','5','6']
    def mix(self):
        self._N1 = random.choice(self.numbers)
        self._N2 = random.choice(self.numbers)

    def test(self):
        for i in range(24):
            self.mix()
            if self._N1 == '6' and self._N2 == '6':
                return True

        return False

def main():
    d = dice()
    cnt = 0
    for i in range(10000):
        res = d.test()
        if res == True:
            cnt += 1
    print(cnt/10000)

main()