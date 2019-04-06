#!/usr/bin/env python
import sys


diction = {}
for line in sys.stdin:
    line = line.strip()
    w, document_id = line.split("\t", 1)
    if w in diction:
        diction[w].append(str(document_id))
    else:
        lis = []
        lis.append(str(document_id))
        diction[w] = lis

for key in diction.keys():       
    print "[\"%s\", %s]" % (key,list(set(diction[key])))
