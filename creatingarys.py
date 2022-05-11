from array import *
arr = array('i', [34, 54, 12, 76])
print(arr)

for i in arr:
    print(i)

# Creating array using input
newarr = array('i', [])
n = int(input('Enter the length of array: '))

for i in range(n):
    x = int(input('Enter the values: '))
    newarr.append(x)

print(newarr)

a = int(input('Enter for search value: '))

y = 0
for j in newarr:
    if j == a:
        print(y)
        break
    y += 1


newarr.extend([64, 28, 54])
print(newarr)
print(newarr.index(a))
