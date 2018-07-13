import pandas as pd

def find_col_distinct_values(df, include=None, exclude=['O']):
    dict_frequency = {}
    for col in df.select_dtypes(include=include, exclude=exclude):
        dict_frequency[col] = {'UQL': len(list(set(df[col]))),
                              'UQV': list(set(df[col])),
                              }
    return dict_frequency

def find_all_zero_col(df, include=None, exclude=['O']):
    all_zero_col = []
    for col in df.select_dtypes(include=include, exclude=exclude):
        if not len(set(df[df[col] != 0][col])):
            all_zero_col.append(col)
    return all_zero_col
