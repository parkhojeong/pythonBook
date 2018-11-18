def main():
    v,h = getInput()
    res1 = maxHeight(v,h)
    res2 = reachFloorTime(v,h)
    print("The maximum height of the ball is {0:.2f} feet.".format(res1))
    print("The ball will hit the ground after approximately {0:.2f} seconds.".format(res2))

def maxHeight(v,h):
    t = v/32
    maxH = h+v*t-16*(t**2)
    return maxH

def reachFloorTime(v,h):
    t = 0
    curHeight = h+v*t-16*t**2
    while curHeight>0:
        t +=0.01
        curHeight= h+(v*t)-(16*(t**2))
    return t

def getInput():
    posFlag = False
    while posFlag == False:
        h = float(input("Enter the initial height of the ball: "))
        posFlag = isValid(h)

    posFlag = False
    while posFlag ==False:
        v = float(input("Enter the initial velocity of the ball: "))
        posFlag = isValid(v)

    return v,h

def isValid(num):
    if num>0:
        return True
    else:
        return False
main()

