fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for l in fh:
    if not l.startswith("From"):
        continue
        
    if l.startswith("From:"):
        continue
    
    l = l.rstrip()
    l1 = l.split()
    print(l1[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
