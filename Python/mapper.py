import sys
import timeit
file=open("purchase.txt","r")
file1=open("mapper.txt","a")
start= timeit.default_timer()
for line in file:
    data = line.strip().split("\t")
    if len(data)==6:
        date,time,store,item,cost,payment=data
        file1.write ("{0}\t{1}\n".format(store,cost))
stop=timeit.default_timer()
print(stop-start)
file1.close()
file.close()


