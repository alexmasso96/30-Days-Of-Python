#1. Create an empty dictionary called dog
cat = {}
print(cat)

#2. Add name, color, breed, legs, age to the cat dictionary
cat['Name'] = 'Jessy'
cat['Color'] = 'Tuxedo'
cat['Breed'] = 'Tomberoneza'
cat['Legs'] = 4
cat['Age'] = 2
print(cat)

#3. Create a student Dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    'First_Name':'Alexandru',
    'Last_Name':'Dinu',
    'Gender':'Male',
    'Age':28,
    'Marital_Status':True,
    'Skills':['Python', 'C++', 'Rust'],
    'Country':'Romania',
    'City':'LA',
    'Address' : {'Street':'Grove Street', 'Postal_Code':'696969'}
}
print(student)

#4. Get the length of the student dictionary
print('The length of the student dictionary is:', len(student))

#5. Get the value of skills and check the data type
print('My skills are', student['Skills'], ' and the data type is', type(student['Skills']))

#6. Modify the skills values by adding one or two skills
student['Skills'].append('Java')
student['Skills'].append('TypeScript')
print('My new skills are:', student['Skills'])

#7. Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)

#8. Get the dictionary items as a list
values_list = student.values()
print(values_list)

#9. Change the dictionary to a list of tuples using items() method
print(student.items())

#10. Delete one item in the dictionary
student.pop('Gender')
print(student)

#11. Delete one of the dictionaries
del cat
#pritn(cat)