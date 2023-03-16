import pandas as pd


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

df = pd.DataFrame({'list1': list1, 'list2': list2})

df.list1.mean()
df.list2.mean()

print(df.list2.mean())

df.list1.min()
df.list2.max()
print(df.list2.max())

df.list1.describe()

print(df.list1.describe())
