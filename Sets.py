#Sets
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
a = first | second
b = first & second
c = first - second
d = second - first
e = first ^ second
print(a)
print(b)
print(c)
print(d)
print(e)

#^ == | - &
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
if a^b == (a|b) - (a&b):
    print(True)

else:
    print(False)

#list and set
from itertools import *
num = list(accumulate(range(8)))
print(num)
num2 = list(takewhile(lambda x: x<10,num))
print(num2)
num3 = list(range(8))
print(num3)
num4 = list(chain(num,num3))
print(num4)
num5 = set(chain(num2,num3))
print(num5)
num6 = [2,5,8,7,1,3,4,6,1,9]
print(list(accumulate(num6)))





#example of set conversion
lis1 = [ 3, 4, 1, 4, 5 ]
 
tup1 = (3, 4, 1, 4, 5)
 
# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))
 
# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))



#next function:
list2 = [2,4,1,3,7,5,6,3]
list2 = iter(set(list2)) #iter function

print('List contents are: ')
while (1): #In bollean, True and 1 are same -  infinite loop.
    val = next(list2,'sayonara')
    if val == 'sayonara':
        print('List ended')
        break
    else:
        print(val)

