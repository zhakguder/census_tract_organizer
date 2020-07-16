#!/usr/bin/env python3

name = 'AB22'
df = None
coding = {'yes': [1], 'no': [2], 'borderline': [3]}

partition = {'high': ['yes', lambda x: x >= 0.125],
             'low': ['yes', lambda x: x <= 0.085]}
# high: yes >= 0.125
# low: yes <= 0.085
partition_tract_nos = None
