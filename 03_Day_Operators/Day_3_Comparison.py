#Comparison Operations

"""
Operator        Name                            Example
==              Equal                           x == y
!=              Not Equal                       x != y
>               Greater than                    x > y
<               Less than                       x < y
>=              Greater than or equal to        X >= y
<=              Less than or equal to            x <= y
"""


#Examples
print( 3 > 2)        #True, because 3 is greater than 2
print( 3 >= 2)       #True, because 3 is greater than 2
print( 3 < 2)        #False, because 3 is greater than 2
print( 2 < 3)        #True, because 2 is less than 3
print( 2 <= 3)       #True, because 2 is less than 3
print( 3 == 2)       #False, because 3 is not equal to 2
print( 3!= 2)        #True, because 3 is not equal to 2

print(len('mango') == len('avocado')) #False
print(len('mango') != len('avocado')) #True
print(len('mango') < len('avocado')) #True
print(len('milk') != len('meat')) #False
print(len('milk') == len('meat')) #True
print(len('tomato') == len('potato')) #True
print(len('python') > len('dragon')) #False

#Comparing something returns either true or false
print('True == True', True == True)
print('True == False', True == False)
print('False == False', False == False)

"""
in addition to the above mentioned comparison operations in python we also have
is => Returns true if both variables are the same
is not => Returns true if both variables are different
in => Returns true if a list contains a certain item
not in => Returns true if an item is not in a list
"""

print('1 is 1', 1 is 1) #True, because data values are the same
print('1 is not 2', 1 is not 2) #True, because 1 is not 2
print('A is in Alexandru', 'A' in 'Alexandru') #True, because A is in Alexandru
print('B is in Alexandru', 'B' in 'Alexandru') #Flase, because B is not in Alexandru
print('codding' in 'codding for all') #True, because codding for all has the world codding
print('a in an:', 'a' in 'an:') #True
print('4 is 2 ** 2', 4 is 2 ** 2) #True

"""
Logical operations

Python uses keywords to perform logical operation instead of symbols

and
or
not
"""

#Examples
print(3 > 2 and 4 > 3) #True, because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False