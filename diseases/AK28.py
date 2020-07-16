#!/usr/bin/env python3


name = 'AK28'
df = None
coding = {'all_the_time': [1,2], 'not_at_all': [3,4]}

partition = {'high': [['all_the_time', 'not_at_all'], lambda x: x[0] > x[1]],
             'low': [['all_the_time', 'not_at_all'], lambda x: x[1] > x[0]]}



def high(*x):
    a, b = _organize(x)
    return a > b

def low(*x):
    a, b = _organize(x)
    return b > a

def _rename(col):
    return name + '_' + col

def _organize(row):
    x = row[0]
    a = x[_rename('all_the_time')]
    b = x[_rename('not_at_all')]
    return a, b


# high: all_the_time > not_at_all
# low: not_at_all > all_the_time
partition_tract_nos = None
