 print()
for i in range(1,4):
  for j in range(1,i+1):
    print(i, end =" ")
  print("\r")


print()
for i in range(1,5):
  for j in range(1,i+1):
    print(j, end =" ")
  print("\r")


print()

n = 1
for i in range(1,5):
  for j in range(1,i+1):
    print(n, end =" ")
    n += 1
  print("\r")


for i in range (1,6,+1):
  print(i*"* ", (5-i)*" ")


print(" ")
for i in range(5,0,-1):
  print(i*"* ")

for i in range (1,6,1):
  print((7-i)*" ",i*"* " )
