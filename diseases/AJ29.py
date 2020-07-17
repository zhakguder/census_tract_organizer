#!/usr/bin/env python3
import os

name = 'AJ29'
df = None
coding = {'all_the_time': [1,2], 'not_at_all': [4,5], 'mid': [3]}

partition = {'high': [['all_the_time', 'not_at_all', 'mid'], lambda x: high(x)],
             'low': [['all_the_time', 'not_at_all', 'mid'], lambda x: low(x)]}


def high(*x):
    a, b, c = _organize(x)
    return a > b and a > c

def low(*x):
    a, b, c = _organize(x)
    return b > a and b > c

def _rename(col):
    return name + '_' + col

def _organize(row):
    x = row[0]
    a = x[_rename('all_the_time')]
    b = x[_rename('not_at_all')]
    c = x[_rename('mid')]
    return a, b, c

# high: all_the_time > not_at_all AND all_the_time > mid
# low: not_at_all > all_the_time AND not_at_all > mid
partition_tract_nos = None

def copy(zoom, image_folder):
    root = os.path.join(name, zoom)
    for key in partition_tract_nos.keys():
        path = os.path.join(root, key)
        breakpoint()
