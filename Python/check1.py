fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
lst = list()
avg = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        count = count + 1
        lst = line.split()
        s = s + float(lst[1])
avg = s/count
print("Average spam confidence: "+ str(avg))
