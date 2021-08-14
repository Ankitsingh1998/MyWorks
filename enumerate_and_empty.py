#enumerate:
"""
enumerate(iterable, start=0)
start = 0 by default, can be assigned with different number.
"""
l1 = ['eat','sleep','repeat']
s1 = 'geeks4geeks'
obj1 = enumerate(l1)
obj2 = enumerate(s1)

type(obj1)
type(obj2)

print(list(obj1))
print(list(obj2))

obj3 = enumerate(s1, 100)
print(list(obj3))

obj4 = enumerate(l1, 0)
for ele in obj4:
    print(ele)

obj3 = enumerate(s1, 100)
for count,ele in obj3:
    print(count,ele)

dict1 = {}
obj3 = enumerate(s1, 100)
for count,ele in obj3:
    dict1[ele] = count
    
    
#empty:
"""
numpy.empty(shape, dtype = float, order = 'C')
shape --> number of rows and columns or dimension of array
order --> C_contiguous or F_contiguous
dtype --> optional, float by default (Data Type of returned array)
"""
import numpy as np
a = np.empty([1,2], dtype=int)
b = np.empty([1, 2, 1], dtype=int)
c = np.empty([2, 1], dtype=int)
d = np.empty([2], dtype=int) #d & e are same
e = np.empty(2, dtype=int)
f = np.empty([2, 2], dtype=int)
g = np.empty([3, 3], dtype=int)


#empty_like:
"""
numpy.empty_like(shape, dtype = None, order = 'K', subok=True)
shape --> number of rows and columns
order --> C_contiguous or F_contiguous
dtype --> optional, float by default (Data Type of returned array)
subok --> bool, optional - to make subclass of shape or not
"""
h = np.empty_like([2,2], dtype=float)
i = np.empty_like(([1,2,3],[4,5,6]), dtype=int)
j = np.empty_like([2, 4, 2], dtype=float)

#Contiguous and non-contiguous allocation: ways of organizing program in memory
"""
Contiguous Allocatuion:
    program must exist as a single block of contiguous address.
    sometimes, it is impossible to find large enough block.
    low overhead on OS.

Non-contiguous Allocation:
    programs is divided into chunks called segments.
    Each segment can be placed in different parts of memory.
    Easier to find 'holes' in which segmemnt it will fit.
    holes --> holes are free space.
"""
