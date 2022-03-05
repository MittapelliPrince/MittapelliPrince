from array import*
arr = array('i', [])

n = int(input('Enter the length of array: '))

for i in range(n):
    x = int(input('Enter the value: '))
    arr.append(x)

print(arr)

val = int(input('Enter value for search: '))

print(arr.index(val))
