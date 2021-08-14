#Object Oriented Programming
class Dog:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

Lucy = Dog("yellowish", 2)
Mike = Dog("white",4)
Rowny = Dog("Black",4)
print(Lucy.color,Lucy.legs)
print(Mike.color)
print(Mike.legs)
print(Rowny.legs)
print(Rowny.color,Rowny.legs)
legs = 'Generally, Dogs have four legs.'
print(legs,Mike.legs)

#Class method 1.0
class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print("Woof! Woof!")

Mike = Dog("Mike", "white", 4)
print(Mike.name,'is my pet dog whose age is', Mike.age,
'and he is of',Mike.color,'color and his bark sounds:')
Mike.bark()

#Class method 2.0
class Dog:
    legs = 4
    bark_for_all = 'Woof!'
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)
print(Dog.bark_for_all)

#Class attributes
class Dog:
    legs = 4
    def __init__(self, name, Gender, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.Gender = Gender
    def bark(self):
        print('Woof! Woof!')

Mike = Dog("Mike",'M', "white", 5)
Cathy = Dog('Cathy','F','Black',4)
print(Mike.age)
print(Cathy.name, Cathy.Gender, Cathy.color, Cathy.age)
print(Dog.legs)
Cathy.bark()

#Inheritance
class Animal: 
    legs = 4
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

class Cat(Animal):
    def purr(self):
        print("Meowwww...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cow(Animal):
    def sound(self):
        print('maaaaaaaaaaa!')

Mike = Dog("Mike", "white", 5)
Cathy = Cat('Cathy','Black & white', 2)
Heera = Cow('Heera','white',5)
Moti = Cow('Moti','brownish',5.2)
print(Mike.color)
Mike.bark()
print(Heera.name, '&', Moti.name, 'are best childhood friends.')
print(Heera.color + ' ' +Moti.color)
print(Moti.age)
Heera.sound()
Moti.sound()
print(Cathy.name)
print(Cathy.color)
print(Cathy.legs)
Cathy.purr()

#Inheritance with similar attributes
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grrrrr....")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
siberian_wolf = Wolf('Danny','Black')
print(husky.name +" is "+ husky.color)
husky.bark()
print(siberian_wolf.name +" is "+ siberian_wolf.color)
siberian_wolf.bark()

#Multi-inheritance
class Wolf:
    legs = 4
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
    def food(self):
        print('Meat of small animals.')
    def bark(self):
        print('Grrrr....')
class Dog(Wolf):
    def food(self):
        print("pedigree")
    def bark(self):
        print('Woof!')
    
class Breed(Dog):
    def Labra(self):
        print('Labrador')
    def gol_ret(self):
        print('Golden Retriever')
    def ger_she(self):
        print('German Shepherd')
    def chi(self):
        print('Chihuahua')

class Wolf_Breed(Wolf):
    def sib_wolf(self):
        print('Breed is siberian wolf.')
    def ame_wolf(self):
        print('Breed is American Wolf.')
    
Mike = Breed('Mike','white',5)
Siberian_wolf = Wolf_Breed('Danny','Black',6)
print(Mike.name, Mike.color, Mike.age, Mike.legs)
Mike.bark()
Mike.food()
Mike.chi()
print()
print(Siberian_wolf.name,Siberian_wolf.color,Siberian_wolf.age,Siberian_wolf.legs)
Siberian_wolf.bark()
Siberian_wolf.food()
Siberian_wolf.sib_wolf()
print('All classes have same legs:',Mike.legs,',',Siberian_wolf.legs,',',Dog.legs,',',Breed.legs,',',Wolf_Breed.legs,'&',Wolf.legs)

#Super function 1.0
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grrrrr....")

class Dog(Wolf):
    def bark(self):
        print("Woof!")
        super().bark()

husky = Dog("Max", "grey")
siberian_wolf = Wolf('Danny','Black')
print(husky.name +" is "+ husky.color)
husky.bark()
print()
print(siberian_wolf.name +" is "+ siberian_wolf.color)
siberian_wolf.bark()

#Super function 2.0
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()
        print(2.5)

class C:
    def spam(self):
        print(3)
        super().spam()
a = A()
a.spam()
b = B()
b.spam()
c = C()
c.spam()

#Magic method - __add__
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
class Vector2D(Vector3D):
    def z_value(self):
        return 'z = 0, always for a 2D vector.'
first = Vector3D(5, 7, 8)
second = Vector3D(3, 9, 2)
third = Vector3D(5, 8, 3)
fourth = Vector3D(9, 8, 15)
result = first + second
cosmos = first + third + fourth
new = result + cosmos + second + second
print(new.z)

trajectory_in_2D = Vector2D(5,9,0)
print(trajectory_in_2D.z)
print(trajectory_in_2D.z_value())

#Magic method - __mul__ and __truediv__
class SpecialString:
    def __init__(self, word):
        self.word = word

    def __truediv__(self, other):
        line = "=" * max(len(self.word),len(other.word))
        return '\n'.join([self.word, line, other.word])
    def __mul__(self,new):
        design = '/'*max(len(self.word),len(new.word))
        line = '='*max(len(new.word),len(self.word))
        design2 = '\\'*max(len(new.word),len(self.word))
        return '\n'.join([design, self.word, line, new.word, design2])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(hello * spam)
print('')
print(hello/spam)
  
#Magical method - __gt__ for comparison
new = ['start','stop']
class SpecialString:
    def __init__(self, word):
        self.word = word

    def __gt__(self, other):
        for i in new:
            for index in range(len(other.word)+1):
                result = other.word[:index] + ">" + self.word + '>' + i
                result += ">" + other.word[index:]
                print(result)
            print()
        for index in range(len(other.word)+1):
            for i in new:
                result = other.word[:index] + ">" + self.word + '>' + i
                result += ">" + other.word[index:]
                print(result)
        print()
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
print()
spam < eggs

#Magic method - class acts like container
import random

class String:
    def __init__(self, word):
        self.word = word

    def __getitem__(self, index):
        return self.word[index + random.randint(-1, 1)]
    def __len__(self):
        return random.randint(0, 2**len(self.word))


vague_list = String(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

#Data Hiding - weakly private method
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, index, value):
        self._hiddenlist.insert(index, value)

    def pop(self, index):
        return self._hiddenlist.pop(index)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3, 4])
print(queue)
queue.push(0, 0)
print(queue)
queue.pop(-1)
print(queue)
print(queue._hiddenlist)
queue.push(len(queue._hiddenlist),4)
print(queue)

#Data Hiding - Strongly private method
class Spam:
    __egg = 'Python Play.'
    def print_egg(self):
        print(self.__egg)

    __num = 586/3
    def print_num(self):
        print(self.__num)

s = Spam()
s.print_egg()
print(s._Spam__egg)

n = Spam()
n.print_num()
print(n._Spam__num)
print(s.__egg)
print(n.__num)




















