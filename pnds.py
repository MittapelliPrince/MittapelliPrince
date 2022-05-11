import pandas as pd

print(pd.__version__)

a = {'First name': ['Chennaboina', 'Mittapelli', 'Gadamalla'],
        'Last name': ['Ashrith', 'Prince', 'Sai']}

data = pd.DataFrame(a)
print(data)
print(data.loc[0])
print(data.loc[[0, 2]])
data = pd.DataFrame(a, index=['1', '2', '3'])
print(data)
print(data.loc['1'])
print()

print('Series:')
data = pd.Series(a)
print(data)
print()

Names = ['Prince', 'Vamc', 'Sai']
var = pd.Series(Names, index=['1', '2', '3'])
print(var)
print(var[0])
print()

Cars = {'car1': 'Verna', 'car2': 'Lamborghini', 'car3': 'Ferrari'}
variable = pd.Series(Cars, index=['car2', 'car1'])
print(variable)

