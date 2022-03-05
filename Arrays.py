from array import*

arr = array('i',[87,34,76,90])
print(arr)

print(arr.buffer_info())

arr.append(45)
print(arr)

print(arr.index(87))

newarr = array(arr.typecode, (x for x in arr))
print(newarr)

for i in range(len(arr)):
    print(arr[i])
    
