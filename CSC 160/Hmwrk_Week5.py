

#CSC 160 Homework Week 5
# Clayton Baker
# https://www.youtube.com/watch?v=nrCAxXfRU28&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=29
# https://www.youtube.com/watch?v=C9ZEGqGHXms&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=30
# https://www.youtube.com/watch?v=sKW-zdYZNX4&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=31
# https://www.youtube.com/watch?v=LtKAXFRtxhQ&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=32
# https://www.youtube.com/watch?v=Uei2ILcxuPs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=33


# Functions
# Ok to copy and paste code
import datetime
# print timestamps to see how long sectiond
# take to run

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()

#Use functions instead of repeating code

import datetime
# Print the current time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time('printed first name')

for x in range(0,10):
    print(x)
print_time('completed for loop')

#This function will take a name and return the
# first letter of the name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someone's name and return the initials with function
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' + get_initial(first_name) + get_initial(middle_name) + get_initial(last_name))

#Returns first initial of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someones name and return the initials w/o and with function
first_name = input('Enter your first name: ')
#first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
#middle_name_initial = middle_name[0:1]
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
#last_name_initial = last_name[0:1]
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)

#Functions reduce rework and bugs


#We already learned functions which accept a parameter
#and return values
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

print('Your initial is: ' + first_name_initial)

#Functions can accept multiple parameters
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)
print('Your initial is: ' + first_name_initial)

#Can set default value for parameters
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print('Your initial is: ' + first_name_initial)

#Can also assign values when you call the function
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name=True, name=first_name)


#Using named notation when calling functions makes your code more readable
def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    #Imagine code here that logs our error to a database or file

first_number = 10
second_number = 5
if first_name > second_number:
    error_logger(45, 1, True,
     'Second number greater than first', 'my_math_method')

#Creating a module
# helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)

#Importing a module
# import module as namespace
import helpers 
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')

# Installing packages
# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama


