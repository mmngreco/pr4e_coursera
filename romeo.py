fname = raw_input("Enter file name: ")
fh = open(fname)
lst = []
words = []

for line in fh:
	lst.append(line.split())
for line in lst:
	for word in line:
		if word in words: continue
		words += [word]
words.sort()
print words

