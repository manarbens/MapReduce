#!/usr/bin/env python
import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 5:
        date, time, store, product, cost = data
        print("{0}\t{1}".format(product, cost))