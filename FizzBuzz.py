#FizzBuzz program
i = int(input('Enter a number: '))
for i in range(i):
    if i%2 == 0:
        continue
    elif (i%3 == 0 and i%5 == 0):
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

#FizzBuzz excluding even numbers
i = int(input('Enter you number: '))
for i in range(1,i):
    Fizz = (i%3==0)
    Buzz = (i%5==0)
    NOTA = (i%2==0)
    if NOTA:
        continue
    elif (Fizz and Buzz):
        print('FizzBuzz')
    elif Fizz:
        print('Fizz')
    elif Buzz:
        print('Buzz')
    else:
        print(i)


















