import pandas as pd


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

df = pd.DataFrame({'list1': list1, 'list2': list2})

print(df.head(3))
