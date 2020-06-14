


#CSC 160 Homework Week 2 Part 1
# Clayton Baker
# https://www.youtube.com/watch?v=oYaGJBMoXok&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=21
# https://www.youtube.com/watch?v=J9luo4cODzM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=22
# https://www.youtube.com/watch?v=IBOHc87yFYw&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=23
# https://www.youtube.com/watch?v=Iui6K2STtbA&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=24


#Handling multiple conditions

#If only one of the conditions will ever occur
#you can use a single if statement with elif
#Or use elif for multiple if statements
#Using 'OR' can combine conditions with same action
#Can also use 'IN' to check multiple possible values
province = input("What is your province? ")
tax = 0

if province in 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

#Can also nest if statements
country = input("What is your country? ")

if country == 'Canada':
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
else:
    tax = 0.0


#Complex Condition Checks
#Sometimes you can combine conditions
#with "AND" instead of nesting if statements

#Code for GPA with "IF" statements

if gpa >= .85:
    if lowest_gpa >= .70:
        print('Well done')

if gpa >= .85 and lowest_grade >= .70:
    print('Well done')

#to remember results of a condition check later,
#use Boolean variables as flags

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
#Somewhere later in your code
if honour_roll:
    print('Well done!')

#Combining operators allows you to handle 
#complex business rules in your code but must be tested 
#very carefully to avoid introducing errors

# Complex condition checks code
# A student makes honour roll if their average is >= 85
# and their lowest grade is not below 75

#Need to specify float because of the decimal
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))
lowest_grade = float(lowest_grade)


if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll')

#Can also use an "AND" instead of a nested if statement
if gpa >= .85 and lowest_grade >= .70:
        print('You made the honour roll')

#Use Boolean to check
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code if you need to check if students
#are on honour roll, just use the Boolean variable
if honour_roll:
    print('You made honour roll')