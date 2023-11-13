# Uploads local salaries.csv file to /holbies/input on hadoop file services
hadoop fs -copyFromLocal salaries.csv /holbies/input
