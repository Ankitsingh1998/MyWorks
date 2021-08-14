#Example - List swapping
num = [15, 12, 13, 17 ,19]
a, b, c, d, e = num
num[0], num[2], num[3] = num[2], num[1], num[0]
print(num)
print(a, b, c, d, e)


nums = (1,4,7,9)
w, x, y, z = nums
print(x, z, y, w)

#Swapping
numbers = (1, 2, 3)
a, b, c = numbers
a, b, c = b, c, a
print(a)
print(b)
print(c)

#Use of *
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a, *b, c, d = num
a, c = b, a
print(a)
print(b)
print(c)
print(d)

#tuples without parentheses
#index and count in tuple
my_tuple = 1,2,3,4,5
print(my_tuple.count(4))
print(my_tuple[3])

#tuple
dir(tuple)