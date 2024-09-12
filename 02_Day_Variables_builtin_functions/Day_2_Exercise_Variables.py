#Day 2: 30 Days of Python Programming
import math

First_Name = 'Alexandru-Daniel'
Last_Name  = 'Dinu'
Full_Name = 'Alexandru Daniel Dinu'
Country = 'Romania'
City = 'Craiova'
Age = 69
Current_Year = 2024
Is_Maried = True
Is_True = False
Is_Light_On = True
Multiple, Variables, In, A, Line = 'Multiple', 'Variables', 'In', 'A', 'Line'

#Ecercise Level 2

#Check Data Types of all declared Variables
print(type(First_Name))
print(type(Last_Name))
print(type(Full_Name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Current_Year))
print(type(Is_Maried))
print(type(Is_True))
print(type(Is_Light_On))
print(type(Multiple), type(Variables), type(In), type(A), type(Line))

#Length of First Name
print('Length of the First Name Variable', First_Name, 'is', len(First_Name))

#compare the Length of First Name to the Last Name
if(len(First_Name)>len(Last_Name)):
    print('Length of the First Name: ', First_Name, 'is', len(First_Name),
          'which is greater than the length of Last Name:', Last_Name, ':', len(Last_Name))
elif(len(First_Name)<len(Last_Name)):
    print('Length of the First Name: ', First_Name, 'is', len(First_Name),
          'which is smaller than the length of Last Name:', Last_Name, ':', len(Last_Name))
else:
    print('Length of the First Name: ', First_Name, 'is', len(First_Name),
          'which is equal to the length of Last Name:', Last_Name, ':', len(Last_Name))

#Calculus
Num_One = 5
Num_Two = 4
Total = Num_One + Num_Two
Dif = Num_Two - Num_One
Product = Num_Two * Num_One
Division = Num_One / Num_Two
Remainder = Num_Two % Num_One
Exp = Num_One ** Num_Two
Floor_Division = Num_One // Num_Two

#Calculus with Circles
Radius = 30

"The standard value of PI in python can be used as math.pi which is equal to: "
print(math.pi)

Area_Of_Circle = math.pi * Radius ** 2
print(Area_Of_Circle)
Circumference_Of_Circle = 2 * math.pi * Radius
print(Circumference_Of_Circle)

#Area and Circumference of a Circle with the Radius as a Usr input
Radius_Usr = int(input('Please enter the Radius of the Circle: '))
Area_Of_Circle_Usr = math.pi * (pow(Radius_Usr, 2))
Circumference_Of_Circle_Usr = 2 * math.pi * Radius_Usr
print('The Area of the circle with the Radius:', Radius_Usr, 'is', Area_Of_Circle_Usr, 'and the Circumference is:', Circumference_Of_Circle_Usr)

#User input for the First Name, Last Name, and Country
First_Name = input('Please enter First Name: ')
Last_Name = input('Please enter the Last Name: ')
Country = input('Please enter the User country: ')
Age = input('Please enter the User age: ')
Age_2 = int(input('Please enter the User age again:'))

#printing of the variables after the user input
print(First_Name)
print(Last_Name)
print(Country)
print(Age)
print('The data type for the First Age variable is:', type(Age))
print(Age_2)
print('The Data type for the Second Age variable is:', type(Age_2))
print('Please note that the input data from the terminal is always a string and needs to be converted to the appropriate Data Type')
'''Please Note that the input Data from the terminal is always a string and needs to be converted to the appropriate Data Type'''

print(help('keywords'))