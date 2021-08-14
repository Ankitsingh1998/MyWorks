#Exception handling 1.0
try:
    num1 = float(input('First number is: '))
    num2 = float(input('Second number is: '))
    print (num1 / num2)
    print("Calculation done.")
except ZeroDivisionError:
    print("An error occurred, due to zero division.")
    
#Exception handling 2.0
try:
    variable = 10
    print(variable / 2)
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero.")
except (ValueError):
    print("Error occurred.")
except (TypeError):
    print('It\'s a type error.')
except (ValueError,TypeError):
    print('Out of them.')
    
#ZeroDivisionError
try:
    print("Let\'s run this code : ")
    print(1 / 5)
except ZeroDivisionError:
    print("Divided by zero.")
finally:
    print("This code will run no matter what since try and except statements are being used.")
    
#raising an error
print(1)
raise ValueError('Error')
    
#Nameerror
name1 = "Keyaru"
name2 = '123'
print(name1)
print(name2)
print(name1, 'is corrrect name.')
raise NameError(name2 + " is an invalid name!")
    
#Exception raising with arguments
a = int(input('Enter a number: '))
if a<0:
    raise ValueError(str(a) + ' is a negative number.')
elif a>0:
    print(a, 'is a positive number.')
else:
    print('a is zero.')
    
#assert with argument
temp = float(input('Enter temperature in kelvin: '))
if temp >= 0:
    print('More than absolute zero.')
else:
    assert (temp > 0), "Colder than absolute zero!"
    
#assert with try/except
try:
    print('How you doin\'?')
    print('I will achieve it.')
    assert(3+8-2==4), 'Error, statement not true.'
    assert(5+4==11-2), 'Accepted, statement holds.'
except:
    print('There\'s an error.')
try:
    assert(3+2==5-1), 'LHS!=RHS'
except:
    print('LHS!=RHS')
    

    
    
    
    
    
    
    
    
    \