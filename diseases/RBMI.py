#!/usr/bin/env python3

name = 'RBMI'
df = None

coding = {'obese': [4]}

partition = {'high': ['obese', lambda x: x >= 0.46],
             'low': ['obese', lambda x: x <= 0.388]}
# high: obese >= 0.46
# low: obese <= 0.388
partition_tract_nos = None
