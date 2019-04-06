#!/usr/bin/env python

import sys
import json

def mapper(record):
    personA = record[0]
    personB = record[1]
    print (personA), (personB)

for line in sys.stdin:
    line = line.strip()
    rec = json.loads(line)
    mapper(rec)
