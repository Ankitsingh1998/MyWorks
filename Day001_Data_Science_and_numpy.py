#Data Science
#Day001 - Data Science and numpy
"""
Why Data Science?? Uses??
Zillow - algorithm to predict better pricing to find houses,
finding key attribues associated with wine quality,
Building a reccomendation system to increase the click-through-rate for amazon.
"""
"""
collecting data
cleaning data
performing EDA(Exploratory Data Analysis)
Building and evaluating ML models
communicating insights to stakeholders
-unifies statistics, data analysis, ML for extraction.
"""
"""
EDA(Exploratory Data Analysis):
    numpy
    pandas
    matplotlib
    scikit-learn
"""
#numpy:
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 
           178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 
           182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 
           185, 188, 188, 182, 185, 191]

count = 0
for height in heights:
    if height > 188:
        count+=1
print(count)

#(numpy) array conversion of list makes it easier and faster to approach the same problem
import numpy as np
height_arr = np.array(heights)
print((height_arr>188).sum())
height_arr.size #similar to len
height_arr.shape
height_arr.ndim

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 
        46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 
        43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights+ages
height_n_age = np.array(heights_and_ages)
height_n_age.shape
new_height_n_age = height_n_age.reshape(2,45)
new_height_n_age.shape
new_height_n_age.dtype

#Indexing and Slicing:
new_height_n_age[1][2] #To call an index
new_height_n_age[1,1:18:4] #sliciing arr[row_no,start:stop:step], row slicing
new_height_n_age[0,::3]
new_height_n_age[0,-10::2] #left to right even for negative indexing
new_height_n_age[::,5] #slicing arr[start:stop:step,column_no], column slicing

#Assigning values:
height_arr[3] = 165 #new value assigned
new_height_n_age[0,3] = 165 #new value assigning in 2D array
height_arr[:] = height_arr.mean() #slicing to assign all values mean value of the array
new_height_n_age[:2,:2] = 0 #assigning first two values 0 by using slicing
new_height_n_age[:,0] = [190,58] #assigning in a row
new_height_n_age[:,1] = [184,56]

#assigning multiple rows
new_record = np.array([[165,178,182],[56,46,59]])
new_height_n_age[:,36:39] = new_record #[column_number(:),row_number(:)]

#Combining two arrays:
ages_arr = np.array(ages)
ages_arr.shape
ages_arr[:33:4]
height_arr.shape
height_arr.reshape((45,1))
height_age_arr = np.hstack((height_arr,ages_arr)) #horizontal combining of arrays, only if same number of rows
height_age_arr.shape
height_age_arr[:34:5]
height_age_arr = np.vstack((height_arr,ages_arr)) #vertical combining of arrays
height_age_arr.shape
height_age_arr[:1,3:34:4]
