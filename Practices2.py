#Recursion - Factorial of a number
a = int(input('Enter a number: '))
def factorial(x):
    if x<0:
        return 'Factorial of negative number do not exists.'
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(a))

#Recursion - letter reversal of a word
def spell(txt):
    #your code goes here
    if len(txt) == 1:
        return txt[len(txt) - 1]
    else:
        return spell(txt[1:]) + '\n' + txt[0]
txt = input('Enter a text to get reversed: ')
print(spell(txt))

#Recursion - Sum of n natural numbers
x = int(input("Sum of n natural numbers:\nEnter a number: "))
def sum_to(x):
    if x==0:
        return 0
    else:
        return x + sum_to(x-1)
print (sum_to(x))

#Recursion - Odd/Even
a = int(input('Enter a number: '))
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(a))

#Recursion - Power of a number
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

a = int(input('Enter base number: '))
b = int(input('Enter power number: '))
print(power(a, b))

#Recursion - Fibonacci
print('Fibonacci series upto nth term:')
num = int(input('Enter term number: '))

def fibonacci(n):
	#complete the recursive function
	if n<=1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

if num<=0:
    print('Fibonacci will not exist.')
else:
    for i in range(num):
        print(fibonacci(i))

#OOP
print('Calculate the area of the rectangle:')
width = int(input('Enter width of the rectangle: '))
height = int(input('Enter height of the rectangle: '))
class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        if width == height:
            print('Quadilateral became a square with area:\n'
            ,self.width*self.height,'cm^2')
        else:
            print('Area of rectangle with its width and height as',width,
        '&',height,
        'cms respectively is:\n',self.width*self.height,'cm^2')
rect = Rectangle(width,height)
rect.area()
    
#random module
import random
name = ['Ankit','Aman','Ronny','Ajju','Rocxxy']
for i in range(len(name)):
    a = -i
    b = len(name) -1 - i
    print(name[i + random.randint(a,b)])  
print()
print(name[random.randint(0,len(name)-1)])
print()
print(dir(random))

#Maximum and minimum
def maximum(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        print('Both are same numbers.')
print('largest string is: '+ maximum(input('Enter first word: '),input('Enter second word: ')))

print(min(range(27,9,-1)))

#Find word inside a text
import re
text = input('Provide any text: ')
word = input('Type the word you want to find: ')

def search(text,word):
    check = re.findall(r"[\w']+", text)
    if word in text:
        return 'Word found'
    else:
        return 'Word not found'

print(search(text, word))

#Practice questions 11/06/2021:
#Question. 1.
arr = [4,3,1,2]
arr[0],arr[arr[0]-1] = arr[arr[0]-1],arr[0]
print(arr)

#Question. 2.
def ishashable(x):
    try:
        set = {x}
        return True
    except TypeError:
        return False
print(ishashable(2),ishashable([2]))

#Question. 3.
def A(x):
    x+=1
    print(x)
def B(x):
    x*=1
    print(x)
a=1
b = int(a/2)
if a and b:
    A(a)
else:
    B(b)

#Question. 4.
a = '4'
print(a*3)

#Question. 5.
a = (7,)
b = (7)
print(int(type(a)==type(b)))
print(type(a)==type(b))

#Average word length of a text
text = input('Provide a text: ')
new = text.split()
i = 0
for i in range(len(new)-1):
    new[i+1] = new[i+1] + new[i]
x = len(new[len(new)-1])

avg_len = x/len(new)
print(avg_len)

#Shortest distance among given coordinates
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

#your code goes here

distances = []

for (x,y) in points:
    distance = ((x**2) + (y**2))**(0.5)
    distances.append(distance)
   
print(distances)
print(min(distances))
print(max(distances))
print(points[distances.index(min(distances))])
print(points[distances.index(max(distances))])

#Revenue collection for a cinema hall ticket
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input('Enter age of the person: '))
ages = []
for value in data.values():
    value = value
    ages.append(value)
above_18 = []
below_18 = []

for i in ages:
    if i >= 18:
        above_18.append(i)
    else:
        below_18.append(i)

revenue_above_18 = 20*len(above_18)
revenue_below_18 = 5*len(below_18)
total_revenue = revenue_above_18 + revenue_below_18

above_age = []
below_age = []
for i in ages:
    if i >= age:
        above_age.append(i)
    else:
        below_age.append(i)

revenue_above_age = 20*len(above_age)
revenue_below_age = 5*len(below_age)
new_total_revenue = revenue_above_age + revenue_below_age
profit = ((new_total_revenue - total_revenue) / total_revenue)*100
print(int(profit))

#regex - email extraction
import re
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact it.hub1992@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())

#Phone number validator
import re
phone_number = input('Enter an eight digit phone number: ')
pattern = r"[1|8|9]([0-9]+)"
match = re.match(pattern,phone_number)
if match and len(phone_number) == 8:
    print('Valid')
else:
    print('Invalid')

#Concatenation
def concatenate(*add_words):
    add_words = list(add_words)
    for i in range(len(add_words) - 1):
        add_words[i+1] = add_words[i] + "-" + add_words[i+1]
    return add_words[len(add_words) - 1]

print(concatenate("I", "love", "Python", "!"))








