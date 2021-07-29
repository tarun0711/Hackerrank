x = ('tarun ', 'is', 'cool')
print(x)
#tupple cannot be sort append reverse insert extend or pop but count or index can be done
print(x[2])
#strings amd tuples are not mutable x[2] =15 will give a traceback
#tuple can be out on right hand side of an assignment statement
(x,y) = (4,'fred')
print(y)
# tuple k smne tuple rkh(a,b) = 9
#comparison operator work in tuples
#('Tarun','Kumar')<('tarun','kumar')
#d = {'Tarun':2,'tarun':7,'kumar':5,'Kumar':9}
#d.items()
#sorted(d.items())
d = {'Tarun':2,'tarun':7,'kumar':5,'Kumar':9}
sorted(d.items())
t = sorted(d.items())
for i,j in t :
    print(i,j)

#for sorting a tupple by value
d = {'Tarun':2,'tarun':7,'kumar':5,'Kumar':9}
tmp=list()
for i,j in d.items():
    tmp.append((i,j))
print(tmp)
print(sorted(tmp))
tmp = sorted(tmp,reverse=True)#reverse= true it sorts in descending it is still sorting keys
print(tmp)


#printing 10 most occuring words in file
f = open('rome.txt')
counts = dict()
#Creating an unsorted histogram
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1
#appending tupples in list
lst = list()
for i,j in counts.items():#converting elements of dict to tupples
    newtup=(i,j)
    lst.append(newtup)#appending tupples in list
#sorting the list
lst = sorted(lst)
lst =sorted(lst, reverse = True)

for i,j in lst[:10]:#printing first 10 because they are the most occuring elements in the file
    print(i,j)



print(sorted[(j,i) for (i,j) in counts.items() ] )#36to50 all code in one line

