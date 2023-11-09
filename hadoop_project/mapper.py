#!/usr/bin/env python3
"""
Mapper function for salaries.csv file
"""
import csv
import sys


reader = csv.reader(sys.stdin, delimiter=',')
for row in reader:
    print(str(row[0]) + '\t' + str(row[1]) + ',' + str(row[3]))
