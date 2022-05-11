import pandas as pd

d = pd.read_excel("C:\\Users\\sentryeagle\\Desktop\\Employee.xlsx")
df = pd.DataFrame(d)

print(df.sort_values('Em_Name'))
print()
print('Sorting Descending order of Em_Address')
print(df.sort_values('Em_Address', ascending=False))

print(df.sort_values(['Em_Address', 'Em_Email_id']))

print(df.sort_values(['Em_Email_id', 'Em_id'], ascending=[0,1]))
