import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)
print(df)

df['Contact No'] = 'NA'
print(df)

print(df.drop(columns='Contact No'))
print(df)

print(df.drop(columns='Contact No', inplace=True))
print(df)
