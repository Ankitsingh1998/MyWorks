#Python arrays:
"""
An array is a collection of items stored at contiguous memory locations. The 
idea is to store multiple items of the same type together. This makes it 
easier to calculate the position of each element by simply adding an offset to 
a base value, i.e., the memory location of the first element of the array 
(generally denoted by the name of the array).
"""    
#An array must contains similar items/data types - array(data_types, value_list)
#A list can store different data types

import array as arr
dir(arr)

a = arr.array('i', [1,2,3])
a[0] #to call an element
a[2]

for i in range(2):
    print(a[i],end=' + ')
print(a[2],'=',a[0]+a[1]+a[2])

b = arr.array('d', [1,2.5,3.9])
b[0]

for i in range(2):
    print(b[i],end=' + ')
print(b[2],'=',b[0]+b[1]+b[2])

a.insert(1,5) #to insert an item in the array at fixed index
print(a)
print(len(a))
for i in range(len(a)-1):
    print(a[i],end=', ')
print(a[len(a)-1])

b.append(4.2) #to insert an item in an array at last index, we use append
b.insert(2,6.5)
b.insert(2, 2.8)
print(b)

b.pop(3) #pop --> to remove from a particular position
b.remove(2.8) #remove --> to remove a particular element from the array
print(b)

a[0:2] #slicing similar to list slicing
a[::-1] #reverse slicing

c = arr.array('d', [])
for i in range(len(a)):
    c.append(a[i])

d = c + b #array addition
d.index(5) #gives index of the element
d.index(3.9)

print(d)

d[2] = 2.4 #updating element of an array
d[3] = 3.6
print(d)
