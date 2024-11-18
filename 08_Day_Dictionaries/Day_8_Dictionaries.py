#Day_8_Dictionaries
empty_dict = {}
print(empty_dict)
dct = {'key1':'value1',
       'key2':'value2',
       'key3':'value3',
       'key4':'value4'
       }
print(dct)

#Dictionary Length can be found using the len() method
dct = {'key1':'value1',
       'key2':'value2',
       'key3':'value3',
       'key4':'value4'
       }
print(len(dct))

person = {
    'first_name':'Alexandru',
    'last_name':'Dinu',
    'age':'69',
    'country':'Romania',
    'is_maried':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove Street',
        'zipcode':'696969'
    }
}
print(len(person))

#Accesign Dictionary Items
#To access a dictionary item cna be done using its key value
dct = {'key1':'value1',
       'key2':'value2',
       'key3':'value3',
       'key4':'value4'
       }
print(dct['key1']) #vlaue1
print(dct['key2']) #value2

person = {
    'first_name':'Alexandru',
    'last_name':'Dinu',
    'age':'69',
    'country':'Romania',
    'is_maried':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove Street',
        'zipcode':'696969'
    }
}
print(person['first_name'])  # Alexandru
print(person['country'])     # Romania
print(person['skills'])      # ['Javascript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])   # Javascript
print(person['address']['street'])  # Grove Street
#print(person['city'])        # KeyError: 'city'

#To avoid the key error received when addressing a non-existing key can be done using the get method
print(person.get('first_name'))  # Alexandru
print(person.get('country'))     # Romania
print(person.get('skills'))      # ['Javascript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))        # None

#Adding Items to a Dictionary
dct = { 'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct)

person = {
    'first_name':'Alexandru',
    'last_name':'Dinu',
    'age':'69',
    'country':'Romania',
    'is_maried':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove Street',
        'zipcode':'696969'
    }
}

person['job_title'] = 'Tester'
person['skills'].append('Rust')
print(person)

#Modify items in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value_one'

print(dct)

person = {
    'first_name':'Alexandru',
    'last_name':'Dinu',
    'age':'69',
    'country':'Romania',
    'is_maried':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove Street',
        'zipcode':'696969'
    }
}

person['first_name'] = 'Alexandru-Daniel'
person['age'] = 6969
print(person)

#Check if a key is in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key1' in dct) #True
print('key5' in dct) #Fales

#Removing Key and Value paris from a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') #removes key1 item
print(dct)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() #removes the last item
print(dct)
del dct['key2'] #removes key2 item
print(dct)

person = {
    'first_name':'Alexandru',
    'last_name':'Dinu',
    'age':'69',
    'country':'Romania',
    'is_maried':True,
    'skills':['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Grove Street',
        'zipcode':'696969'
    }
}
print(person)
person.pop('first_name')    #removes the firstname item
print(person)
person.popitem()            #removes the address item
print(person)
del person['is_maried']     #removes the is_maried item
print(person)

#Changing Dictionary to a list of items
#The items() method changes the dictionary to a list of tupels
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())  #dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#Clearing a Dictionary cna be done using clear() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.clear()
print(dct)

#Deleting a Dictionary can be done using the del() method
dct = {'key1':'value1', 'key2':'value2','key3':'value3', 'key4':'value4'}
del dct
#print (dct) #NameError: name 'dct' is not defined.

#Copy a Dictionary can be done using the copy() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)     #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

#Getting Dictionary Keys as a List can be done using keys() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)

#Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)