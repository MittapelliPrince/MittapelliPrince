data = {1: 'Python', 2: 'Pycharm', 3: 'Sublime'}
print(data)

print(data[1])

data[4] = 'Jupyter'
print(data)

data2 = {1: 'sai', 2: 'kiran', 3: ['kumar', 'sharath'], 4:{'suman': 'Suresh', 'vinay': 'shravan'}}
print(data2)

print(data2[3])

print(data2[3][0])

print(data2[4]['suman'])

keys = {5, 6, 7}
values = {'sravan', 'raghu', 'vamc'}
data3 = dict(zip(keys, values))
print(data3)
