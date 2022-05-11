import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)
print(df)
print()

print(df.head())
print()

print(df.head(8))
print()

print(df.tail(3))

print(df.describe())
print()

print('Rows and Columns:')
print(df.shape)

print(df[0:7:2])
print()
print('Indexing by Coloumn name')
print(df['Em_Name'])
print('Indexing multiple columns')
print(df[['Em_Name', 'Em_Address']])

print(df[['Em_id', 'Em_Name']][2: 8: 2])
print()

for data in df.iterrows():
    print(data,'\n')