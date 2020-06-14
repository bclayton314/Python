








#User Input & Type Converting

#accepting and outputting user input
#print(input("What is your name?"))



#using the try and except blocks, use tab to indent where necessary
try:
  ans = float(input("Type a number to add: "))
  print("100 + {} = {}".format(ans, 100 + ans))
except:
  print("You did not put in a valid number!")
#without try/except print statement would not get hit if error occurs
print("The program did not break!")


#converting a variable from one data type to another
num = "9"
num = int(num)  #re-declaring num to store an integer
print(type(num))  #checking type to make sure conversion worked

#working with user input to perform calculations
ans = input("Type a number to add: ")
print(type(ans))  #default type is string, must convert
result = 100 + int(ans)
print("100 + {} = {}".format(ans, result))


#working with user input to perform calculations
ans = input("Type a number to add: ")
print(type(ans))  #default type is string, must convert
result = 100 + int(ans)
print("100 + {} = {}".format(ans, result))

ans1 = input("Type a first number to add: ")
ans2 = input("Type a second number to add: ")
result = int(ans1) + int(ans2)
print(result)

ans_make = input("What is the make of your car? ")
ans_model = input("What is the model of your car? ")
ans_year = input("What is the year of your car? ")
ans_color = input("What is the color of your car? ")

print("Your car is a {} {} {} {}".format(ans_make, ans_model, ans_year, ans_color))
