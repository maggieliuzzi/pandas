import pandas as pd

# 1)
# users = pd.read_csv('dataset/users.csv', index_col=0)
# print(users)

# 2)
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitors': [139, 237, 326, 456],
        'signups': [7, 12, 3, 5]}

users2 = pd.DataFrame(data)
print(users2)

# 3)
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']

list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays] # list of lists

zipped = list(zip(list_labels, list_cols)) # list of tuples (column names and columns)
print(zipped)

data3 = dict(zipped)
users3 = pd.DataFrame(data3)
print(users3)

# Broadcasting - Saves time by generating long list arrays or columns without loops
users3['fees'] = 0 # Broadcasts to entire column
print(users3)

heights = [59.0, 64.5, 21.5, 12.5, 75.7, 78.7]
data4 = {'heights': heights, 'sex': 'M'} # dict
results = pd.DataFrame(data4)
print(results)

# Changing columns and index labels
results.columns = ['height (in)', 'sex']
# or list_labels = [ ... ], results.columns = list_labels
results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(results)
# Can assign lists of strings to the attributes columns and index as long as they are of a suitable length
# (number of rows and columns respectively)

# Broadcasting:
state = 'PA'
# Construct a dictionary: data
data = {'state':state, 'city':cities}
# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)
print(df)