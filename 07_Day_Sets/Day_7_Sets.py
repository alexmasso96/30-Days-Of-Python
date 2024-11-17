#Creating an empty set
st = set()

#Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

#length of a set using len() method
st = {'item1', 'item2', 'item3', 'item4'}
print ('Length of the set:', len(st))
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Length of fruits:', len(fruits))

#Checkign an item in a string
st = {'item1', 'item2', 'item3'}
print('Does set st contain item 3? ', 'item3' in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

#Adding items to a set
st = {'item1', 'item2', 'item3'}
st.add('item4')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

#To add multiple items to a set we use update()
st.update(['item5', 'item6', 'item7'])
print(st)

vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

#Remove an item from a set
st = {'item1', 'item2', 'item3'}
st.remove('item2')
print(st)

#pop() method removes a random item form a list and returns the removed item
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)
print (fruits)

#Clearing Items in a set can be done using clear() method

st  = {'item1', 'item2','item3', 'item4'}
print(st)
st.clear()
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits.clear()
print(fruits)

#Deleting Set can be done using del method
st = {'item1', 'item2', 'item3', 'item4'}
del st
#print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
#print(fruits)

#Converting List to Set
lst = ['item1', 'item2', 'item3', 'item4']
st = str(lst)
print(lst)
print(st)

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
print(fruits)
print(type(fruits))
frutis = set(fruits)
print(type(frutis))

#Joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st1)
print(st2)
print(st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(vegetables))

# update() method ads the items of one set to another
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
print(st1)
print(st2)
st1.update(st2)
print(st1)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits)
print(vegetables)
fruits.update(vegetables)
print(fruits)

#Finding the intersection of two sets can be done using the intersection() method
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.intersection(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))

#Checking subset and SuperSet
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))
print(st1.issuperset(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(even_numbers.issuperset(whole_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issubset(dragon))

#Checking the difference Between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1', 'item2'}
print(st2.difference(st1))
print(st1.difference(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))
print(dragon.difference(python))

#finding symmetric difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.symmetric_difference(st2))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(st2))
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

#Joining Sets
st1 = {'itme1', 'itme2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))
print(st1.isdisjoint(st2))

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))