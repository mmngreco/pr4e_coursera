fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
lst = []
count = 0
fh = open(fname)
for line in fh:
	if not line.startswith("From:"): continue
	lst += [line.rstrip().split()[1]]
	count += 1

for e in lst:
	print e

print "There were", count, "lines in the file with From as the first word"