#!/usr/bin/env python3

import sys

top_salaries = []

for line in sys.stdin:
    data = line.strip().split('\t')

    id = data[0]
    if id == 'id':
        pass
    else:
        key_value_pairs = data[1].split(',')
        company = data[1].split(',')[0]
        Salary = float(data[1].split(',')[1])

        top_salaries.append((id, company, Salary))

# Sorting the salaries in descending order
top_salaries = sorted(top_salaries, key=lambda x: x[2], reverse=True)

for line in top_salaries[:10]:
    print(line)
