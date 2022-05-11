import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)

print(df.iloc[1: 3])

print(df.iloc[3:7, 2:])

print('Indexing by rows and columns')
print(df.iloc[5:, 3])

print(df.iloc[[3, 5, 9]])

print(df.iloc[:, 1:])

print(df.iloc[4:9, [1, 3]])

print(df.iloc[[1, 2, 3], [1, 2]])
