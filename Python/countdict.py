counts = dict()
line = input('Enter a line of text:')
words = line.split()
print(words)

for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts', counts)
for a,b in counts.items():
    print(a,b)
    print(a)
    print(b)

ccc = dict()
ccc['cwen'] = 1
ccc['cwen'] = ccc['cwen']+1
print(ccc)
print('csev' in ccc)


counts = dict()
names = ['cse', 'tarun', 'kumar','saurabh']
for name in names:
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name]+1
print(name)
print(counts)

#get method
counts = dict()
names = ['cse', 'tarun', 'kumar','saurabh']
for name in names:
    if name in names :
        counts[name] = counts.get(name,0) +1
print(counts)


counts = { 'tarun':1 , 'chucks':2, 'chucks':3, 'alpha': 55}
for a in counts:
    print(a)
    print(a,counts[a])
print(counts.keys())
print(counts.values())
print(counts.items())
print(list(counts))

#finding and printing maximum
bc = none
bw = none
for w,c in counts.items():
    if bc is none or c>bc:
        bw = w
        bc = c
print(bc,bw)
