# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
import math

print('Thirty' + ' ' + 'Days' + ' ' + '0f' + 'Python')

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
challenge = ['Codding', 'For', 'All']
print(challenge[0] + ' ' + challenge[1] + ' ' + challenge[2])

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Codding For All'

# 4. Print the variable Company using print
print(company)

# 5. Print the length of the company string using len() adn print
print(len(company))

# 6. Change all the characters to uppercase letters using upper()
print(company.upper())

# 7. Change all Characters to lowercase letters using lower()
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the vale of the string
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first world of Codding For All string.
first_word = company.split()[0]
print(first_word)

#10. Check if Codding For All string contains a word Codding using the method index, find or other methods.
print(company.index('Codding'))
print(company.rindex('Codding'))
print(company.find('Codding'))
print(company.rfind('Codding'))
print('Codding' in company)
print(company.count('Codding'))

# 11. Replace the word codding in the string Codding For All to Python
new_string = company.replace('codding', 'Python')
print(new_string)

# 12. Change Python for Everyone to Python for all using replace method or other methods
new_string = 'Python for Everyone'
print(new_string.replace('Evetyone', 'All'))

# 13. split the string Codding For All using space as the separator
print(company.split(' '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
new_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new_string.split(', '))

# 15. What is the character at index 0 in the string Codding For All.
print(company[0])

# 16. What is the last index of the string Codding For All
print(company.rfind(company[-1]))

# 17. What Character is at index 10 in Codding for All string
print(company[10])

# 18. Create an acronym or an abbreviation for Python For Everyone
company = 'Python for Everyone'
new_strings = company.split()
print(''.join(new_string[0] for new_string in new_strings))

# 19. Create an acronym or an abbreviation for Codding for Everyone
company = 'Codding for Everyone'
print(''.join(new_string[0] for new_string in company.split()))

# 20. Use index to determine the position of the first occurrence of C in Codding For All
company = 'Codding For All'
print(company.index('C'))

# 21. Use index to determine the position fo the first occurrence F in Codding For All
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Codding For All People
company = 'Codding For All People'
print(company.rfind('l'))

# 23. Use index to find the position of the first occurrence of the word 'because' in the following sentence
#'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24. use rindex to find the position of the last occurrence of the word because in the following sentence:
#'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence
#'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

# 26. Find the position of the first occurrence of the word 'because' in the following sentence
#'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 27. Slice out the phrase 'because because because' in the following sentence
#'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

# 28. Does Codding for All starts with substring Codding?
company = 'Codding for All'
print(company.startswith('Codding'))

# 29. Does Codding for All end with substring 'codding'
print(company.endswith('codding'))

# 30. ' Codding For All ' remove the left and right trailing spaces in the given strng
company = ' Codding For All '
print(company.removeprefix(' ').removesuffix(' '))

# 31. Which of the following variables returns true when we use the method isidentifier().
#30DaysOfPython
#thirty_days_of_python
print('30DaysOfPython returns ->','30DaysOfPython'.isidentifier(), '-> because a identifier can not start with a nuber or contain any spaces')
print('thirty_days_of_python returns ->','thirty_days_of_python'.isidentifier(), '-> because it respects all rules for an identifier')

# 32. The following list contains the names of some of Python libraries. Join the list with a has with spae string
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_Libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_Libraries))

# 33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge\nI just wonder what is next.')

# 34. Use a tab escape sequence to write the following lines
print('Name\t\tAge\t\tCountry\t\tCity\nAlexandru\t69\t\tRomania\t\tCraiova')

# 35. Use the string formatting method to display the following
radius = 10
area = math.pi * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36 make the following using string formatting methods
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
