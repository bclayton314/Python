

#CSC 160 Homework Week 1 Part 2
# Clayton Baker
# https://www.youtube.com/watch?v=tSebLz1hNpA&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=9
# https://www.youtube.com/watch?v=zv3cVJHCqXA&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=10
# https://www.youtube.com/watch?v=bQQqxysLIGE&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=11
# https://www.youtube.com/watch?v=E850-MF22P0&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=12


#Strings can be stored in variables
first_name = 'Christopher'
print(first_name)
last_name = "Harrison"
print(first_name + last_name)
print('Hello' + first_name + " " + last_name)

#Use Functions to modify strings
sentence = "The dog is Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

#Format strings wiith functions
first_name = input("What is your last name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name.capitalize() + " " last_name.capitalize())
print("Hello, " + first_name + " " last_name)

#You can combine strings with +
first_name = "Christopher"
last_name = "Harrison"
print(first_name + last_name)
print("Hello " + first_name + " " + last_name)

output = "Hello, " + first_name + " " + last_name
output = "Hello, {} {}".format(first_name, last_name)
output = "Hello, {0} {1}".format(first_name, last_name)
output = f"Hello, {first_name} {last_name}"