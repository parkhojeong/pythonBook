str = input("Enter a word to code:")
li = list(str)
for i in range(len(li)-1,-1,-1):
    if li[i] in ['a','e','i','o','u','h','y','w']:
        del li[i]
    elif li[i] in ['b','f','p','v']:
        li[i]='1'
    elif li[i] in ['c','g','j','k','q','s','x','z']:
        li[i] ='2'
    elif li[i] in ['d','t']:
        li[i]='3'
    elif li[i] in ['l']:
        li[i]='4'
    elif li[i] in ['m','n']:
        li[i]='5'
    elif li[i] in ['r']:
        li[i]='6'

prevCh= '-'
for i in range(len(li)-1,-1,-1):
    if li[i] != prevCh:
        prevCh = li[i]
    else:
        del li[i]

if len(li) >=4 :
    li = li[:4]
else:
    for i in range(len(li),4):
        li.append('0')

str = "".join(li)
print("The coded word is {}".format(str))
