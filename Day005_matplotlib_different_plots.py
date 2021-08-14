#Day005 - different plots in matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('professors.csv')

#scatterplot:
plt.style.use('ggplot')
plt.scatter(df['age'], df['salary'], marker='$d$', color = 'k') #for more markers see documentation
plt.xlabel('age')
plt.ylabel('salary')
plt.title('age vs salary distribution for professors')
plt.show()

#plotting with pandas
plt.style.use('ggplot')
df.plot(kind='scatter', x = 'salary', y = 'age', title='age vs salary distribution for professors', color='r')
plt.legend()
plt.show()

#Histogram
df['salary'].plot(kind='hist', title='salary distribution', bins=10, color='k', legend=True)
plt.show() #Method 1

plt.hist(df['salary'],bins = 10, color='c')
plt.legend('salary')
plt.show() #Method 2

df['salary'].hist(color='b', legend=True)
plt.show() #Method 3

#Boxplot
print('Information about the salary of professors is: \n'+str(df['salary'].describe()))
plt.style.use('classic')
df.boxplot(column='salary')
"""
info about boxplot:
lower and upper black whiskers --> minimum and maximum
red bar -=> median
blue box --> IQR(Interquartile range, i.e., between the first and third quartile), 50% data will fall in this range
"""

#Barplot
discipline_counts = df['discipline'].value_counts()
plt.style.use('classic')
discipline_counts.plot(kind='bar', legend = True, color='g')
plt.xlabel('different discilplines')
plt.ylabel('number of similar disciplines in the college')
plt.suptitle('classic barplot')
plt.title('distribution of different disciplines and their counts')
plt.show()

#sololearn code challenge missing numbers
#input_data = 5 4 8 7 9 nan 8 7 9 nan 7 8 9 10
#Method 1:
lst = [float(x) if x != 'nan' else np.NaN for x in input('Pass the input_data: ').split()]
lst = np.array(lst)
lst = pd.Series(lst)
lst = lst.fillna(lst.mean()).round(1)
print(lst)

#Method 2:
lst = [float(x) if x != 'nan' else np.NaN for x in input('Pass the input_data :').split()]
lst = np.array(lst)
lst = pd.DataFrame(lst, columns=[''])
lst = lst.fillna(lst.mean()).round(1)
print(lst)
print(lst.dtypes)
