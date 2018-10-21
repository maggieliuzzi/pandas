import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 'AA','B': 'BB'})

print(type(df))
print(df.shape)
print(df.columns)
print(type(df.columns))
print(df.index)

df.iloc[:5,:] # slice til 5, non-inclusive
df.iloc[:-5,:] # slice from 5th last row til the end
# another option is using labels with the .loc attribute
print(df.head(5))
print(df.tail()) # returns last 5 rows
print(df.tail(3))
print(df.info())
# Pandas slicing also supports Broadcasting

# slicing: every third row starting from 0 in the last column
df.iloc[::3, -1] = np.nan # "not a number" | assigning scalar value to column slide broadcasts value to each row

# columns of a dataframe are series
col1 = df['Col1']
print(type(col1))
col1.head()

# can use the DataFrame attribute .values to represent a DataFrame df as a NumPy array
# can also pass pandas data structures to NumPy methods
col1s = col1.values # to extract numerical entries from the series
# data from series form a numpy array, what values attributes yields
# panda series one-dimensional labeled numpy array
# panda dataframe two-dimensional labeled numpy array whose columns are series
print(type(col1s))

# -----------

# Extract the values and store them in an array using the attribute .values. Then use those values as input into the
# NumPy np.log10() method to compute the base 10 logarithm of the population values. Finally, ass the entire pandas
# DataFrame into the same NumPy np.log10() method and compare the results.


# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]