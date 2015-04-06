#!/usr/bin/env
# -*- coding:utf-8 -*-

name = raw_input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name, 'r')
count_dict = dict()
maxkey = None
maxvalue = None

for line in handle:
    if not line.startswith('From '):
        continue
    w = line.split()[1].strip()
    c = count_dict.get(w, 0)
    count_dict.update({w: c + 1})

for k, v in count_dict.items():
    if maxvalue is None or v > maxvalue:
        maxkey = k
        maxvalue = v

# for k, v in count_dict.iteritems():
#     print k, v

t = ' El Mejor Valor '.center(30, '=')
print t
print maxkey, maxvalue
print '=' * len(t)
