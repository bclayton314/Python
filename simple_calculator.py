



#step 1: ask user for calculation to be performed

operation = input("Would you like to add/subtract/multiply/divide? ").lower()
#print("You chose {}.".format(operation))

#step 2: ask for numbers, alert order matters for subtracting and dividing
if operation == "subtract" or operation == "divide":
  print("You chose {}.".format(operation))
  print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
print("First Number: {}".format(num1))
print("Second Number: {}".format(num2))

#step 3: setup try/except for mathematical operation
try:
  num1, num2 = float(num1), float(num2)
  if operation == "add":
    result = num1 + num2
    print("{} + {} = {}".format(num1, num2, result))
  elif operation == "subtract":
    result = num1 - num2
    print("{} - {} = {}".format(num1, num2, result))
  elif operation == "multiply":
    result = num1 * num2
    print("{} * {} = {}".format(num1, num2, result))
  elif operation == "divide":
    result = num1 / num2
    print("{} / {} = {}".format(num1, num2, result))
  else:
    print("Sorry, but '{}' is not an option.".format(operation))
except:
  print("Error: Improper numbers used. Please try again.")