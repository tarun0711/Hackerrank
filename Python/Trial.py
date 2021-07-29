#Assignment 9

name = input("Enter file:")
f = open(name)
dd = dict()
lst =list()
for line in f :
    line = line.rstrip()
    if line.startswith("From"):
        words = line.split()
        dd[words[1]] = dd.get(words[1],0) +1


bc = None
bw = None
for i,j in dd.items():
    if bc is None or j>bc:
        bc = j
        bw = i
print(bc,bw)


#Assignment 10

name = input("Enter file:")
handle = open(name)
dd = dict()
for line in handle:
    line =line.rstrip()
    
    if line.startswith('From '):
        words = line.split()
        words = words[5]
        words = words[0:2]
        dd[words] = dd.get(words,0)+1
 
lst = list()
for j,i in dd.items():
    lst.append((j,i))
    
    
lst.sort()
for j,i in lst:
    print(j,i)