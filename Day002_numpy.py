#Day002 - numpy
import numpy as np
#Concatenate
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 
           178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 
           182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 
           185, 188, 188, 182, 185, 191] #in cms
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 
        46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 
        43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
height_arr = np.array(heights).reshape((45,1))
ages_arr = np.array(ages).reshape((45,1))

height_age_arr = np.concatenate((height_arr,ages_arr), axis=1) #similar using hstack
print('horizontal addition of array:\n',height_age_arr)
height_age_arr = np.concatenate((height_arr,ages_arr), axis=0) #similar using vstack
print('vertical addition of array:\n',height_age_arr)

#Mathematical operations on arrays: *,/,+,-,**
new_height = height_arr*0.0328084 #in feet
print(new_height[:,0])

#Numpy array method:
new_height.sum() #sum gives sum of all elements in an array
height_age_arr.sum(axis=0) #sums all heights and ages seperately
new_height.min()
new_height.max()
new_height.mean()
new_height.std()

#Comparisons: >, <, ==, !=, >==, <== (returns boolean values)
ages_arr > 55 #returns boolean value
(ages_arr == 55).sum() #to get total satisfying the comparison operator

#Mask and Subsetting:
mask = (ages_arr >= 58)
mask.sum()

old_ages = ages_arr[mask, ]
old_ages
print(old_ages)
old_ages.shape
"""
Masking is used to extract,modify,count or otherwise manipulate values in an 
array based on some criterion(like using comparison operators).
"""

mask1 = (height_age_arr[:,0]>182) & (height_age_arr[:,1]>52)
mask1.sum()

unique = height_age_arr[mask1,]
print(unique)
#Data manipulation in Python is nearly synonymous with Numpy array manipulation

#sololearn code challenge
import numpy as np

n, p = [int(x) for x in input('Enter row number and number of elements: ').split()]
lista = []
for i in range(n):
    lista.append(input('Enter row elements to take their mean: ').split())
mean = np.array(lista).astype(np.float64).mean(axis=1).round(2)
print(mean)
