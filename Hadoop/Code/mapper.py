#!/usr/bin/python

import sys
import timeit
start=timeit.default_timer()
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
stop=timeit.default_timer()
elapsed=stop-start
print ("%.2f" % elapsed)
