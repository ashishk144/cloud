#!/usr/bin/env python
# coding=utf-8

import sys
import json

for line in sys.stdin:
    rec = json.loads(line.strip())
    print (rec[1]), (rec)


