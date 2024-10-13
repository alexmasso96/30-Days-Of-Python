#Creating a tuple
empty_tuple = ()
empty_tuple = tuple()

#Tuple with Initial Values
tpl1 = ('item1', 'item2', 'item 3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(tpl1)
print(fruits)

#Tuple Length
print(len(tpl1))

#Accessing Tuple Items
first_item = tpl1[0]
print(first_item)
second_item = tpl1[1]
print(second_item)

first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[len(fruits)-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)

#Negative indexing
tpl = ('item1', 'item2', 'item3', 'item4')
print(tpl)
first_item = tpl[-4]
second_item = tpl[-3]
print(first_item)
print(second_item)

first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)

#slicing Tuples
all_items = tpl[0:4]
print(all_items)
all_items = tpl[0:]
print(all_items)
middle_two_items = tpl[1:3]
print(middle_two_items)

all_fruits = fruits[0:4]
print(fruits)
all_fruits = fruits[0:]
print(fruits)
orange_mango = fruits[1:3]
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

#changing a tuple to a List
tpl = ('item1', 'item2', 'item3', 'item4')
print(tpl)
lst = list(tpl)
print(lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
fruits = list(fruits)
print(fruits)
print(fruits[0])
fruits = tuple(fruits)
print(fruits)

#Checking an item in a Tuple
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
print('orange' in fruits)
print('apple' in fruits)

#Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print(tpl1)
print(tpl2)
print(tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits)
print(vegetables)
print(fruits_and_vegetables)

#deleting Tuples
del tpl1
del fruits