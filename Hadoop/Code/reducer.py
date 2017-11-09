#!/usr/bin/python
import sys
import timeit
salesTotal = 0
oldKey = None

time1=[]
start=timeit.default_timer()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped)==1:
        time1.append (data_mapped)
        continue

    if len(data_mapped) != 2:       
       # Something has gone wrong. Skip this line.
        continue
     

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
elapsed=timeit.default_timer()-start
if oldKey != None:
    print oldKey, "\t", salesTotal
print "\nTime for Reducer :"
print elapsed 
print "\nTime for each Mapper :"
print time1
