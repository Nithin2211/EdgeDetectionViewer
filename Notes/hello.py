# VARIABLE - A container for a value (string, integer, float, boolean).
#            A Variable behaves as if it was the value it contains

# F-STRING - format string                                     # (can be used in return statement also)

# Syntax
# print(f"hello{name}")
# return f"hello{name}"

# SEP KEYWORD ARGUMENT - Separator keyword

# Synatx
# print("1", "2", "3", "4", sep="-")                           # output - 1-2-3-4

# STRINGS - Enclosed with double quotes or single quotes or triple quotes
# INTEGERS - numbers
# FLOAT - decimal numbers
# BOOLEAN - true or false

# TYPECASTING - The process of converting avariable from 
#               one data type to another type( str(), int(), float(), bool())

# Syntax
# print(type(name))

# INPUT FUNCTION - A function that prompts the user to enter data 
#                  Returns the entered data as a string

# Syntax
# name = input("what is your name: ")
# age = int(input("what is your age: "))

# ARITHMETIC OPERATOR - add, sub, mul, div, exponent, modulus

# Syntax

# add - age += 1 (augumented assignment operator) or age = age + 1 
# sub - age -= 1 (augumented assignment operator) or age = age - 1
# mul - same as add and sub
# div - same as add and sub
# expo - same as add and sub (**)
# modulus(remainder) - same as add and sub (%)
# equal - (==)

# MATH RELATED FUNCTIONS
        # round function - (result = round(3.14))              # output - 3 
        # abosoulute function - (result = abs(-4))             # output - 4
        # power function - (result = pow(4, 3))                # output - (4*4*4 = 64)
        # max function - (result = max(5, 4, 3))               # output - 5
        # min function - (result = min(5, 4, 3))               # output - 3

# IF CONDITION - Do some code only if some condition is True 
#                Else do something else

# Syntax

# if age >= 18:
#   print("hello")

# elif age < 0:
#   print("hello")

# else:
#   print("bye")

# LOGICAL OPERATORS - evaluate multiple conditions (or, and, not) 
#                or - at least one condition must be true 
#               and - both conditions must be true 
#               not - inverts the condition (not false, not true)

# syntax
# if temp >= 28 or not sunny:                                                          # (same for not and And operator)

# STRING METHODS
# print(help(str))
    # name = "premp"
    # len function - (result = len(name))                      # output - 5            # (if not found -1)
    # find function - (result = name.find("p"))                # output - 0
    # reverse find function - (result = name.rfind("p"))       # output - 4 
    # capiatalize function - (result = name.capitalize())      # output - Premp        # (only first letter)
    # upper function - (result = name.upper())                 # output - PREMP
    # lower function - (result = name.lower())                 # output - premp
    # isdigit function - (result = name.isdigit())             # output - False
    # isalpha function - (result = name.isalpha())             # output - true
    # count function - (result = name.count("p"))              # output - 2
    # replace function - (result = name.replace("e", "a"))     # output - pramp

# INDEXING - accessing elements of a sequence using [] (indexing operator) 
#            [start : end : step]                              # (only string, tuple or list)   

# Synatx
#   num="1234-5678-9012-3456"
#   print(num[0])                                              # output - 1
#   print(num[:4])                                             # output - 1234
#   print(num[5:9])                                            # output - 5678
#   print(num[5:])                                             # output - 5678-9012-3456
#   print(num[-1])                                             # output - 6
#   print(num[-4:])                                            # output - 3456
#   print(num[::3])                                            # output - 146-136
#   print(num[0:8:2])                                          # output - 13-6
#   print(num[::-1])                                           # output - 6543-2109-8765-4321

# FORMAT SPECIFIERS - {value:flags} format a value based on what 
#                     flags are inserted

# Synatx
# price1 = 3.14159
# price2 = -987.65
# price3 = 3000.14159

#   .(number)f - round to that many decimal places (fixed point) 
#   eg: (print(f"price1 is {price1:.2f}"))                     # output - 3.14

#   :(number)  - allocate that many spaces 
#   eg: (print(f"price1 is {price1:10}"))                      # output - (   3.14159)

#   :03        - allocate and zero pad that many spaces
#   eg: (print(f"price1 is {price1:010}"))                     # output - (0003.14159)

#   :<         - left justify
#   eg: (print(f"price1 is {price1:<10}"))                     # output - (3.14159   )

#   :>         - right justify
#   eg: (print(f"price1 is {price1:>10}"))                     # output - (   3.14159)

#   :^         - center align
#   eg: (print(f"price1 is {price1:^10}"))                     # output - ( 3.14159  )

#   :+         - use a plus sign to indicate positive value
#   eg: (print(f"price1 is {price1:+}"))                       # output - (+3.14159)
#   eg: (print(f"price1 is {price2:+}"))                       # output - (-987.65)

#   :          - insert a space before positive numbers
#   eg: (print(f"price1 is {price1: }"))                       # output - ( 3.14159)
#   eg: (print(f"price1 is {price2: }"))                       # output - (-945.65)

#   :,         - comma separator
#   eg: (print(f"price1 is {price3:,}"))                       # output - (3,000.14159)


# final eg: (print(f"price1 is {price3:+,.2f}"))               # output - (+3,000.14)

# WHILE LOOP - execute some code WHILE some condition remains true

# Syntax
#   while name == "":
#       print("hello")

# Continue function - it skips the loop for once
# Break function    - it breaks the loop and next loop will not run

# FOR LOOPS - execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc.

# Syntax
# Range function - it returns the number from 1 to 10
#   for x in range(1,11):
#       print(x)                                               # output - 10 times block runs

# Reversed function - it returns the number from 10 to 1 in vertical
#   for x in reversed(range(1,11)):

# Indexing
#   for x in range(1,11,3):                                    # output - 1,4,7,10 in vertical

# Continue function - it skips the loop for once
# Break function    - it breaks the loop and next loop will not run

# End function - actually all the print statements contains 
#                new line character. so basically we use this 
#                end function to eliminate this character

# Syntax
#   for x in range(1,10):
#       print(x, end="")                                       # output - 123456789

#   for x in range(1,10):
#       print(x, end=" ")                                      # output - 1 2 3 4 5 6 7 8 9

# NESTED LOOP - A loop within another loop (outer, innnner) 
#               outer loop:
#                    inner loop:

# Syntax
#   for x in range(2):
#       for y in range(1,5):
#           print(y, end="")                                   # output - 1234512345
#       print()                                                # output - 12345
#                                                                         12345

# 1D Collection = single "variable" used to store multiple values
#          LIST = [] ordered and changeable. Duplicates OK
#          SET  = {} uncorderd and immutable, but add/remove OK. NO Duplicates
#         TUPLE = () ordered and unchangeable. Duplicates OK. FASTER
#  DICTIONARIES = A collection of {key:value} pairs ordered and changeable. No Duplicates

# LISTS
# Syntax
#   fruits = ["a","b","c","d"]
#   print(fruits[1])                                           # output - b
#   print(fruits[0:3])                                         # output - ["a","b","c"]

#   for x in fruits:
#       print(fruits)

#   print(dir(fruits))                                         # output - it prints all the functions of list(only functions name)
#   print(help(fruits))                                        # output - it prints all the function of list with definitions
#   print(len(fruits))                                         # output - 4
#   print("a" in fruits)                                       # output - True
#   fruits.append("pineapple")
#   fruits.remove("a")
#   fruits.insert(0,"pineapple")
#   fruits.sort()
#   fruits.reverse()
#   fruits.clear()
#   fruits.index("a")
#   fruits.count("a")

# SET
# Syntax
#   fruits = {"a","b","c","d"}
#   print(fruits)   #output - {"b","a","d","c"} (since unordered)

#   print(dir(fruits))                                         # output - it prints all the functions of set(only functions name)
#   print(help(fruits))                                        # output - it prints all the function of set with definitions
#   print(len(fruits))                                         # output - 4
#   print("a" in fruits)                                       # output - True
#   print(fruits[1])                                           # output - error occurs since unordered
#   fruits.remove("a")
#   fruits.add("a")
#   fruits.pop()
#   fruits.clear()

# TUPLE
# Syntax
#   fruits = ("a","b","c","d")
#   print(dir(fruits))                                         # output - it prints all the functions of tuple(only functions name)
#   print(help(fruits))                                        # output - it prints all the function of tuple with definitions
#   print(len(fruits))                                         # output - 4
#   print("a" in fruits)                                       # output - True
#   fruits.index("a")
#   fruits.count("a")

#   for x in fruits:
#       print(fruits)

# DICTIONARIES
# Syntax
#   capitals = {"INDIA": "Delhi", "RUSSIA": "Moscow", "CHINA": "Beijing"}
#   print(dir(capitals))                                       # output - it prints all the functions of dictionary(only functions name)
#   print(help(captials))                                      # output - it prints all the function of dictionary with definitions
#   print(capitals.get("INDIA"))                               # output - Delhi (if no value it returns "none")
#   capitals.pop("CHINA")
#   capitals.popitem()
#   capitals.clear()
#   capitals.update({"USA": "washington"})                     # (in this we can update the value and we can add new key and value)
#   capitals.keys()
#   capitals.values()
#   capitals.items()                                           # (it prints all key and values in 2D list of tuples ("[(), (), ()]") )

# 2D LISTS - [list1, list2, list3]
# Syntax
#   fruits = ["a","b","c","d"]
#   fruits1 = ["ab","cd","ef","gh"]
#   groceries = [fruits, fruits1]
#   print(groceries)                                           # output - [['a','b','c','d'], ['ab','cd','ef','gh']]
#   print(groceries[0])                                        # output - ['a','b','c','d']
#   print(groceries[0][0])                                     # output - a

# 2D TUPLES - [tuple1, tuple2, tuple3)
# Syntax
#   fruits = ("a","b","c","d")
#   fruits1 = ("ab","cd","ef","gh")
#   groceries = (fruits, fruits1)
#   print(groceries)                                           # output - (('a','b','c','d'), ('ab','cd','ef','gh'))
#   print(groceries[0])                                        # output - ('a','b','c','d')
#   print(groceries[0][0])                                     # output - a

# 2D SET - ({set1, set2, set3})
# Syntax
#   fruits = {"a","b","c","d"}
#   fruits1 = {"ab","cd","ef","gh"}
#   groceries = (fruits, fruits1)
#   print(groceries)                                           # output - ({'a','b','c','d'}, {'ab','cd','ef','gh'})
#   print(groceries[0])                                        # output - {'a','b','c','d'}



# 1. DEF FUNCTION WITH POSITIONAL ARGUMENTS - A block of reusable code. 
#                                             Place() after the function name to invoke it
#                                             ( 1. Positional, 2. Default, 3. Keyword, 4. Arbitrary)

# Syntax
#   def birthday():
#       print("Happy Birthday")
#   birthday()

#   def birthday(name, age):
#       print(f"Happy Birthday {name} and {age} years old")
#   birthday("bro", 20)   

# RETURN - Statement used to end a function and send a 
#          result back to the caller(it is used inside the def block).
#          It is also return the value to the function not variable.

# Syntax
#   def add(x, y):
#       z = x + y
#       return z
#   print(add(1, 3))

# 2. DEF FUNCTION WITH DEFAULT ARGUMENTS - A default value for certain parameter 
#                                          default is used when that argument is omitted
#                                          make your functions more fleible, reduces # of arguments

# Synatx
#   def add(x, y=2):                                           # (if a new argument is needed then default argument is not onsidered 
#       z = x + y                                                and you can change argument while calling the function)
#       return z                                               # (always in def function the default argument should be last in the bracket)
#   print(add(1))

# 3. DEF FUNCTION WITH Keyword ARGUMENTS - An argument preceded by an identifier 
#                                          helps with readability order of arguments doesn't matter 

# Syntax
#   def div(x, y):                                             # (If the arguments in the calling fuction is changed 
#       z = x / y                                                then we can use keyword to identify with the def function parameter)
#       return z                                               # (Always positional arguments should be first in the bracket)
#   print(div(y=1, 3))

# 4. DEF FUNCTION WITH Arbitary ARGUMENTS - Can use 2 types of parameters they are *args & **kwargs
#                                   *args - allows you to pass multiple non-key arguments (tuple)
#                                **kwargs - allows you to pass multiple keyword-arguments (dictionary)
#                                           (* unpacking operator)

# Synatx
#   *args argument
#       def add(*args):                                        # (in this *args takes the parameter as tuple)
#           print(type(args))                                  # output - tuple
#       add(1, 2, 3)

#       def add(*args):
#           total = 0
#           for arg in args:
#               total += arg
#           return total
#       print(add(1, 2, 3, 4, 5))                              # output - 15

#   **kwargs argument
#       def address(**kwargs):
#           print(type(kwargs))                                # output - dictionary
#       address(street="22", city="chennai")

#       def address(**kwargs):
#           for key, value in kwargs.items():
#               print(f"{key}:{value}")                        # output - street:22 and city:chennai (in vertical)
#       address(street="22", city="chennai")

#   Both arguments
#       def label(*args, **kwargs):                            # (the args & kwargs should be in same place of calling and def function)
#           pass
#       label("Dr.", "name", street="22", city="chennai")

# MEMBERSHIP OPERATOR - used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, dictionary)
#                       1. in
#                       2. not in

# Syntax
# IN OPERATOR
#   word = "apple"
#   letter = input("guess: ")
#   if letter in word:
#       print(letter)
#   else:
#       print("there is no {letter}")

# NOT IN OPERATOR
#   word = "apple"
#   letter = input("guess: ")
#   if letter not in word:
#       print("there is no {letter}")
#   else:
#       print(letter)

# MATCH-CASE STATEMENt(SWITCH) - An alternative to using many 'elif' statements 
#                                Execute some code if a value matches a 'case' 
#                                Benefits: cleaner and syntax is more readable

# Syntax
#   def week(day):
#       match day:
#           case 1:
#               return "it is sunday"
#           case 2:
#               return "it is monday"
#           case _:
#               return "it is not valid"
#   print(week(1))                                             # output - it is sunday

#   def weekend(day):
#       match day:
#           case "saturday" | "sunday":
#               return True
#           case "monday" | "Tuesday" | "Wednesday":
#               return False:
#           case _:
#               return False
#   print(weekend("wednesday"))                                # output - False

# VARIABLE SCOPE   - Where a Variable is visible and accessible
# SCOPE RESOLUTION - (LEGB) local -> Enclosed -> Global -> Built-in

# VARIABLE SCOPE
# Syntax
#   LOCAL VARIABLE:
#       def func1():
#           a = 1                                              # (Here "a" is a local variable to the the parrticular function. 
#           print(a)                                           # so, "a" cannot be printedoutside the function )
#       func1()

#       def func2():
#           b = 2
#           print(b)                                           # output - 2
#           print(a)                                           # (error - since the variable is not declared in the function 2.
#       func2()                                                #  The variable "a" is local variable)

#   ENCLOSED VARIABLE: 
#       def func1():
#           x = 1                                              # (Before printing the 'x' it checks for the value of the variable 'x'.
#           def func2(x):                                      # If the variable 'x' is in the same function (local variable) it prints 
#               x = 2                                          # the value or else it checks for the enclosed variable which is in line no 429 and prints the value of 'x') 
#               print(x)                                       # output - (if the line no 431 is present the output is '2'. If not it is the output is '1')
#           func2()
#       func1()

#   GLOBAL VARIABLE:
#       def func1():
#           x = 1                                               
#           print(x)                                           # output - (If the line no 438 is there the output is '1' or else the output will be '3')
#       func1()

#       def func2():
#           x = 2                                          
#           print(x)                                           # output - (If the line no 438 is there the output is '2' or else the output will be '3')
#       func2() 
#       x = 3 (It is a global variable)                        # (This value will be if there is no loacal and enclosed variable is present in the function)

#   BUILT-in VARIABLE:
#       from math import e (built in varaiable)
#       def func():
#           print(e)                                           # Output - (If the line no 452 is there the output is '3' or else the output will be '2.718...')
#       e = 3(global variable)
#       func()

# if __name__==__main__: (this script can be imported OR run standalone)
#                        Functions and classes in this module can be reused
#                        without the main block of code ececuting

# syntax
#   def main():
#       #your program goes here
# if __name__== '__main__':                                    # (refer bro code)
#       main()

# OBJECT - A "bundle" of related attributes (vriables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# CLASS - (blueprint) used to design the structure and layout of an object

# Syntax
#   class Car:                                                 # In this the car is class name
#       def __init__(self, model, year):                       # It is a constructor where it starts with 'init'. self is like a tool to call the value of the particular object. model and year are attributes
#           self.model = model                                 # In this the self helps to call the value of model of an particular object and it assigns the value of model to the self.model
#           self.year = year
#   car1 = car("Mustang", 2024)                                # In this car1 is a object name where it is acts like a calling function with attribute. The syntax of this should be same like first class name and the attributes.   
#   car2 = car("kia", 2025)

#   print(car1.model)                                          # Output = Mustang ( In this the car1 object calls the self in init to find the model )
#   print(car2.year)                                           # Output = 2025

# Example - https://chatgpt.com/share/689dec81-6838-800d-8a67-c7a0f9a5b19d

# CLASS VARIABLE - Shared among all instances of a class
#                  Defined outside the constructor
#                  Aloow you to share data among all objects created from that class

# Syntax for 'what is class and instance variable'
#   class Car:
#       Wheels = 4                                             (Class Variable)
#   def __init__(self, model, year):
#       self.model = model                                     (Instance Variable)
#       self.year  = year                                      (Instance Variable)

# Synatx
#   class Student:
#       class_yesr = 20
#       def __init__(self, name,age):
#           self.name = name
#           self.age = age

# student1 = student("Spongebob", 30)
# student1 = student("muthu", 20)

# print(student1.name)                                         # output - Spongebob
# print(student2.age)                                          # output - 20
# print(student1.class_year)                                   # output - 2024
# print(student2.class_year)                                   # output - 2024 (accessing the class variable via object name)
# print(Student.class_year)                                    # output - 2024 (access the class variable via class name it is easy and readable way)

# INHERITANCE = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               Class Child(parent) OR sub(super)

# Syntax
#   Class Animal:                                              # (Animal class is a parent class )
#       def __init__(self, name):
#           self.name = name
#           self.is_alive = True

#       def eat(self):
#           print(f"{self.name} is eating")

#       def sleep(self):
#           print(f"{self.name} is sleeping"))

#   class Dog(Animal):                                         # (Child class)
#       def speak(self):
#           print("Woof")

#   dog = Dog("Scooby")
#   print(dog.name)                                            # output - scooby
#   print(dog.is_alive)                                        # output - True
#   dog.eat()                                                  # output - scooby is eating
#   dog.sleep()                                                # output - scooby is sleeping
#   dog.speak()                                                # output - woof

# MULTIPLE INHERITANCE - Inherit from more than one parent class
#                        C(A, B) 

# MULTILEVEL INHERITANCE - Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# Syntax
# Multiple Inheritance

#   class Prey:
#       def flee(self):
#           print("This animal is fleeing")

#   class predator:
#       def hunt(self):
#           print("This animal is hunting")

#   class Rabbit(Prey, predator):
#       pass

#   rabbit = Rabbit()
#   rabbit.hunt()                                              # output - This animal is hunting
#   rabbit.flee()                                              # output - This animal is fleeing

# Multilevel Inheritance

#   class Animal:
#       def __init__(self, name):
#           self.name = name
#       def eat(self):
#           print(f"{self.name} is eating")
#       def sleep(self):
#           print(f"{self.name} is sleeping")
#   class Prey(Animal):
#       def flee(self):
#           print(f"{self.name} is fleeing")

#   class predator(Animal):
#       def hunt(self):
#           print(f"{self.name} is hunting")

#   class Rabbit(Prey, predator):
#       pass

#   rabbit = Rabbit("Bugs")
#   rabbit = eat()                                             # output - Bugs is eating
#   rabbit = sleep()                                           # output - Bugs is sleeping
#   rabbit.hunt()                                              # output - Bugs is hunting
#   rabbit.flee()                                              # output - Bugs is fleeing

# SUPER() - Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

# Syntax
#   class Shape:
#       def __init__(self, color, is_filled):
#           self.color = color
#           self.is_filled = is_filled
#       def describe(self):
#           print(f"it is {self.color} and {self.is_filled})

#   class Circle(Shape):
#       def __init(self, color, is_filled, radius):
#           self.color = color
#           self.is_filled = is_filled
#           self.radius = radius
#       def decribe(self):
#           print("hello")
#           super().describe()

#   class Square(Shape):
#       def __init(self, color, is_filled, width):
#           self.color = color
#           self.is_filled = is_filled
#           self.width = width

#   class Triangle(Shape):
#       def __init(self, color, is_filled, width, height):
#           super().__init__(color, is_filled)
#           self.width = width
#           self.height = height

#   circle = circle("red", is_filled = True, radius = 5)
#   square = Square("blue", is_filled = false, width = 6)
#   triangle = Triangle("white", is_filled = True, width = 8, height = 10)
#   print(circle.color)                                        #output - red
#   print(square.is_filled)                                    #output - false
#   print(triangle.width)                                      #output - 8
#   traingle.describe()                                        #output - it is white and true 
#   circle.describe()                                          #output - hello as well it is red and true

# POLYMORPHISM - Greek word that means to "have many forms or faces"
#                Poly - many
#                Morphe - form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance   - An object could be treated of the same type as a parent class
#                2. "Duck typing" - Object must have necessary attributes/methods

# Syntax
#   from abc import ABC, abstractmethod                        #(https://www.google.com/search?q=what+is+abc+abstractmethod&rlz=1C2UEAD_enIN1023IN1045&sca_esv=1c2c48b035966a68&sxsrf=AE3TifPWJe5JZFYTsdGI5qn7gr0lobwJQg%3A1755695595247&source=hp&ei=68mlaMnwDJvR1e8PhfmU2QE&iflsig=AOw8s4IAAAAAaKXX-6A8WwBlnImhQJImI0m5O735FVyE&oq=what+is+abc+in+abstr&gs_lp=Egdnd3Mtd2l6IhR3aGF0IGlzIGFiYyBpbiBhYnN0cioCCAAyBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogQyCBAAGIAEGKIEMgUQABjvBTIFEAAY7wVIrEtQxARYuz1wAXgAkAEAmAGCAqAB6xqqAQYwLjE3LjO4AQPIAQD4AQGYAhWgArUbqAILwgIGELMBGIUEwgIKEAAYAxjqAhiPAcICChAuGAMY6gIYjwHCAgsQABiABBiRAhiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgILEAAYgAQYsQMYgwHCAgsQLhiABBixAxiDAcICCBAAGIAEGLEDwgIFEC4YgATCAgoQABiABBhDGIoFwgIWEC4YgAQYsQMY0QMYQxiDARjHARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIOEAAYgAQYkQIYsQMYigWYAwniAwUSATEgQPEFJTkdfpZPouWSBwYxLjE3LjOgB-J4sgcGMC4xNy4zuAesG8IHCTAuMTAuMTAuMcgHPw&sclient=gws-wiz)
#   class Shape:
#       @abstractmethod
#       def area(self):
#           pass
#   class Circle(Shape):
#       def __init__(self, radius):
#           self.radius = radius
#       def area(self):
#           return 3.14 * self.radius ** 2
#   class Square(Shape):
#       def __init__(self, side):
#           self.side = side
#       def area(self):
#           return self.side ** 2

#   shapes= [Circle(4), Square(5)]                             # Here is polymorphism works
#   for shape in shapes:
#       print(f"{shape.area()}")                               #output - 50.24 and 25

# DUCK TYPING = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck."

# Syntax
#   class Animal:
#       alive = true
#   class Dog(Animal):
#       def speak(self):
#           print("Woof")
#   class Cat(Animal):
#       def speak(self):
#           print("Meow")
#   class Car(Animal):
#       alive = false
#       def speak(self):
#           print("Honk!")

#   animals = [Dog(), Cat()]
#   for animal in animals:
#       animal.speak()
#       print(animal.alive)

# STATIC METHODS = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions
# Instance methods = Best for operations on instances of the class (objects)
# Static methods   = Best for utility functions that do not need access to class data

