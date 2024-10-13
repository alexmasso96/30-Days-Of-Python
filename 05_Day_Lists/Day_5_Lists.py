# Day 5 Lists

#A list can be build using the list() function
empty_list = list()
print(len(empty_list))

#Using square brackets []
empty_list = []
print(len(empty_list))

#List examples
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

#print the lists adn the length
print('Fruits:', fruits)
print('Number of Fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animal Products:', animal_products)
print('Number of Animal Products:', len(animal_products))
print('Web Technologies:', web_techs)
print('Number of Web Technologies:', len(web_techs))
print('Countries:', countries)
print('Number of Countries:', countries)

# Lists can have multiple data types
new_list = ['Alexandru', 250, True, {'Country':'Romania', 'City':'Craiova'}] #list containing different data types
print(new_list)

#Accesing list items using positive indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
third_fruit = fruits[2]
print(third_fruit)
forth_fruit = fruits[3]
print(forth_fruit)

#last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

#Accessing list items using negative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last_fruit = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last_fruit)

#Unpacking List Items
lst = ['item1', 'item2', 'item3', 'itm4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

#Example
fruits = ['bananna' ,'orange ', 'mango','lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
#example
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
#example
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, sw, *scandic, es = countries
print(gr)
print(fr)
print(sw)
print(scandic)
print(es)

#Slicing items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] #will take all values from the interval 0-4
print(all_fruits)
all_fruits = fruits[0:] #if an end value is not provided the interval will be form start (0 in our case) to the end
print(all_fruits)
orange_and_mango = fruits[1:3] #it will take the values in the interval 1-3 (index 1 and 2)
print(orange_and_mango)
orange_mango_lemon = fruits[1:] #will take all values from 1 to the end of the list
print(orange_mango_lemon)
orange_and_lemon = fruits[::2] #the third argument is used as a step in this chase the list wil be orange and lemon
print(orange_and_lemon)

#Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] #it returns all the fruits
print(all_fruits)
orange_and_mango = fruits [-3:-1] #it will not include the first and last index
print(orange_and_mango)
orange_mango_lemon = fruits[-3:] #the list will start form the second item in the list to the end
print(orange_mango_lemon)
reverse_fruits = fruits[::-1] #a negative step will return the list in reverse order
print(reverse_fruits)

#Modifying lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
fruits[len(fruits)-1] = 'lime'
print(fruits)

#Checking items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print('banana' in fruits)
print('lime' in fruits)

#adding items to a list
#To add an item to the end of an existing list can be done using append()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

#Inserting items into a list
#To inset an item in a list wee cna use insert()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.insert(2, 'apple') # inserts apple at index 2
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

#Removing Items from a list
#to remove an item from a list we can use remove() method
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

#Remove items using Pop
#the pop() methods removes the specified index or the last index if none is provided
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

#Remove items from a list using del()
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits #deletes the list completely so no print is possible
#print(fruits)

#Clear items from a list can be done using the clear() method
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print(fruits.clear())

#Copying a list
"""Copying a list can be done using the '=' operator: list2 = list1. Now list2 is a reference of list1
so any modification in list2 is also visible in list1.
We can also make a coppy using the coppy() method. This will make a truly different coppy of list 2"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits
print('fruits_copy = fruits')
print("Fruits", fruits)
print("Fruits_copy", fruits_copy)
print('Fruits.clear()', fruits.clear())
print("Fruits_copy", fruits_copy)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print('fruits_copy = fruits.copy()')
print('Fruits', fruits)
print('Fruits_copy', fruits_copy)
print('Fruits.clear()', fruits.clear())
print('Fruits_copy', fruits_copy)

#Joining Lists
#Plus Operator (+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#joining using extend() allows to append a list in a list
num1 = [0, 1, 2, 3]
num2 = [4, 5]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5, -4, -3, -2, -1,]
zero = [0]
positive_numbers = [1, 2, 3, 4, 5]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers: ", negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits.extend(vegetables)
print('Fruits and Vegetables:', fruits)

#Counting items in a list count()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('banana'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#Finding the index of an item can be done using index()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

#Sotring list items can be done using the sort() method
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits: ', fruits)
fruits.sort()
print('Fruits_Sort: ', fruits)
fruits.sort(reverse=True)
print('Fruits_Sort_reverse', fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('ages:', ages)
ages.sort()
print('ages_sort:', ages)
ages.sort(reverse = True)
print('ages_sort_reverse:', ages)

#Sorted() returns the ordered list without modifying the original
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits_Original:', fruits)
print('Fruits_Sorted',sorted(fruits))
print('Fruits_Sorted_Reversed', sorted(fruits, reverse = True))
print('Fruits_Original ', fruits)

