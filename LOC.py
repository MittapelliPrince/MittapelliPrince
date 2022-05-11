import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)

print(df.loc[2])

print(df.loc[5,['Em_Name', 'Em_Address']])

print(df.loc[3:7])
print()
print('Indexing by Column Name using Strtng pos and Endng pos')
print(df.loc[4:6, 'Em_Address'])

print(df.loc[3:6, ['Em_id', 'Em_Address']])

print(df.loc[1:4, 'Em_id': 'Em_Name'])
