#Magic methods:
#__truediv__ v1.0
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * max(len(other.cont),len(self.cont))
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print((hello / spam) + '\n'  + (spam / hello))

#__truediv__ v2.0
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self,other):
        return (self.cont/other.cont)**2

spam = SpecialString(25)
hello = SpecialString(5)
print(spam / hello)

""" To call magic methods we use symbols
 instead of calling a function.
"""

#Overloading v1.0
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

python = SpecialString('python')
hello = SpecialString("Hello World!")
python > hello


#Overloading v2.0
import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

#Data Hiding:
#Weakly protected methods:
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue_items({})".format(self._hiddenlist)

queue = Queue((1, 2, 3))
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
"""
__repr__ for string representation
push to add item at the place first index
pop to remove item from last by providing index number inside pop method
FILO --> First IN Last OUT for Queue
FIFI --> First IN First OUT for Stack
"""

#Strongly protected methods:
class Spam:
    __egg = 7
    def print_egg(self):
       print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.egg)

#Same above example, If not strongly protected:
class Spam:
    egg = 7
    def print_egg(self):
        pass
s = Spam()
s.print_egg()
print(s.egg)
print(Spam.egg)

#class method:
class cuboid:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def calculate_volume(self):
        return self.width * self.height * self.length

    @classmethod
    def for_cube(cls, side_length):
        return cls(side_length, side_length, side_length)

x = int(input('Enter the side of your cube, in cm: '))
my_cube = cuboid.for_cube(x)
print('Volume of your cube is: '+str(my_cube.calculate_volume())+'cm^3')
a = int(input('Enter the width of your cuboid, in cm: '))
b = int(input('Enter the height of your cuboid, in cm: '))
c = int(input('Enter the length of your cuboid, in cm: '))
my_cuboid = cuboid(a,b,c)
print('Volume of your cube is: '+str(my_cuboid.calculate_volume())+'cm^3')
"""new_square is a class method and is called on the class,
rather than on an instance of the class.
It returns a new object of the class cls.
Technically, the parameters self and cls are just conventions;
they could be changed to anything else. However, they are universally
followed, so it is wise to stick to using them.
"""

#static method:
#class Pizza v1.0   
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        pass

    @staticmethod
    def validate_topping(topping):
        if topping != "pineapple":
            return topping+' is available.'
        else:
            raise ValueError("No pineapples!")

ingredients = ["cheese", "onions", "tomato", 'pineapple', 'capsicum']
for item in ingredients:
    print(Pizza.validate_topping(item))
    
"""
-->Static methods don't requires additional argument like "cls" in class method.
-->Static methods behave like plain functions, except for the 
fact that you can call them from an instance of the class.
"""

#class Pizza v2.0   
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        pass
    
    @staticmethod
    def validate_topping(topping):
        if topping != "pineapple":
            print(topping+' is available.')
        else:
            raise ValueError("No pineapples!")
my_topping = input('Enter the topping you want to get served: ')
Pizza.validate_topping(my_topping.lower())
"""
Here, we called it by class.
Argument in dunder is just to pass, we have to pass argument 
in static method function to get the result.
"""

#properties:
"""
Similar to static method the dunder method is just to pass we
make a method which we call by @property. No need to treat it as function.
"""
#class Pizza v1.0:
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        if self.toppings != 'pineapple':
            return self.toppings + ' is available.'
        else:
            raise ValueError('No pineapples!')

my_topping = ["cheese", "tomato", "capsicum", "onion"]
for item in my_topping:
    pizza_topping = Pizza(item)
    print(pizza_topping.pineapple_allowed)
no_pineapples = Pizza('Pineapple'.lower())
print(no_pineapples.pineapple_allowed)
#pizza.pineapple_allowed will run because property are not callable.
#pizza.pineapple_allowed() is not used i.e., property and not a function.
#pizza.pineapple_allowed = True -->can't assign attribute new value.


#property.setter
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = 'onion'
print(pizza.pineapple_allowed)
"""
Here, setter is used so that we can assign our private value 
new value and then we can call our property.
we don't have to call function since it's a property.
"""

#property.setter example:
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

person1 = Person("Keyargu")
print(person1.name)
person1.name = 'Keyaru'
print(person1.name)

#Shooting game - Example
class Enemy:
    name = ""
    lives = 0
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives == 0:
            print(self.name + ' killed')
        elif self.lives > 0:
            print(self.name + ' has '+ str(self.lives) + ' lives')
        else:
            print(self.name + ' is already dead, don\'t waste your energy.')

class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster', 3)

class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien', 5)

m = Monster()
a = Alien()

while True:
    x = input('Enter weapon choice among (laser,gun or exit): ')
    if x == 'laser':
        a.hit()
    elif x == 'gun':
        m.hit()
    elif x == 'exit':
        break
    





