#1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

#2. Create a tuple containing names
brothers = ('Marian', 'Mariann', 'Mariannn', 'Mariannnn', 'Mariannnnn')
print(brothers)
sisters = ('Mariana', 'Marianaa')
print(sisters)

#3. Join brothers and sisters tuples and assign it tu siblings
siblings = brothers + sisters
print(siblings)

#4 How many siblings do you have?
print('Number of siblings: ', len(siblings))

#5. Modify the sibling tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings) + ['Maricica', 'Maricel']
siblings = tuple(siblings)
family_members = siblings
print(siblings)
print(family_members)