fname = input("Enter file name: ")
fh = open(fname)
count = 0
lst = list()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        print(words[1])
        count= count + 1
print('There were ' + str(count) +' lines in the file with From as the first word')
