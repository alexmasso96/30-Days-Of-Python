#Variables in Python
First_Name = "Alexandru"
Last_Name = "Dinu"
Country = "Romania"
City = "Craiova"
Age = 69
Is_Maried = True
Skills  = ['C', 'C++', 'Python', 'Capl']
Person_Info = {
    'firstname':'Alexandru Daniel',
    'Name':'Dinu',
    'Country':'Romania',
    'city':'Craiova'
}

#Some Print Examples
print('Hello World')                #Print a single argument
print('Hello', ',', 'World', '!')   #Print multiple arguments
print(len('Hello World!'))          #Len function takes only one argument and it will print the length of the string

#Print Examples using multiple argments
print('First Name:', First_Name)
print('First Name: ', First_Name)
# printing with multiple arguments automatically adds a space between each argument


#Print Examples based of the Variable declarations from line 2 to 14
print('First Name:', First_Name)
print('First Name Length:', len(First_Name))
print('Last Name:', Last_Name)
print('Last Name Length:', len(Last_Name))
print('Country:', Country)
print('City:', City)
print('Age:', Age)
print('Maried', Is_Maried)
print('Skills:', Skills)
print('Person information:', Person_Info)