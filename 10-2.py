name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = {}
for line in handle:
    if not line.startswith('From '): continue
    key = line.split()[5].split(':')[0]
    count[key] = count.get(key, 0) + 1
print 
for k in sorted(count, reverse=False):
    print k, count[k]