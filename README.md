# Hadoop-vs-Python
Comparative Analysis Study of Hadoop (Distributed) and Python (Serial) Execution for Big Data Set.
A dataset text file of Sales is take which contains six columns seperated by tab which include date,time,store,item,cost,payment.
Our aim is to find the time taken by Hadoop and Python for executing same task. Task - Finding Total Cost for every Store.

# HADOOP

Dataset name: purchases.txt

Upload data to hadoop HDFS

Command

<b>hadoop fs -mkdir myinput 

hadoop fs -put purchases.txt myinput</b>

Navigate to the code folder with the mapper.py and reducer.py

<b>hs mapper.py reducer.py myinput output1 </b> *//hs used for hadoop streaming as Python used instead of default Java*

Output saved in the dir output1
Command to view

<b>hadoop fs -cat output1/part-00000 | less </b>

# PYTHON

run python using python mapper.py, sort.py and reducer.py in order from the Python folder. (Python 2.6)

Timing details in the outputfor both Python and Hadoop.

DataSet URL : https://drive.google.com/open?id=0ByF9VTm44xRNWXkzRk9oNHRSVEE
