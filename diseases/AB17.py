#!/usr/bin/env python3

name = 'AB17'
df = None
coding = {'yes':[1], 'no':[2]}


# name of dataset partition: [name of column in df, condition to satisfy for being part of partition]
partition = {'high': ['yes', lambda x: x>=0.087],
            'low': ['yes', lambda x: x<=0.067]}
# high: yes >= 0.087
# low: yes <= 0.067

partition_tract_nos = None
