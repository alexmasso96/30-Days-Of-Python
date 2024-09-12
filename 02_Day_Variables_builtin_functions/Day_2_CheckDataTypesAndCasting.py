#from import new_module

First_Name = 'Alexandru Daniel'     #str
Last_Name = 'Dinu'                  #str
Country = 'Romania'                 #str
City = 'Craiova'                    #str
age = 69

#print out types
print(type("Alexandru Daniel"))     #str
print(type(First_Name))             #str
print(type(10))                     #int
print(type(3.14))                   #float
print(type(3 + 2j))                 #complex
print(type(True))                   #Bool
print(type([1, 2, 3, 4]))           #list
print(type({"name":"Alexandru", "age":39, "is_maried":True})) #Dict
print(type((1,2)))                  #Tuple
print(type(zip([1,2],[3,3])))       #set

'''Casting: Converting one data type to another data type. 
We use int(), float(), str(), list, set 
When we do arithmetic operations string numbers should be first converted to int or float
otherwise it will return an error. If we concatenate a number with a string, the number should be 
first converted to a string. We will talk about concatenation in String section.'''

#int to Float
num_int = 10
print('num_int:', num_int)
num_float = float(num_int)
print('num_float', num_float)

#Float to Int
gravity = 9.81
print(type(gravity), ':', gravity)
print(type(int(gravity)), ':', int(gravity))

#int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

#str to int or float
num_str = "10.6"
print("num_int:", int(float(num_str)))
print("num_float:", float(num_str))

#Str to List
First_Name = "Alexandru Daniel"
print(First_Name)
First_Name_List = list(First_Name)
print(First_Name_List)
