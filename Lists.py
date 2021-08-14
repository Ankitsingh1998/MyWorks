#Lists
words = ["Hello", "world", "!"]
print(words[0] , words[1] , words[2])
 
a = 'Python'
b = 'coding'
c = 'Rocks'
print(a, b, c,',', 'Esmaart!')

#List element addition
nums = [float(input('Enter number, a: ')), float(input('Enter number, b: ')), float(input('Enter number, c: '))]
sims = [float(input('Enter number, d: ')), float(input('Enter number, e: ')), float(input('Enter number, f: '))]
a = [nums[0] + sims[0], nums[1] + sims[1], nums[2] + sims[2]]
print(a)
print(a * 3)

#List function - append
nums = [1, 2, 3]
nums.append('spring')
print(nums)
print(nums[3])

#List function - insert
words = ['Spring','Winter','Summer']
words.insert(1, "Fall")
print(words)
print(words[2],words[0],words[3],words[1])

#List functions
a = float(input('Enter number, a: '))
b = float(input('Enter number, b: '))
c = float(input('Enter number, c: '))
d = float(input('Enter number, d: '))
e = float(input('Enter number, e: '))
f = float(input('Enter number, f: '))
g = float(input('Enter number, g: '))
h = float(input('Enter number, h: '))
num = [a,b,c,d,e]
print(num.index(a))
print(num.index(c))
print(num.index(e))
print(max(num))
print(min(num))
num.append(f)
num.insert(0,g)
print(num)
print(len(num))
print(num + [h])
print(num.count(a))
num.remove(b)
print(num)
num.reverse()
print(num)

#List slicing
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[-5:-1])
print(squares[2:7])
print(squares[-5:1])
print(squares[-6:7])
print(squares[-3:9])
print(squares[:-2])
print(squares[-10:12])

#List comprehensions, average of squares of even numbers
m = int(input("Enter your number: "))
evens=[
         i**2 for i in range(m) 
                 if i**2 % 2 == 0
                                   ]
print(evens)
if m %2==0:
    a = int(m/2)
    print('a is:',a)
else:
    a = int((m+1)/2)
    print('a is:',a)
x = 1
for x in range(1,a):
    evens[x] = evens[x] + evens[x-1]
print(evens[a-1]/(a))

# string formatting
nums = [4, 5, 6, 7, 8]
msg = "Numbers: {0} {1} {1} {2} {0} {3}". format(nums[0], nums[1], nums[4], nums[3])
print(msg)

#List functions
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
else:
    print('Atleast one is smaller than 5')
    
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
else:
    print('No one is even')

for v in enumerate(nums):
    print(v)

stg = ['Ankit','Aman','Amar','Anukul']

if all([(len(stg[i]) == 5) for i in range(4)]):
    print('All characters are of same length.')

else:
    print("All characters are not of five letters.")

if any([(len(stg[i]) == 4 or 6) for i in range(4)]):
    print('Atleast one character has four or six letters in it.')

else:
    print("No character has either four or six letters in it.")

for x in enumerate(stg):
    print(x)

#Booklist_example_sololearn
Booklist = ['Harry Potter' , 'Pride and Prejudice' , 'Sherlock Holmes' , 'Papillion' , 'Benjamin Franklin']

x = 0
for x in range(len(Booklist)):
    Booklist[x] = Booklist[x]
    print(Booklist[x][0] + str(len(Booklist[x])))
    continue

#Lambda function
add = lambda x : x + 5
subtract = lambda x , y : x - y
multiply = lambda z , y : z * y
divide = lambda a , z , y , x : ((a*z)**y)/(x**2.5)
print(multiply(5,3))
print(subtract(8,3))
print(add(8))
print(divide(divide(5,3,2,8),subtract(9,2),add(13),multiply(5,9)))

#use of filter
nums = [11, 22, 33, 44, 55]
odd = list(filter(lambda x: x%2!=0, nums))
print(odd)

evens = list(filter(lambda x: x%2==0, nums))
print(evens)

#reverse of a list, map, and lamda
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print('result is:',result)

reverse = [result[len(result)-1-a] for a in range(len(result))]
print('reverse of result is:',reverse)

num = [12, 24, 36, 48, 60]

div_12 = list(map(lambda x : x/12, num))
print('div_12 is:',div_12)

rev = [div_12[len(div_12)-1-a] for a in range(len(div_12))]
print('reverse of div_12 is:',rev)

















