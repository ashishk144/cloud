#!/usr/bin/env python
import sys
import json


diction = {}
for line in sys.stdin:
    pA, pB = line.strip().split('\t', 1)
    if pA in diction:
        diction[pA].append(pB)
    else:
        lis = [pB]
        diction[pA] = lis

for key in diction.keys():
    print "[\"%s\", %d]" % (key, len(diction[key]))
