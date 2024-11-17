#Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 26, 24, 25, 24]

#Find the length of the set it_companies
print('Length of it_companies is:', len(it_companies))

#2 Add 'Twitter' tp it_companies
it_companies.add('Twitter')
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update({'Forvia', 'Faurecia', 'Hella'})
print(it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

#5 What is the Difference between remove and discard?
print('The difference between remove and discard is that remove raises a key error if it is not present in the set')