import timeit
salesTotal=0
oldKey=None
f=open("sort.txt","r")
start=timeit.default_timer()
for line1 in f:
    data_mapped=line1.strip().split("\t")
    if len(data_mapped) !=2:
        continue
    thisKey,thisSale=data_mapped
    if oldKey and oldKey !=thisKey:
        print (oldKey,"\t",salesTotal)
        oldKey = thisKey;
        salesTotal=0


    oldKey = thisKey
    salesTotal +=float (thisSale)
if oldKey != None:
    print (oldKey,"\t",salesTotal)
stop=timeit.default_timer()
print(stop-start)
f.close()

    
