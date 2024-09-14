#Age as an integer
import math

age = 69
#Height as a float variable
height = 1.75
#Complex number
comp =  2 + 3j

#Script that calculates the area of a triangle
Triangle_Base = int(input('Enter the base of the triangle: '))
Triangle_Height =int(input('Enter the height of the triangle: '))
Triangle_Area = 0.5 * Triangle_Base * Triangle_Height
print('Area of the triangle is:', Triangle_Area)

#Script that calculates the perimeter of a triangle
Side_A = int(input('Enter side A of the Triangle: '))
Side_B = int(input('Enter side B of the Triangle: '))
Side_C = int(input('Enter side C of the Triangle: '))
Triangle_Perimeter = Side_A + Side_B + Side_C
print('Perimeter of the triangle is:', Triangle_Perimeter)

#Length and Width of a rectangle
Rectangle_Width = int(input("Please enter the Width of the rectangle: "))
Rectangle_Height = int(input('Please enter the Height of the rectangle: '))
Rectangle_Perimeter = 2 * (Rectangle_Width + Rectangle_Height)
Rectangle_Area = Rectangle_Height * Rectangle_Width
print('Rectangle Perimeter:', Rectangle_Perimeter)
print('Rectangle Area:', Rectangle_Area)

#Area and Circumference of a circle
Circle_Radius = int(input("Please enter the radius of the circle: "))
Circle_Area = math.pi * (Circle_Radius ** 2)
Circle_Circumference = 2 * math.pi * Circle_Radius
print("Circle Area:", Circle_Area)
print("Circle Circumference:", Circle_Circumference)

#Calculate a slope
First_X = int(input("Please enter the X coordinate for the first point: "))
First_Y = 2 * First_X - 2
Second_X = int(input("Please enter the X coordinate for the second point: "))
Second_Y = 2 * Second_X - 2
Slope = (Second_Y - First_Y)/(Second_X - First_X)
Euclidean_Distance = math.sqrt((Second_X - First_X) ** 2 + (Second_Y - First_Y)^2)
print('The entered points are First Point(',First_X,',',First_Y, 'and Second Point(',Second_X, ',',Second_Y,')')
print('Slope:', Slope)
print('Euclidean Distance:', Euclidean_Distance)

#Comparison between 2 slopes
Slope_GivenValues = (10-2)/(6-2)
if Slope > Slope_GivenValues:
    print('The calculated slope', Slope, 'is greater than the given slope', Slope_GivenValues)
elif Slope < Slope_GivenValues:
    print('The calculated slope', Slope, 'is smaller than the given slope', Slope_GivenValues)
else:
    print('The calculated slope', Slope, 'is equal to the given slope', Slope_GivenValues)

#Find out what for what value x the Y value will be 0
x = 0
while True:
    y = x ** 2 + 6 * x + 9
    if y == 0:
        break
    x -= 1
print('Using the formula for calculating Y = x^2 + 6x + 9, Y will be equal to 0 for X =',x)

#Find the length of 'Python' and 'Dragon' and make a false comparison
print(len('Python') > len('Dragon'))

#Use and operator to check if 'on' is found in both 'Python' and 'Dragon'
print('on' in 'Python' and 'on' in 'Dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon')

#there is no 'on' in both dragon and python
print('on' not in 'Python' and 'on' not in 'Dragon')

#Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('Python'))))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
for i in range(0, 10):
    if i % 2 == 0:
        print(i, 'is an even number')
    else:
        print(i, 'is an odd number')

#The floor division of 7 by 3 is equal to the int converted value of 2.7
print(7//3 == int(2.7))

#Check if type of '10' is equal to 10
print(type('10') == 10)

#Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

Hours = int(input('Please enter the number of hours you worked: '))
Rate = float(input('Please enter the rate per hour: '))
print('Your earnings are:', Hours * Rate)

#Write a script that prompts the user to enter the number of years lived. Calculate the number of seconds lived.
years = int(input('Please enter the number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
remaining_seconds = (100-years) * 365 * 24 * 60 * 60
print('You have lived for', seconds, 'seconds', 'and you have', remaining_seconds, 'seconds remaining')

#Write a python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)