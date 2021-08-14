#Day003 - pandas
import pandas as pd
import numpy as np

#series - one building blocks in pandas, and can hold data of any type
#Series are as numpy 1darray with index or row names.
item_list = pd.Series([1, 2, 3], index=['a', 'b', 'c']) # with index
print(item_list)


item_list2 = pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c']) # from a numpy 1darray
print(item_list2)

item_list3 = pd.Series({'a': 1, 'b': 2, 'c':3}) # from a dict
print(item_list3)
item_list3[0] #using numeric indexes
item_list3['b'] #using keys - similar for arrays

#DataFrame construction using a dictionary
wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine':[5, 0, 10]
}
wine_sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"]) #dataframe construction
wine_sales['white_wine'] #calling a column

#shape and size of a dataframe
wine_sales.shape
wine_sales.size
wine_sales.shape[0] #row numbers
wine_sales.shape[1] #column numbers

#head and tail
wine_sales.head(n=2)
wine_sales.tail(n=2)

#info - to get an overview of our dataframe
wine_sales.info()

#loc function - when we don't know the integer position
wine_sales.loc['bob']
wine_sales.loc['bob'].shape
wine_sales.loc['bob':'charles'] #index slicing
wine_sales.loc['bob':'charles'].shape

#iloc - when we know the integer position
wine_sales.iloc[:,:1]

#columns
wine_sales.columns

wine_sales.loc[:,'red_wine':'white_wine']
wine_sales.loc[:,'red_wine']
wine_sales.loc[:,'white_wine']

#statistics
wine_sales.min()
wine_sales.max()
wine_sales.mean()
wine_sales.var()
wine_sales.std()
wine_sales.median() #divides data into two parts(50-50%), similar to quantile(0.5)
wine_sales.quantile([0.25, 0.5, 0.75, 1.0]) #divides data into four parts (25-25%)
wine_sales.describe() #gives all statistics values except variance
#describe ignores the null values, NaN(Not a Number)
wine_sales['white_wine'].value_counts()
"""
A categorical variable can take on only one values from a variety of categories.
"""

#groupby and aggregate
df = pd.read_csv('professors.csv')
df.groupby('discipline')['salary'].mean()
df.groupby('discipline')['salary'].agg(['min', np.median, max, np.mean])
#agg can take string, function or a list.
aggregated = df.groupby('discipline').agg({'salary':[min, max, np.mean, np.std],
                              'age':[min, max]})
#for different columns properties we can use dictionaries

#sololearn code challenge - reshape
import numpy as np
r = int(input('Enter number of rows: ')) 
lst = [float(x) for x in input('Enter a list ').split()]
arr = np.array(lst)
arr = arr.reshape(r,int((len(lst)/r)))
print(arr)

