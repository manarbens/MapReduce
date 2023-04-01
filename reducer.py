#!user/bin/python
import sys
Total = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
    # if Something has gone wrong. Skip this line.
            continue
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
         print oldKey, "\t", Total
         Total = 0
    oldKey = thisKey
    Total += int(thisValue)
    if oldKey != None:
        print oldKey, "\t" , Total