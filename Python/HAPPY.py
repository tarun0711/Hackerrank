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
    n= int(input("enter a number:"))
    p = checkHappy(n)

    if p==1:
        print(a+"is a HAPPY NUMBER")
    else:
        print(a+"is NOT a HAPPY NUMBER")
