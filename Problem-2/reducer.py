#!/usr/bin/env python

import sys
import json

order = {}
line_item = {}
result = {}

for line in sys.stdin:
    val = line.strip().split(" ", 1)
    rec = eval(val[1])
    
    if(rec[0] == "order"):
        order[val[0]] = rec
    elif (rec[0] == "line_item"):
        if (val[0] in line_item):
            line_item[val[0]].append(rec)
        else:
            line_item[val[0]] = [rec]


i = 1
for key.encode("ascii","replace") in line_item:
    for value in line_item[key]:
        result[i] = order[key] + value
        i += 1
	
for keys in result:
    print result[keys]


