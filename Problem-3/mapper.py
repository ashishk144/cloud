#!/usr/bin/env python
import sys
import json


def mapper(record):
    personA = record[0]
    personB = record[1]
    print "%s\t%s" % (personA, personB)

for line in sys.stdin:
    rec = json.loads(line)
    mapper(rec)
