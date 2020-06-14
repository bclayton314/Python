


#CSC 160 Homework Week 4
# Clayton Baker
# https://www.youtube.com/watch?v=beA8IsY3mQs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=25
# https://www.youtube.com/watch?v=4PaSlXNjawM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=26
# https://www.youtube.com/watch?v=LrOAl8vUFHY&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=27
# https://www.youtube.com/watch?v=rAvD-6MpTw4&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=28

#Collections - Vid.1
#Lists are collections of items
names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # Collections are ZERO-indexed

#Arrays are also collections of items
from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

#Common operations
names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)

#Retrieving ranges
names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
# Start and end index
print(names)
print(presenters)

#Collections Code - Vid.2
#Dictionaries
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

christopher = {}
christopher['first'] = 'Christopher'
christopher['last'] = 'Harrison'

susan = {}
susan['first'] = 'Susan'
susan['last'] = 'Harrison'

people = []
people.append(christopher)
people.append(susan)
people.append({
    'first': 'Bill', 'last': 'Gates'
})

#Loops - Vid.3
#Loop through a collection
for name in ['Christopher', 'Susan']:
    print(name)

#Looping a number of times
for index in range(0, 2):
    print(index)     

#Looping with a condition
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    # Change the condition!!
    index = index + 1

#Loops Code Vid.4

people = ['Christopher', 'Susan']

for name in people:
    print(name)

index = 0
while index < len(people):
    print(people[index])
    index = index + 1
print()
