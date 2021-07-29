def checks(n):
    for i in range (0,n+1):
        if(i%19==0):
            print(i)
        
n = int(input("enter the number"))
checks(n)