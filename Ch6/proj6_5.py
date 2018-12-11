def main():

    fun("abc")
def fun(str):

    if(len(str)==2):
        return (str, str[1]+str[0])
    else:
        res1 = ""
        res2 = ""
        res = []
        for i in range(len(str)):
            if(i< len(str)-1 ):
                res1,res2 = fun(str[:i]+str[i+1:])
            else:
                res1,res2 = fun(str[:i])
            res.append(str[i]+res1)
            res.append(str[i]+res2)
        print(res)
main()