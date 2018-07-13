import pandas as pd

def find_col_distinct_values(df, include=None, exclude=['O']):
    dict_frequency = {}
    for col in df.select_dtypes(include=include, exclude=exclude):
        dict_frequency[col] = {'UQL': len(list(set(df[col]))),
                              'UQV': list(set(df[col])),
                              }
    return dict_frequency
