# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
c = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s = s + float(line[-7:-1])
    #print(line[-7:-1])
    c = c + 1
    # print(line)
print("Average spam confidence:",s/c)
