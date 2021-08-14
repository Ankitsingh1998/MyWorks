#Day004 - matplotlib
"""
"A picture is worth a thousand words." rings true in data science. 
Data visualization can reveal patterns that are not obvious and communicate 
the insights more effectively. In this part, we will take a look at the 
Matplotlib library, one of the most popular data visualization tools, 
operating on numpy arrays as well as pandas Series and DataFrames. 
By convention, we import the library under a shorter name: 
import matplotlib as mpl

Specifically, the module matplotlib.pyplot, a collection of command style 
functions that make matplotlib work like MATLAB, will be used for the rest 
of the course:
import matplotlib.pyplot as plt

The style can be changed from classic to ggplot, mimicking the aesthetic 
style used in the R package ggplot2.
plt.style.use('ggplot')

matplotlib.pyplot is a collection of functions that make plotting in python 
work like MATLAB. Each function makes some change to a figure, e.g., creates 
a figure, creates a plotting area in a figure, plots lines, annotates the 
plots with labels, etc. as we will see in the following lessons.
"""
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()
plt.show()

import numpy as np
x = np.linspace(0,10,1000) #x is a 1000 evenly spaced numbers from 0 to 10
y = np.sin(x)
fig = plt.figure()
ax = plt.axes()
ax.plot(x, y)
plt.style.use('ggplot')
plt.savefig('sine_function.png')
plt.show()

#with labels and titles
x = np.linspace(0,10,1000) # 1darray of length 1000
y = np.cos(x)

plt.plot(x, y)
plt.legend()
plt.xlim(0,5) #to limit x-axis
plt.ylim(0,1) #to limit y-axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.suptitle('function: cos(x)')
plt.title('graph for cosine function')
plt.savefig("cos_function_for_a_range.png")
plt.show()

#Multiple plots in single graph
x = np.linspace(0,10,1000)
y = np.cos(x)
z = np.sin(x)
plt.plot(x, y, color = 'm', linestyle='--', label = 'cos(x)')
plt.plot(x, z, color = 'y', label = 'sin(x)')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph for cosine vs sine function')
plt.show()
