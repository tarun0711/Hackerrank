def sqaureSum(t) :
    s =0
    while(t>0) :
        r = t%10
        s = s + r*r
        t=int(t/10)
    checkHappy(s)

def checkHappy(sum):
    if sum >9:
        sqaureSum(sum)
    else :
        return sum

def acceptNum():
    n= int(input("enter :"))
    p = checkHappy(n)

    if p==1:
        print(n+"is a HAPPY NUMBER")
    else:
        print(n+"is NOT a HAPPY NUMBER")
