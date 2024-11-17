#Sets
from os.path import split

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 26, 24, 25, 24]

#1. Convert the ages of a set and compare the length of the list and set, which one is bigger?
age_set = set(age)
print('length of list:', len(age))
print('length of set:', len(age_set))
print('Length of list bigger than set',len(age)>len(age_set))

#2. Explain the difference between the following data types: string, list, tuple, and set
print('List: is a collection of items, it is ordered and changeable. It allows duplicate members.')
print('Tuple: is a collection of items, it is ordered and unchangeable. It allows duplicate members.')
print('Set: is a collection of items, it is unordered and unindexed. It does not allow duplicate members.')
print('Dictionary: is a collection of items, it is unordered, changeable and indexed. It does not allow duplicate members.')

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence. Use the split() method and set to get the unique worlds
string = 'I am a teacher adn I love to inspire and teach people'
sets = set(string.split(' '))
print('In the string there are ', len(sets),' unique words.')