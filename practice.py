''' 
#variable = A container for a value (string, integer, float, boolean)
#           A variables behaves as if it was the value it contains



#strings

first_name = "bro"
food = "pizza"
email = "nithin@gmsil.com"

#integers 

age = 25 
quantity = 3
number_of_students = 30

#float

price = 10.99
gpa = 3.2
distance = 5.5

#Boolean

is_student = True
for_sale = True
if_online = True

'''


#Typecasting = the process of converting a variable from one data type to another data type 
#              str(), int(), float(), bool()
'''
name = "Nithin"
age = 21 
gpa = 3.9
is_student = True

name = bool(name)
age = float(age)
print(age)
print(name)

'''


#input () = A function tha prompts the user to enter data 
#           Returns the entered data as a string
''''
name = input("What is your name?: ")
age = int(input("How old are you"))


age = age + 1

print(f"hello {name}!")
print(f"You are {age} years old")
'''

# Exercise 1 Rectangle Area calculation
'''
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is {area} cm")


'''
#Exercise 2 Shopping cart program
'''

item = input("What item would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

'''

#Madlibs game
#word game where you create a story 
#by filling in blanks with random words
'''
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description): ")


print(f"Today i went to a {adjective1} zoo.")
print(f"In a exhibit , I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
'''
#Arithmetic operators
'''
friends = 5
#frineds = friends + 1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
#friends = friends / 2
#friends /= 2
#friends = friends ** 2 
#friends **= 2
#remainder = friends % 3
print(friends)
'''
# Math related functions
'''
x = 3.14
y = 4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)
#result = max(x, y, z)
#result = min(x, y, z)

print(result)
'''
'''
import math

x = 9.9

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)
print(result)

'''

#calculating circumference of a circle 
'''
radius = float(input("enter the radius of circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
'''

#calculating area of a circle 
'''
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)

print(f"The are of the circle is:{round(area, 2)}cm^2")
'''

#calculating hypotenuse of right ANGLE TRAINGLE
'''
import math
a = float(input("Entert side A: "))
b = float(input("Entert side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side C = {round(c, 2)}")
'''

#if = Do some code only IF some condition is True
#     Else do something else
'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old")
else:
    print("You must be 18+ to sign up")
'''
#python calculator
'''
operator = input("Enter an operator (+ - * /):")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("You entered a invalid operator")
'''
#python weight converter
'''
weight = float(input("Enter the weight"))
unit = input("Enter your weight as 'K' for kilogram and 'L' for pounds: ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"The weight is{round(weight, 2)} {unit}]")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"The weight is {round(weight, 2)} {unit}")
else:
    print(f"The entered unit {unit} is invalid ")
'''
#Tempreature coversion program 
'''
unit = input("Is this tempreature in celcius or farenhiet (c/f): ")
temp = float(input("Enter the tempreature: "))

if unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The tempreature in farenhiet is: {temp} F")
elif unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print (f"The temperature in celcius is: {temp}")
else:
    print(f"{unit} is unvalid unit of measuremnet")

'''
#logical operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be true 
#                    and = both conditions must be true 
#                    not = inverts the condition (not false, not true)

#or
'''
temp = 40
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The plan is cancelled")
else:
    print("The plan is on")
'''
#and/ not
'''
temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")
'''

#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         x if condition else Y
'''
num = 6
a = 6 
b = 7
age = 13 
tempreature = 30 
user_role = "admin"
#print("Positive" if num > 0 else "Negative" )
#result = "Even" if num % 2 == 0 else "odd"
#min_num = a if a < b else b
#max_num = a if a > b alse b
#status = "Adult" if age >= 18 else "child"
#weather = " HOT" if tempreature > 30 else "COLD"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)
'''
'''
name = input("Enter your full name: ")
phone_number  = input("Enter your phone#: ")
#result = len(name)
#result = name.find("N")
#result = name.rfind("r")
#name = name.capitalize()
#name= name.upper()
#name = name.lower()
#result = name.isdigit()#finds only digit#
#result = name.isalpha()#true when there is words only continous name.
#result = phone_number.count("-")
#result = phone_number.replace("-", " ")
result
print(result)
'''

#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces 
#3. username must not contain digits
'''
username = input("Eter a user name: ")


if len(username) > 12:
    print("Your user name can't be more than 12 characters. ")
elif not username.find(" ") == -1:
    print("Your username cant't contain spaces")
elif not username.isalpha():
    print("Your username can't conatain numbers")
  

else:
    print(f"Welcome {username}")
'''

#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]
'''
credit_number = "1234-5678-9012-3546"
#print(credit_number[0])
#print(credit_number[:4])
#print(credit_number[5:9])#(starting is inclusive and ending is exclusive))
#print(credit_number[5:])#starting to end
#print(credit_number[-1])#starts from the reverse
#print(credit_number[::3])#strats from 3 number

#last_digits = credit_number[-4:]
#print(f"xxxx-xxxx-xxxx-{last_digits}")

#credit_number = credit_number[::-1]#prints the number from reverse
#print(credit_number)
'''
# format specifiers = {value:flags} format a value based on what 
#                      flags are inserted


# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify 
# :^ = center align 
# :+ = use a plus sign to indicate positive value 
# := = place sign to leftmost position
# : = insert a space before positive numbers 
# :, = comma seperator              
'''
price1 = 3.14576
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1: .3f}")
print(f"Price 2 is ${price2: .3f}")
print(f"Price 3 is ${price3: .3f}") 
'''
'''
price1 = 3.14576
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}") 
#output
Price 1 is $   3.14576
Price 2 is $   -987.65
Price 3 is $     12.34
'''

'''
price1 = 3.14576
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}") 
#output
Price 1 is $0003.14576
Price 2 is $-000987.65
Price 3 is $0000012.34
'''
'''
price1 = 3.14576
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}") 
#output
Price 1 is $+3.15
Price 2 is $-987.65
Price 3 is $+12.34
'''

#while loop = execute some code WHILE some condition remains true
'''
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")
'''

'''
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")
'''

'''
num = int(input("Enter a # between 1 - 10"))

while num < 1 or num > 10:
    #print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")
'''

#Python compound intrest calculator
'''
principle = 0
rate = 0
time = 0

while True:
    principle = int(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = int(input("Enter the intrest rate: "))
    if rate <= 0:
        print("intrest can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

'''

#for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.
'''
credit_card = "1234-5678-91678-6868"
for x in credit_card:
    print(x)
'''

for x in credit_card:
    print(x)