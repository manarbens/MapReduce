#!/usr/bin/env/python
import sys
#--- get all lines from stdin ---
for line in sys.stdin:
     #--- remove leading and trailing whitespace---
     line = line.strip()
     if len(line)==0:
         continue
     #--- split the line into words ---
     words = line.split()
     #--- output tuples [word, l] in tab-delimited format---
     for word in words:
         print '%s\t%s' % (word,"1")