# Syntax
#   class Employee:
#       def __init__(self, name, position):
#           self.name = name
#           self.position = position
#       def get_info(self):                                    # The def get_info is a instance method
#           return f"{self.name} = {self.position}"

#       @staticmethod (It is called a decorator)               # In static method the def does not belongs to any object instead it belongs to class
#       def is_valid_position(position):                       # The def is_valid_position is static method
#           valid_positions = ["manager", "cashier", "cook", "janitor"]
#           return position in valid_positions

#   employee1 = Employee("ram", "Manager")
#   employee2 = Employee("ramesh", "Cook")

#   print(Employee.is_valid_position("cook"))                  # output - True (Static method)
#   print(Employee.is_valid_position("Rocket scientist"))      # output - False (Static method)
#   print(employee1.get_info())                                # output - ram = Manager (Instance method)
# IN FINAL STATIC METHOD WILL USE TO ACCESS THE DATA ONLY THROUGH CLASS BUT INSTANCE METHOD WILL USE THE OBJECT TO ACCESS THE DATA

# CLASS METHODS = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Syntax
#   class Student:
#       count = 0
#       total_gpa = 0
#       def __init__(self, name, gpa):
#           self.name = name
#           self.gpa  = gpa
#           Student.count += 1
#           Student.total_gpa += gpa

#       #INSTANCE METHOD
#       def get_info(self):
#           return f"{self.name} {self.gpa}"

#       @classmethod
#       def get_count(cls):
#           return f"Total no of student: {cls.count}"

#       @class method
#       def get_average_gpa(cls):
#           if cls.count == 0:
#               return 0
#           else:
#               return f"{cls.total_gpa / cls.count:.2f}"

#   student1 = Student("Ram", 3.2)
#   studenr2 = Student("Ramesh, 2.0")

#   print(Student.get_count())                                 # output - 2
#   print(Student.get_average_gpa())                           # output - 3.060

# MAGIC METHODS - Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects.

# Syntax
#   class Book:
#       def __init__(self, title, author, num_pages):
#           self.title = title
#           self.author = author
#           self.num_pages = num_pages

#       def __str__(self):                                     # It is used to give a string representation of an object by the call off only oject name in like line no:758
#           return f"'{self.title}' by {self.author}"

#       def __eq__(self, other):                               # It is defined as def sunder "equal". It is used to check whether the two objects are equal.
#           return self.title == other.title and self.author == other.author

#       def __lt__(self, other):                               # It is defined as def dunder "less than". It is used to check whether the object is less than the other objects.
#           return self.num_pages < other.num_pages

#       def __gt__(self, other):                               # It is defined as def dunder "greater than". It is used to check whether the object is greater than the other objects.
#           return self.num_pages > other.num_pages

#       def __add__(self, other):                              # It is defined as def dunder "add". It is used to add the two objects.
#           return f"{self.num_pages + other.num_pages} pages"

#       def __contains__(self, keyword):                       # It is defined as def dunder "contains". It is used to check whether the given word is there in the particular object.
#           return keyword in self.title or keyword in self.author

#       def __getitem__(self, key):                            # It is defined as def dunder "getitem". It is used to get the particular item from the object.
#           if key == "title":
#               return self.title
#           elif key == "author":
#               return self.author
#           elif key == "num_pages":
#               return self.num_pages
#           else:
#               return f"key '{key}' was not found"

#   book1 = ("The habbit", "J.R.R", 310)
#   book2 = ("The hobby", "J.R.S", 110)
#   book3 = ("The hobby", "J.R.S", 120)

#   print(book1)                                               # output - 'The habbit' by J.R.R
#   print(book2)                                               # output - 'The hobby' by J.R.S
#   print(book2  == book3)                                     # output - true
#   print(book2 < book3)                                       # output - true
#   print(book2 > book3)                                       # output - false
#   print(book2 + book3)                                       # output - 230 pages
#   print("habbit" in book1)                                   # output - true
#   print(book2['title'])                                      # output - The hobby
#   print(book2['author'])                                     # output - J.R.S
#   print(book2['num_pages'])                                  # output - 110

# @PROPERTY - Decorator used to define a method as a propery (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

