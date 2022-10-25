import pandas as pd
import numpy as np

# Load csv into DataFrame
df = pd.read_csv('/path/to/file.csv')

# Export DataFrame to csv
df.to_csv('/path/to/file.csv')

"""
DataFrame Constructors
   col1   col2
0  1      A
1  2      B
"""
# Row like input data 
df = pd.DataFrame(
    np.array([[1, 'A'], [2, 'B']]),
    columns=['col1', 'col2'],
)
# Column like input data
df = pd.DataFrame(
    {
        'col1': [1, 2],
        'col2': ['A', 'B'],
    }
)
# Column like input data by Series
df = pd.DataFrame(
    {
        'col1': pd.Series([1, 2]),
        'col2': pd.Series(['A', 'B']),
    }
)

"""
Add row for exist DataFrame
    col1   col2
0   1      A   
1   2      B   
2   3      C
"""
df_as_row = pd.DataFrame([[3, 'C']], columns=['col1', 'col2'])

"""
Add column for exist DataFrame
    col1   col2   col3
0   1      A      True
1   2      B      False
"""
df.assign(col3=[True, False])


"""
Filtering
"""
df[df['col1'] == 'A']

"""
SQL like operations
"""
df1 = pd.DataFrame(
    np.array([[1, 'A', 1], [2, 'B', 1]]),
    columns=['col1', 'col2', 'total'],
)
df2 = pd.DataFrame(
    np.array([[1, 'A', 1], [3, 'C', 2]]),
    columns=['col1', 'col3', 'total'],
)

# Join
df1.merge(df2,
          how='left', # left, right, cross, inner
          left_on=['col1'],
          left_on=['col1'],
          suffixes=['_left', '_right'],
          )
# Grouping 
df1g = df1.groupby(['col1'])

# Aggregate functions
df1g['total'].sum()