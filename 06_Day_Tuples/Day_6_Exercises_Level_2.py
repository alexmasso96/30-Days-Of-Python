#1. Unpack siblings and parents from family_members
family_members = ('Alex','Iza', 'Remus')
father, mother, son , *siblings= family_members
print('Father:', father) # Father: Alex
print('Mother:', mother) # Mother: Iza
print('Son:', son) # Son: Remus

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to food_stuff_tp
fruits = ('banana', 'orange', 'apple')
vegetables = ('tomato', 'potato', 'carrot')
animal_products = ('milk', 'cheese', 'meat')

food_stuff_tp = fruits + vegetables + animal_products
print('Joined Tuple:', food_stuff_tp)

#3. change the about food_stuff_tp tuple to food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('The touple converted into list:', food_stuff_lt)

#4. slice out the middle item or items from the food_stuf_tp tuple or food_stuff_lt list
middle_item = food_stuff_lt[len(food_stuff_lt)//2]
print('Middle Item:', middle_item)

#5. Slice out the first three items and the last three items from food_stuff_lt list
first_3_elements = food_stuff_lt[0:3]
print ('The First 3 elements are:', first_3_elements)
last_3_elements = food_stuff_lt[-3:]
print('The Last 3 elements are:', last_3_elements)
elements = first_3_elements + last_3_elements
print('The Combined List is:', elements)

#6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

#Check if Estonia is a nordic country
print('Estonia' in nordic_countries)

#Check if Iceland is a nordic country
print ('Iceland' in nordic_countries)