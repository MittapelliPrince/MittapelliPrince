import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)
print(df)

print(df.duplicated())

print(df.drop_duplicates())