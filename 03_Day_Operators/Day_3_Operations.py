#Arithmetic operations in Python
#Integers
from difflib import Differ

from mymodule import gravity

print('Addition:', 1 + 2)
print('Subtraction', 2 - 1)
print('Multiplication', 3 * 2)

#please note that Division in Python returns floating numbers
print('Division', 4 /2 )
print('Division', 6 / 2)
print('Division', 7 / 2)

#To print a division as an integer (Without Remainder) the Floor Division should be used '//'
print('Division without Remainder:', 7 // 2)
print('Division without Remainder:', 7 // 3)

#To get the Remainder of a Division the '%' [modulus] operation should be used
print('Modulus', 3 % 2)

print('Exponentiation:', 3 ** 2)


#Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

#Complex Numbers
print('Complex Number:', 1 + 1j)
print('Complex Number Multiplication', (1 + 1j) * (1 - 1j))

#Example of Mathematical Operation using 2 User inputs
#Please remember that the console input is a string!

First_Num = int(input('Please input the First Number: '))
Second_Num = int(input('Please input the Second Number: '))

#Arithmetic operations and assigning the result to a variable
Total = First_Num + Second_Num
Difference = First_Num - Second_Num
Product = First_Num * Second_Num
Division = First_Num / Second_Num
Remainder = First_Num % Second_Num
Floor_Division = First_Num // Second_Num
Exponential = First_Num ** Second_Num

print('First Number + Second Number =', Total)
print('First Number - Second Number =', Division)
print('First Number * Second Number =', Product)
print('First Number / Second Number =', Division)
print('First Number % Second Number =', Remainder)
print('First Number // Second Number =', Floor_Division)
print('First Number ** Second Number =', Exponential)

#Example
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

#declaring the values
num_one = 3
num_two = 4

#Arithmetic operations
Total = num_one + num_two
Difference = num_one - num_two
Product = num_one * num_two
Division = num_one / num_two
Remainder = num_one % num_two

#Printing Values with a label
print('total: ', Total)
print('difference', Difference)
print('product', Product)
print('division', Division)

#Example 2
#Calculating the area of a circle
radius = 10
area_of_circle = 3.14 + radius ** 2
print('Area of a circle:', area_of_circle)

#Claculating area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)\

#Calculating the Weight of an object
mass = 75
Gravity = 9.81
weight = mass * Gravity
print(weight,'N')

#Calculate the density of a liquid
mass = 75 #in Kg
volume = 0.075 #in cubic meter
density = mass / volume