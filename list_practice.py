fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line1 = line.split()
    
    for i in line1:
        if i not in lst:
            lst.append(i)
            lst.sort()

print(lst)
