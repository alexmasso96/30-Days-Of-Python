#Ecercises Day 5 Level 1

# 1. Declare an empty list
empty_list = []
print(empty_list)

# 2. Declare a list with more than 5 items
integers = [1, 2, 3, 4, 5, 6, 7]
print(integers)

# 3. Find the length of the list
print('Length of list integers is: ', len(integers))

# 4. Get the first Item, the middle item and the last item of the list
print('First Item: ', integers[0])
middle = len(integers) / 2
print('Middle Item: ', integers[int(middle)])
print('Last Item: ', integers[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Alex', 69, 1.75, True, 'Romania']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print (it_companies)
print (mixed_data_types)

#8. Print the number of companies in the list
print (len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[0] = 'Faurecia'
print (it_companies)

#11. Add an IT company to it_companies
it_companies.append('Forvia')
print(it_companies)

#12.Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2),'Hella')
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded)
it_companies[it_companies.index('Hella')] = it_companies[it_companies.index('Hella')].upper()
print(it_companies)

#14. Join the it_companies with a string '#, '
it_companies.append('#, ')
print (it_companies)

#15. Check if a certain company exists in the it_companies list.
print(it_companies.index('Forvia'))

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print (first_three)

#19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print (last_three)

#20. Slice Out the middle IT company or companies form the list
middle_company = it_companies[int(len(it_companies)/2)]
print(middle_company)

#21. remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company from the list
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

#23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies
#print (it_companies)

#26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'express', 'MongoDB']
web_development = front_end + back_end
print(web_development)

#27. After joining the list in question 26. Coppy the joined list and assign it to a variable full_stack. Than insert Python and SQL after Redux
full_stack = web_development.copy()
for i in range(full_stack.index('Redux')+1, full_stack.index('Redux') + 3):
    full_stack.insert(i,'Python') if i == full_stack.index('Redux')+1 else 'SQL'