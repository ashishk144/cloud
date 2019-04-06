#!/usr/bin/env python

import sys

lists = []
diction = {}
for line in sys.stdin:
    line = line.strip()
    pA, pB = line.split(" ", 1)
    if pA in diction:
        diction[pA].append(pB)
    else:
        diction[pA] = [pB]

def reducer(personA, friendlist):
    for so_called_friend in friendlist:
        if so_called_friend not in diction.keys() or personA not in diction[so_called_friend]:
            lists.append((personA, so_called_friend))
            lists.append((so_called_friend, personA))


for key in diction.keys():
    reducer(key, diction[key])

for tups in set(lists):
    print "[\"%s\", \"%s\"]" % (tups[0], tups[1])
