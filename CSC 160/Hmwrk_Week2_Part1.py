

#CSC 160 Homework Week 2 Part 1
# Clayton Baker
# https://www.youtube.com/watch?v=5yhn0MFLcu8&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=13
# https://www.youtube.com/watch?v=T1j2tfZK7OI&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=14
# https://www.youtube.com/watch?v=o1dlxoHxdHU&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=15
# https://www.youtube.com/watch?v=Zs9u8TAv4_k&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=16


#Number can be stored in variables
pi = 3.14159
print(pi)

#You can do math with numbers
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

#Combining numbers and strings can be confusing
days_in_feb = 28
print(str(days_in_feb) + " days in February")

#Numbers can be stored as strings
first_num = "5"
second_num = "6"
print(first_num + second_num)

#input function always returns strings
first_num = input("Enter first number ")
second_num = input("Enter second number ")
print(first_num + second_num)

#Convert strings to numbers
first_num = input("Enter first number ")
second_num = input("Enter second number ")
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

#Using the datetime library
from datetime import datetime
current_date = datetime.now()
#the now func returns a datetime object
print("Today is: " + str(current_date))


#there are functions you can use with datetime 
#objects to manipulate dates
#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday was: " + str(yesterday))

#Use date functions to control date formatting
print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))

#Convert string to a datetime object
birthday = input("When is your birthday (dd/mm/yyyy)? ")
birthday_date = datetime.strptime(birthday, "%d/%m/%y")
print("Birthday: " + str(birthday_date))
one_day = timedelta(days=1)

birthday_eve = birthday_date - one_day
print("Day before birthday: " + str(birthday_eve))













