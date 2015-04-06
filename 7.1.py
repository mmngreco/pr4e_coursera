# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
s = []
n = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    s += [line.rstrip()]

for e in s:
    n += [float(e.split(" ")[1])]

print "Average spam confidence:", sum(n)/len(n)