# Syntax
#   class Rectangle:
#       def __init__(self, width, height):
#           self._width = width                                # The underscore before width is used to 'private the width for inside the class'. If it is accessed internally it should be "rectangle._width" but if it is in "rectangle.width" then it will access the 'def width' only. 
#           self._height = height

#       @property (Getter method to get data)                  # The property decorator used to return the 'def width' if the 'rectangle.width' is called.
#       def width(self):
#           return f"{self._width:.1f}cm"

#       @property
#       def height(self):
#           return f"{self._height:.1f}cm"

#       @width.setter (Setter method to change or write the data) # The width can be changed by setter decorator
#       def width(self, new_width):
#           if new_width > 0:
#               self._width = new_width
#           else:
#               print("Width must be greater than zero")

#       @height.setter
#       def height(self, new_height):
#           if new_height > 0:
#               self._height = new_height
#           else:
#               print("Height must be greater than zero")

#       @width.deleter
#       def width(self):
#           del self._width
#           print("Width has been deleted")

#       @height.deleter
#       def Height(self):
#           del self._height
#           print("Height has been deleted")

#   rectangle = Rectangle(3, 4)

#   print(rectangle._width)                                    # output - 3
#   print(rectangle.height)                                    # output - 4.0cm

#   rectangle.width = 5
#   rectangle.height = -1

#   print(rectangle.width)                                     # output - 5.0cm
#   print(rectangle.height)                                    # output - Height must be greater than zero

#   del rectangle.width                                        # output - Width has been deleted
#   del rectangle.height                                       # output - Height has been deleted

# DECoRATOR - A function that extends the behaviour of another function
#             without modifying the base function
#             Pass the base function as an argument to the decorator

#             get_ice_cream("vanilla") - It is a base function where a man need a vanilla flavored ice cream.
#             @add_sprinkles           - It acts as a Decorator where a man need a ice cream with sprinkles but some no need.

#   def add_sprinkles(func):
#       def wrapper(*args, **kwargs):                                         # This wrapper function used to define when the get_ice_cream is called orelse if it is not there then it atomatically print the output without calling the function.
#           print("You add sprinkles")
#           func(*args, **kwargs)
#       return Wrapper

#   def add_fudge(sunc):
#       def wrapper(*args, **kwargs):
#           print("You add fudge")
#           func(*args, **kwargs)
#       return wrapper

#   @add_sprinkles                                             # If you need to add sprinkles then call the add_sprinkles decorator.
#   @add_fudge
#   def get_ice_cream(flavor):
#           print(f"Here is your {flavour} ice cream")
#       

#   get_ice_cream("vanilla")                                            # output - you add sprinkles, you add fudge and here is your ice cream

# EXCEPTION - An event that interrupts the flow of a program
#             (ZeroDivisionError (1/0), TypeError (1 + "1"), ValueError (int("pizza")))
#             1.try, 2.except, 3.finally
#             THERE ARE SO MANY EXCEPTION ARE THERE SO CHECK THE PYTHON OFFICIAL DOCUMENT.

# Syntax
#   try:
#       number = int(input("Enter a number: "))
#       print(1 / number)
#   except ZeroDivisionError:
#       print("You can't divide by zero")
#   except ValueError:
#       print("Enter only numbers please!")
#   except Exception:
#       print("Something went wrong!")
#   finally:
#       print("Do some cleanup here")

# PYTHON FILE DETECTION:

# Syntax for relative path
#   import os
#   file_path = "test folder/test.txt" (It is a relative path. If the file is stored in the current working directory)
#   if os.path.exists(file_path):
#       print(f"The location '{file_path}' exists")
#   else:
#       print("That location doesn't exist")

# Syntax for absolute path
#   import os
#   file_path = "M:\\visual studio\\test.txt" #(It is a absolute file path. If the file is stored in the system)
#   if os.path.exists(file_path):
#       print(f"The location '{file_path}' exists")
#   else:
#       print("That location doesn't exist")

# DID NOT LEARN
# PYTHON WRITING FILES (.txt, .json, .csv)
# PYTHON READING FILES

###@@@@ LAST 3 HOUR VIDEO MUST WATCH

nums = list(map(int, input().split()))
target = int(input())