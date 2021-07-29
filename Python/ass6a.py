def power(b,e): 
    if(e==1):
        return (b)
    if(e!=1):
        return (base*power(base,e-1))
base=int(input("Enter the base number.."))
exp=int(input("Enter the exponential value.."))
print("Result:",power(base,exp))