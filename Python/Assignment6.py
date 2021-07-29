def power(b,e): 
    if(e==1):
        return (b)
    if(e!=1):
        return (base*power(base,e-1))
base=int(input("Enter the base number.."))
n=int(input("Enter the number of terms"))
print("1",end=" ")
for i in range(1,n):
  print(power(base,i),end=" ")