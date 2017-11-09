import timeit
filename = ("mapper.txt")
file_handle = open(filename, "r+")
f1=open("sort.txt","a")
words = []
for line in file_handle:
    words += line.split("\n")
start=timeit.default_timer()
words.sort()
stop=timeit.default_timer()
for i in range (0,len(words)):
    f1.write(words[i])
    f1.write("\n")
file_handle.close()
f1.close()
print (stop-start)
