#this is a comment

"""This is a multiline comment
It can be used on multiple lines"""

"""Multiple Data Types Try!"""


My_Int = 3
My_Float = 4.5
My_List = [1, 2, 3, 4] #a cna have any data type inside (float, int, string, bool)
My_Bool = True
My_Dict = {
    'Name':'Alexandru-Daniel Dinu',
    'E-Mail':'alexmasso96@gmail.com',
    'Age': 69,
    'Programming_Languages':['C++', 'Python'],
}
My_Tuple = {1, 2, 3, 4}

#Print Exercise of the types and the variables :D

#Int
print("The value of My_Int is:" + str(My_Int) + ". The type is " + str(type(My_Int)))

#Float
print("The value of My_Float is:" + str(My_Float) + ". The type is " + str(type(My_Float)))

#List
print("The value of My_List is:" + str(My_List) + ". The type is " + str(type(My_List)))
#List print only one element in loop
print("Print only one element from the List in a 'For' lopp")
for i in range(len(My_List)):
    print("The value of element " + str(i) + " from the List is: " + str(My_List[i]) + ". The type of the element is " + str(type(My_List[i])))


#Bool
print("The value of My_Bool is: " + str(My_Bool) + ". The type is " + str(type(My_Bool)))

#Dict
print("The value of My_Dict is: " + str(My_Dict) + ". The type is " + str(type(My_Dict)))
#Each element of the dictionary is also addresable separately
print("The value of My_Dict: Name is: " + str(My_Dict['Name']) + ". The type is " + str(type(My_Dict['Name'])))
print("The value of My_Dict: E-Mail is: " + str(My_Dict['E-Mail']) + ". The type is " + str(type(My_Dict['E-Mail'])))
print("The value of My_Dict: Age is: " + str(My_Dict['Age']) + ". The type is " + str(type(My_Dict['Age'])))
print("The value of My_Dict: Programming_Languages is: " + str(My_Dict['Programming_Languages']) + ". The type is " + str(type(My_Dict['Programming_Languages'])))

#Tuple
print("The value of My_Tuple is: " + str(My_Tuple) + ". The type is " + str(type(My_Tuple)))



#Day 1 - 30 Days of Python Challange

#Math Operations
print (2 + 3)   #Addition(+)
print (2 - 3)   #Subtraction (-)
print (2 * 3)   #Multiplication (*)
print (3 / 2)   #Division (/)
print (3 ** 2)  #Exponential (**)
print (3 % 2)   #Modulus (%)
print (3 // 2)  #Floor division (//)


"""Check Data types (Again)
this is just a coppy paste from the Example Project"""
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple