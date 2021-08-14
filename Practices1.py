#Beginning
print('Hello world!')
print('Hello world!')
print('Spam and eggs...')
print('Python rocks....!')
print("Python is fun!")
print('Always look on the bright side of life')
print("I'm gonna make it")

#Odd/Even number
x = 1
while x <= 10:
    if x%2 == 0:
        print(str(x) + ' is an even number.')
    else:
        print(str(x) + ' is an odd number.')
    x = x + 1 
    
#Odd/Even inside a range
for x in range(0,20):
    if x%2==0:
        print(x, 'is an even number.')
    else:
        print(x, 'is an odd number.')
        
#Odd/Even using generators
a = int(input('Enter a number: '))

def even_numbers(x):
    for i in range(x+1):
        if i % 2 == 0:
            yield i
print('List of even numbers:',list(even_numbers(a)))

def odd_numbers(x):
    for i in range(x+1):
        if i % 2 != 0:
            yield i      
print('List of odd numbers:',list(odd_numbers(a)))


   

#list functions
ara = ['Winter', 'Spring', 'Summer', 'Fall', 'Cold', 'Hot']
print(min(ara))
print(max(ara))
print(len(ara))
ara.append('Rabbit')
ara.insert(4,'Start')
ara.insert(5, 'Spring')
print(ara)
print(ara.index('Summer'))
print(ara.index('Start'))
print(ara.index('Cold'))
print(ara.count('Spring'))
ara.reverse()
print(ara)
ara.remove('Winter')
print(ara)
ara.reverse()
print(ara)

#Range function
numbers = list(range(3, 8))
print(numbers)
print(range(20,0) == range(0, 20))
print(range(11) == range(0, 11))
print(range(8) or range(0, 7))
print(range(0,16) and range(22))
print(list(range(20,0)))

#multiple of 5
a = [2,5,10,7,18,25]
for data in a:
    if data%5==0:
        print('amk is a multiple of 5.')
    else:
        print(data)

#Same argument outside codeblock
def function(variable):
    variable += 10
    print(variable)
function(7)
function(91)
variable = "Summer",'Winter','Spring','Fall'
print(variable)

#which character has less number of letters:
def shortest_string(x,y):
    if len(x)>len(y):
        return y + ' is smaller.'
    elif len(x)<len(y):
        return x + ' is smaller.'
    elif len(x)==len(y):
        return 'Both characters have same letters.'
print(shortest_string(str(input('Enter first word: ')),str(input('Enter second word: '))))
z = shortest_string('Ankit','Chetan')
print(z)

#return statement
def add_numbers(x, y):
    total = x + y
    divisor = x/y
    print("This will get printed.")
    print(divisor)
    return total
    return divisor
    print('This will not get printed.')
z = add_numbers(5,6)
print(z)

#celsius to fahrenheit converter
celsius = int(input('Enter temperature in celcius: '))
def conv(c):
    return (9/5*c + 32)    

fahrenheit = conv(celsius)
print(fahrenheit)

#prime numbers in a range iof given numbers.
print('Please provide a number below which you want to print all prime and non-prime numbers.')
num = int(input('Enter your number: '))
for p in range(2,num+1):
    for i in range(2,p):
        if p%i==0:
            print(p, 'is not a prime number.')
            break
    else:
        print(p, 'is a prime number.')

#prime number
num = int(input('Check for a prime number, \n Enter your number: '))
for i in range(2,num):
    if num%i==0:
        print(num, 'is not a prime number.')
        break
else:
    print(num, 'is a prime number.')

#Co-prime numbers:
a = int(input('Smallest Number : '))
b = int(input('Largest Number : '))
if a>1 and b>1:
    for c in range(2,a+1):
        if a%c==0 and b%c==0:
            print(a, 'and', b,'are not co-primes.')
            break
    else:
        print(a,'and',b,'are co-primes.')

#All Co-primes between a range:
x = int(input('Smallest number: '))
y = int(input('Largest number: '))
if x>1 and y>1:
    for a in range(x,y+1):
        if a>1:
            for b in range(2,a):
                if b>1:
                    for c in range(2,b+1):
                        if b%c==0 and a%c==0:
                            print(a,'and',b,'are not co-primes.')
                            break
                    else:
                        print(a, 'and',b ,'are co-primes.')

#Factorial of a number:
n = int(input('Enter the number: '))
Factorial = 1
if n < 0:
    print('Factorial of negative number doesn\'t exists.')
elif n==0:
    print('Factorial of 0 is 1.')
else:
    for i in range(1,n+1):
        Factorial = Factorial*i
    print('Factorial of ' , n , 'is' , Factorial, '.')

#Longest word - re.findall
import re
txt = input('Enter your sentence here: ')

a = re.findall(r"[\w']+", txt)

b = [len(a[x]) for x in range(len(a))]
print(a[b.index(max(b))])

#Longest and shortest word
import re
txt = ('Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,totam rem aperiam.Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')

new = txt.replace('.',' ').replace(',',' ').split(' ')
print(new)
print('')
b = [len(new[x]) for x in range(len(new))]
print(new[b.index(max(b))])
print('')
print(new[b.index(min(b))])

#reverse countdown
def countdown():
    i=int(input('Enter a number: '))
    while i >= 0:
        yield i
        i -= 1

for i in countdown():
    print(i)




