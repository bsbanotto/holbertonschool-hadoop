# Project: Hadoop

There are 8 mandatory tasks in this project as follows:

## Task 0. HDFS with BASH (1)

Write a bash script  `createdirectories.sh`  that creates the directory  `/holbies`  and  `/holbies/input`  within HDFS.

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part1$ /createdirectories.sh
hdoop@Ahmed-Belhaj:~/ProjectHadoop$ hadoop  fs -ls -R /
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:08 /holbies
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:08 /holbies/input
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part1$
```

## Task 1. HDFS with BASH (2)

Write a bash script  `lao.sh`that upload the file  `lao.txt`  to the  `/holbies/input`  directory on the HDFS.

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop$./lao.sh
hdoop@Ahmed-Belhaj:~/ProjectHadoop$ hadoop fs -ls /holbies/input
Found 1 items
-rw-r--r--   1 hdoop supergroup        287 2022-05-01 02:14 /holbies/input/lao.txt
```

## Task 2. HDFS with BASH (3)

Write a bash script  `text.sh`  that displays the content of the file  `lao.txt`  on the HDFS.

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop$./lao.sh
Simplicity, patience, compassion. These three are your greatest treasures. Simple in actions and thoughts, you return to the source of being. Patient with both friends and enemies, you accord with the way things are. Compassionate toward yourself, you reconcile all beings in the world.
```

## Task 3. HDFS with Python (Snakebite): createdir

For this part we need to install the snakebite library.

`pip install snakebite-py3`

Write a function  **def createdir(l)**: that creates the directories listed on l within HDFS

```BASH
#!/usr/bin/python3.8


createdir = __import__('4-createdir').createdir


l = ["/Betty", "/Betty/Holberton"]
createdir(l)

```

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part_two$ python3 main.py
{'path': '/Betty', 'result': True}
{'path': '/Betty/Holberton', 'result': True}
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part_two$ hadoop fs -ls -R /
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:40 /Betty
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:40 /Betty/Holberton
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:08 /holbies
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:14 /holbies/input
-rw-r--r--   1 hdoop supergroup        287 2022-05-01 02:14 /holbies/input/lao.txt
```

## Task 4. HDFS with Python (Snakebite): deletedir

Write a function  **def deletedir(l)**: that removes the directories listed on l within HDFS

```BASH
#!/usr/bin/python3.8


deletedir = __import__('5-deletedir').deletedir


l = ["/Betty", "/Betty/Holberton"]
deletedir(l)

```

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part_two$ python3 main.py
{'path': '/Betty/Holberton', 'result': True}
{'path': '/Betty', 'result': True}
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part_two$ hadoop fs -ls -R /
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:08 /holbies
drwxr-xr-x   - hdoop supergroup          0 2022-05-01 02:14 /holbies/input
-rw-r--r--   1 hdoop supergroup        287 2022-05-01 02:14 /holbies/input/lao.txt
```

## Task 5. HDFS with Python (Snakebite): download

Write a function  **def download(l)**: that retrieves from the HDFS files listed in l and store them in the home  `/tmp`  folder of the user

```BASH
#!/usr/bin/python3.8


download = __import__('6-download').download


l = ["/holbies/input/lao.txt"]
download(l)
lao =  open("/tmp/lao.txt", "r")
print(lao.read())
lao.close()

```

```BASH
hdoop@Ahmed-Belhaj:~/ProjectHadoop/part_two$ python3 main.py
{'path': '/tmp/lao.txt', 'result': True, 'error': '', 'source_path': '/holbies/input/lao.txt'}
Simplicity, patience, compassion. These three are your greatest treasures. Simple in actions and thoughts, you return to the source of being. Patient with both friends and enemies, you accord with the way things are. Compassionate toward yourself, you reconcile all beings in the world.
```

## Task 6. MapReduce (mapper)

The aim of this task and the next one is to run a Mapreduce application on a Hadoop environment with Python. You have to write two Python programs:  `mapper.py`  and  `reducer.py`

Write the script  `mapper.py`  that takes the rows of the  `salaries.csv`  and print the id, the company and the totalyearlycompensation items. Id and company will be separated by a tabulation while company and totalyearlycompensation will be separated by a comma.

```BASH
hdoop@amine-virtualbox:~/hdoop-project/MapReduce/salaries$ cat salaries.csv |./mapper.py 
id      company,totalyearlycompensation
1       Oracle,127000
2       eBay,100000
3       Amazon,310000
4       Apple,372000
5       Microsoft,157000
6       Microsoft,208000
7       Microsoft,300000
8       Microsoft,156000
9       Microsoft,120000
10      Microsoft,201000
11      Salesforce,450000
12      Microsoft,155000
13      Microsoft,150000
14      Microsoft,191000
```

## Task 7. MapReduce (reducer)

Write the script  `reducer.py`  that takes the output of the  `mapper.py`  script and gives the top ten salaries sorted by totalyearlycompensation. The output should be as below. The mapper and reducer should be run on the Hadoop environment with the mapred command.

This command used to start hadoop streaming service

```BASH
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /holbies/input/salaries.csv \
-output /holbies/output/
```

You have to:

1- Use the put command to upload the  `salaries.csv`  file on the HDFS system on  `/holbies/input`.

2- The output should be stored in the  `/holbies/output/`  folder on the HDFS system.

3- You’re only allowed to use an array of 10 element on your reducer

```BASH
hdoop@amine-virtualbox:~/hdoop-project/MapReduce/salaries$ hdfs dfs -cat /holbies/output/part-00000
2022-04-25 10:01:01,844 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
id      Salary  company
61992   4980000.0       Facebook
61968   4950000.0       Microsoft
61983   4500000.0       Google
61991   4490000.0       Facebook
61970   2500000.0       Snap
61988   2372000.0       Facebook
61986   2200000.0       Facebook
61973   2000000.0       SoFi
61975   1950000.0       Google
61990   1900000.0       Uber
```
