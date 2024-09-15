#Day 4 Strings
import math

#Creating a string
letter = "P"    #String with single character
print(letter)   #P
print(len(letter))  # 1
greeting = "Hello, World!"  #a string can be made using a single or double quote, 'Hello, World!' is a string
print(greeting) #Hello, World!
print(len(greeting)) #13
sentence = 'I hope you enjoy 30 days of Python Challenge'
print(sentence)

#Multiline strings can be made using triple simple (''') or double quotes (""")
multiline_string = '''I am a teacher and enjoy teaching.
i didn't find anything as rewarding as empowering people.
That is whi I created 30 days of python'''
print(multiline_string)
multiline_String = """I am a teacher and enjoy teaching.
i didn't find anything as rewarding as empowering people.
That is whi I created 30 days of python"""

#String Concatenation
first_name = 'Alexandru'
last_name = 'Dinu'
space = ' '
full_name = first_name + space + last_name
print(full_name) #Alexandru Dinu
#Checking the length of a string using len() built-in function
print(len(first_name)) #9
print(len(last_name))   #4
print(len(first_name)>len(last_name))   #True
print(len(full_name))   #14

"""Escape Sequence in Strings
\n : New Line
\t : Tab (8 spaces)
\\ : Back Slash
\' : Single Quote
\" : Double Quote
"""
#Examples of escape Sequences
print('I hope everyone is enjoying the Python Challenge. \nAre you?') #line break
print('Days\tTopics\tExercises') #adding tab space or 8 spaces
print('Day 1\t5\t\t5')
print('Day 2\t6\t\t20')
print('Day 3\t5\t\t23')
print('Day 4\t1\t\t35')
print('this is a backslash symbol (\\)') #to write a backslash
print('In every programming language is starts with \"Hello, World!\"')

#String Formatting
"""
Old style Formatting (% Operator)

In Python there are many ways of formatting strings. In this section, we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digits".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digits f" - Floating point numbers with fixed precision
"""

#Strings only
first_name = "Alexandru"
last_name = 'Dinu'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

#strings and numbers
radius = 69
pi = 3.14
area = pi * radius ** 2
formated_String = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_String)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_String = 'The following are python libraries:%s' % python_libraries
print(formated_String)

#Mew Style formatting introduced in python Version 3.
first_name = 'Alexandru'
last_name = 'Dinu'
language = 'Python'
formatted_string = 'I am {}{}. I teach {}'.format(first_name, last_name, language)
print (formatted_string)

a = 3
b = 4
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a +- b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

#Strings and numbers
radius = 69
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}'.format(radius,area)
print(formated_string)

#String Interpolation / f.strings(Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Python Strings as Sequences of Characters
language = 'Python'
a,b,c,d,e,f = language #unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#accessign Characters in String by Index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
print(language[len(language)-1])

#We can also use negative Indexing to access a specific character from a string
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last_letter = language[-2]
print(second_last_letter)

#Slicing Python Strings
language = 'Python'
first_three = language[0:3] #Starts at index 0 and up to 3 not including 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three)    #hon
#Another way
print(language[-3:])    #hon
print(language[3:])      #hon

#Rversing Strings
greeting = 'Hello, World!'
print(greeting[::-1]) #!dlroW ,olleH

#Skipping Characters while slicing in Python
language = 'Python'
pto = language[0:6:2]
print(pto)

#String Methods
#capitalize(): converts the first letter of a string into a capital letter
challenge = 'thirty days of python!'
print(challenge.capitalize()) #Thirty days of python!

#Count(): returns the nuber of occurrences of a sub string, count(substring, start = ..., end = ...)
print(challenge.count('y')) #3
print(challenge.count('y',7,14))
print(challenge.count('th'))

#endswith(): Checks if string with a specific substring
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

#expandtabs(): Replaces tab character with spaces, default tab size is 8. it takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#find(): Returns th index of the first occurrence of a substring. if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

#rfind(): Returns the index of the last occurrence of a substring. if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

#format(): formats the string into a nicer output
first_name = 'Alexandru'
last_name = 'Dinu'
age = 69
job = 'tester'
country = 'Romania'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence)

radius = 69
pi = math.pi
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print (result)
print('the area of a circle with radius {} is {}'.format(radius, area))
result = 'THE area of a circle with radius {} is {}'.format(radius, area)
print(result)

#index(): Returns the lowest index of a substring, additional arguments indicate string starting and ending index (default 0 and string length -1).
#If the substring is not found it raises a valueError
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) #7
print(challenge.index(sub_string, 0, 9))

#ridnex(): Returns the highest index of a substring, additional arguments indicate starting adn ending index (default 0 and string length -1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string, 0,9))

#isalum(): Checks alphanumeric character
challenge = 'thirtydaysofpython'
print(challenge.isalnum()) #True

challenge = 'ThirtyDaysOfPhyton'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum()) #fales because space is not an alphanumeric character

challenge = 'Thirty days of python 2024'
print(challenge.isalnum())

#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'Thirty days of Python'
print(challenge.isalpha()) #Flase, Space is excluded
challenge = 'ThirtydaysofPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())

#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge)
print(challenge.isdecimal())
challenge = '12 3'
print(challenge.isdecimal())

#isdigit(): Checks if all characters in a string are numbers(0-9 and some Unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) #False
challenge = '30'
print(challenge.isdigit()) #True
challenge = '\u00b2'
print(challenge)
print(challenge.isdigit())

#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit()) but it accepts more symbols
num = '10'
print(num.isnumeric()) #True
num = '\u00bD'
print(num)
print(num.isnumeric()) #True
num = '10.5'
print(num.isnumeric()) #Flase

#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) #Falsem because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) #True

#islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = "30 days of python"
print(challenge.islower())
challenge = 'Thirty Days of Python'
print(challenge.islower())

#isupper(): Checks if all characters in a string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = '30 DAYS OF PYTHON'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#'.join(web_tech)
print(result)
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

#strip(): Removes all given characters starting from the beginning adn end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'codding'))

#split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))

#swapcase(): converts all uppercase characters to lowercase and all lowercase to uppercase
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.swapcase())

#startswith(): Checks if string starts with specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = 'Thirty days of python'
print(challenge.startswith('thirty'))


challenge = '30 Days of Ptthon'
print(challenge.startswith('thirty'))