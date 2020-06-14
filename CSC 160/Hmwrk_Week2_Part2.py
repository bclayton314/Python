

#CSC 160 Homework Week 2 Part 2
# Clayton Baker
# https://www.youtube.com/watch?v=HQqqNBZosn8&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=17
# https://www.youtube.com/watch?v=LrRh-V-hYEc&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=18
# https://www.youtube.com/watch?v=5pPKYWqkoek&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=19
# https://www.youtube.com/watch?v=zqVmqtTLmgw&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=20

#Syntax Errors
# This code won't run at all
x = 206
if x == y:
    print('Success!!')
#error above requires a colon at the end of the if statement

#Runtime Errors
# This code will fail when run
x = 42
y = 0
print(x / y)
#error from division by zero

#Catching runtime errors
try:
    print(x/y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')    

#try/except/finally - not used to find bugs,
#debugging, not error handling, don't have to catch all errors

#Logic Errors
x = 206
y = 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))
#code won't run because x > y

#Error in code
#Seek out line numbers
#Reread your code
#Check documentation
#Take a break
#Ask for help

x = 42
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()


#Your code needs the ability to take different 
#actions based on different conditions
if price >= 1.00:
    tax = .07
    print(tax)

#Symbols & Operations: >, <, >=, <=, ==, !=

#Using "else" to add default action
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)
#INDENTATION MATTERS!!!

#Be careful comparing strings, CASES MATTER
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')
#Conditions allow our code to react to different situations

#DEMO VIDEO
price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is : ' + str(tax))


country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')



