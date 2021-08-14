#Grade viewer
grade = float(input('You have obtained: '))
if (grade >= 33) and (grade <= 100):
    print("Congrats, You\'re Pass!") 
elif (grade) < 0 or (grade > 100):
    print('Calculation error!')
else:
    print('You have to reappear!')
    
#Comparing two numbers   
x = float(input('First number is x: ') )
y = float(input('Second number is y: '))
if x > y:
  print("x > y")
elif x==y:
    print('x = y')
else:
    print('y > x')

#Biodata of a person inside a list
Name = str(input('Name of the person: '))
Age = int(input('His age is: '))
Blood_group = str(input('His blood group is: '))
Data = [Name,Age,Blood_group]
print(Data[0])
print(Data[1])
print(Data[2])

# a*x**2 + b*x + c = 0
# To solve a quadratic equation
a = float(input('Coefficient of x^2 is a: '))
b = float(input('Coefficient of x is b: '))
c = float(input('Constant is c: '))
D = b**2 - 4*a*c
sol1 = (-b + D**0.5) / (2*a)
sol2 = (-b - D**0.5) / (2*a)
Sol1 = Sol2 = -b/(2*a)
if D>0 :
    print(sol1, sol2)
elif D==0 :
    print(Sol1, Sol2)
elif D<0 :
    print('This quadratic equation has imaginary roots.')

#while loop - by taking input
i = float(input('Enter a number: '))
while i >= 1:
    print(i)
    i = i - 1
    print(i)
    
#While loop 1.0
i = 1
while i <=5:
    print(i)
    print(i+1)
    print(i-3)
    i = i + 1
    print(i)
    print(i+1)
    print(i+3)
    print(i-1)
    print(i-3)
    
#while loop 2.0
i = 0
while True:
    print(i)
    i = i + 1
    if i < 8:
        continue
    elif i >= 8:
        print('Breaking.')
        break
print("Finished")

#Boolean value
print(1==1 or False)

#continue statement:
i = 1
while i<=5:
  print(i)
  i+=1
  if i==4:
    print("It\'s number 4.")
    continue

#break inside for loop
words = ["hello", "world", "spam", "eggs"]
for a in words:
    if a == 'spam':
        break
    else:
        print(a + "!")
        
#continue inside for loop
words = ["hello", "world", "spam", "eggs"]
for a in words:
    if a == 'spam':
        continue
    else:
        print(a + "!")

#while loop with range function
i = 2
while i in range(5):
    print("hello!")
    i+=1

#for loop with range function
for i in range(2,5):
    print("hello!")

#arguments usage
def arg(word,word2):
   print((word + "!"),(word2 + ':'))
   print(word2 + ':')
arg("spam",'hi')
arg("eggs",'you')
arg("python",'is fun')

#multiple arguments
def print_sum_twice(x, y):
   print(x + y)
   print(x - y)
print_sum_twice(5, 8)

#while inside a function
def function(variable):
    while variable<=10:
        print(variable)
        variable += 1
function(2)

#function, argument and return
def fruits():
    print('Guava')
    print('Mango')
    print('Orange')
    print('Pomegranate')
    print('Pineapple')
    return
    print('Banana')
    print('Tomato')

fruits()

#modules
import math
print('Napier\'s constant is: ', math.e)
print('Value of pi is: ',math.pi)
print(dir(math))
help(math.radians(x))

#as use for modules
from math import *
from math import e as Napiers_constant
print(Napiers_constant)

from math import pi as Value_of_pi
print(Value_of_pi)

from math import sin as sinusoidal_function
print(sinusoidal_function(pi/2))

#math module
import math as m
print(m.e)
print(m.pi)

#None object - when return is not used
def some_func(x):
    if x==4:
        print(x,"is True.")
var = some_func(4)
print(var)

#Higher-order function:
#First input will be taken by number we are operating,
#Second input will be taken by func1 which is add,
#Third input will be taken by func2 which is multiply,
#Fourth input will be taken by func3 which is subtract,
#Fifth input will be taken by func4 which is divide.
#Using only these five functions multiple operations can be done with multiple variable constants and coefficients:
def apply_multi(func4, func3, func2, func1, arg):
    return func4(func3(func2(func1(arg))))

def add(x):
    return x + float(input('Enter second number: '))

def subtract(y):
    return y - float(input('Enter fourth number: '))

def multiply(z):
    return z*float(input('Enter third number: '))

def divide(a):
    return a/float(input('Enter fifth number: '))

print(apply_multi(divide, subtract, multiply, add, float(input('Enter first number: '))))

#generator
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

#Impure function
some_list = []
def impure():
    some_list.append('spam')

print(impure())
print(some_list)

#Pure function
x = int(input('Enter the number, x: '))
y = int(input('Enter the number, y: '))
def pure(x,y):
    temp = x + 2*y
    return temp/(2*x + y)

print(pure(x,y))

#Docstring
print("""this
is a
multiline
text""")

#Counting with for loop
str = "testing for loops"
count = 0

for x in str:
    if(x == 't'):
        count += 1

print(count)

#Boolean logic
print(int(True))
print(int(False))

#random module
import random

print(random.randint(-5,5))
print(dir(random))
help(random.triangular())

#The zen of python
import this

#function argument - *args
def function(Person_name, *Biodata):
    print(Person_name)
    print(Biodata)
    Bio = list(Biodata)
    print(Bio)

function("Keyaru", "Age = 19", "Blood Group = B+", "Height = 164cm", "Weight = 64.5kg")

#function argument - default values
def function(x, y, food="spam", pet = 'cat'):
    print(food)
    print(pet)
function(1, 2)
function(3, 4, "egg")
function(6,7,"egg","dog")

#function arguments - **kwargs
def my_func(x, y=7, *num, **new_nums):
    print(x)
    print(y)
    print(num)
    print(new_nums)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#Ternary operator
a = int(input('Enter the number, a: '))
b = 1 if a >= 5 else 42
print(b)

status = int(input('Enter keyword to check the status: '))
user = "Logout" if status == 1 else "Login"
print(user)

#More on else statement - else with for/while loop
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

#More on else statement - else with try/except
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

#__main__ function
def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")

#function
def my_func():
    print("spam")
    print("and")
    print("eggs.")

my_func()

"""
end():
    In python 3.0, 
    end can be give at last of print to add any character as a string.
"""
print('Python ')
print('is Fun!')
print('Python ',end='')
print('is Fun!')
"""
opposite of '\n'/newlines. end='input()' will connect two print statements
with the character we provide.
"""
print('Python ')
print('is Fun!')
print('Python ',end=input('Enter a character: '))
print('is Fun!')
