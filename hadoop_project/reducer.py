#!/usr/bin/env python3

import sys

top_salaries = []
count = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    id = data[0]
    if id == 'id':
        pass
    else:
        key_value_pairs = data[1].split(',')
        company = data[1].split(',')[0]
        Salary = float(data[1].split(',')[1])

        # Build a 10 element long list
        if count < 10:
            top_salaries.append((id, company, Salary))
            top_salaries = sorted(top_salaries,
                                  key=lambda x: x[2],
                                  reverse=True)
            count += 1

        # Add new element, sort, pop
        else:
            top_salaries.append((id, company, Salary))
            top_salaries = sorted(top_salaries,
                                  key=lambda x: x[2],
                                  reverse=True)
            top_salaries.pop(10)

# Add new column headers
headers = ("id", "company", "Salary")
top_salaries.insert(0, headers)

# Make pretty for printing
for line in top_salaries:
    print(str(line[0]) + '\t' + str(line[2]) + '\t' + str(line[1]))
