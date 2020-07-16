#!/usr/bin/env python3

from diseases import AB17, AB22, AJ29, AJ32, AK28, RBMI
import pandas as pd
tract_no = 'TRACT10'
code = 'Level'
colname_prefix = 'Pct_'

data = None

types = [AB17, AB22, AJ29, AJ32, AK28, RBMI]

def arrange_disease(disease):
    colname = colname_prefix + disease.name
    columns = [tract_no, code, colname]
    disease_df = pd.DataFrame()
    for group, cols in disease.coding.items():
        tmp = data[columns][data[code].isin(cols)]
        tmp = tmp.drop(code, axis = 1).groupby(tract_no).aggregate(sum)
        tmp = tmp.rename(columns={colname: disease.name + '_' + group})
        disease_df = pd.concat([disease_df, tmp], axis=1)
        disease.df = disease_df
    return disease_df

def partition_tract_nos(disease):
    tract_nos = {}
    for group, (cols, criterion) in disease.partition.items():
        if type(cols) == list:
            colnames = [disease.name + '_' + col for col in cols]
            filtered = pd.DataFrame(disease.df[colnames]).apply(criterion, axis=1)
        elif type(cols) == str:
            colnames = disease.name + '_' + cols
            filtered = disease.df[colnames].apply(criterion)
        tract_nos[group] = disease.df[filtered].index.tolist()
    return tract_nos
