#!/usr/bin/env python

import sys
import json

def uniqueify(seq, idfun=None): 
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result


for line in sys.stdin:
    line = line.strip()
    record = json.loads(line);
    document_id = record[0]
    document_contents = record[1]
    words = document_contents.split()
    for w in uniqueify(words):
        print "%s\t%s" % (w, document_id)
        #print(w, "Document id: ", document_id)
	#mr.emit_intermediate(w, document_id)


