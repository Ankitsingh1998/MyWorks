#Property 1.0
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
print(pizza.pineapple_allowed == False)
print(pizza.toppings)
pizza.pineapple_allowed = True

#Property 2.0
a = int(input('Enter a number: '))
class Person:
    def __init__(self,age):
        self.age = int(age)


    @property
    def isAdult(self):
        if self.age >= 18 :
            return True

        else:
            return False

Age = Person(a)
print(Age.isAdult)


#Class method
a = int(input('Enter number, a: '))
b = int(input('Enter number, b: '))
c = int(input('Enter number, c: '))
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(a)
print(square.calculate_area(),'cm^2')

rectangle = Rectangle(b,c)
print(rectangle.calculate_area(),'cm^2')

#Static method
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

ingredient = ['cheese','macroni','pineapple']
if all(Pizza.validate_topping(i) for i in ingredient):
    pizza = Pizza(ingredient)

#setter and getter
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

















