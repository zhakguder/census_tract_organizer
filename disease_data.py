#!/usr/bin/env python3

import pandas as pd

path = None
clean_path = None

def read():
    return pd.read_excel(path)

def write_clean(dfs):
    pd.concat(dfs, axis=1).to_excel(clean_path)
    print(f"Data saved to {clean_path}")
