import pandas as pd
import numpy as np

# Load csv into DataFrame
df = pd.read_csv('/path/to/file.csv')

# Export DataFrame to csv
df.to_csv('/path/to/file.csv')

# DataFrame Constructors
#     col1   col2
#  0  1      A
#  1  2      B
df = pd.DataFrame(
    np.array([[1, 'A'], [2, 'B']]),
    columns=['col1', 'col2'],
)
df = pd.DataFrame(
    {
        'col1': [1, 2],
        'col2': ['A', 'B'],
    }
)
df = pd.DataFrame(
    {
        'col1': pd.Series([1, 2]),
        'col2': pd.Series(['A', 'B']),
    }
)

# Add row for exist DataFrame
#     col1   col2
# 0   1      A   
# 1   2      B   
# 2   3      C
df_as_row = pd.DataFrame([[3, 'C']], columns=['col1', 'col2'])

# Add column for exist DataFrame
#     col1   col2   col3
# 0   1      A      True
# 1   2      B      False
df.assign(col3=[True, False])


# SQL like join
df1.merge(df2,
          how='left', # left, right, cross, inner
          left_on=['lkey'],
          left_on=['lkey'],
          suffixes=['_left', '_right'],
          )
