


# letter1 = ['a', 'c', 'e', 'g']
# letter2 = ['b', 'd', 'f', 'h']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# letter = input("Please enter a letter for the board location: ")
# number = int(input("Please enter a number for the board location: "))

# if letter in letter1 and (number%2 != 0):
#   print("Black")
# elif letter in letter1 and (number%2 == 0):
#   print("White")
# elif letter in letter2 and (number%2 != 0):
#   print("White")
# elif letter in letter2 and (number%2 == 0):
#   print("Black")



# freq = input("Please enter the level of electromagnetic radiation(Please enter value in scientific notation, Ex. 1.23e7): ")

# if freq < 3e9:
#     print("Radio waves")
# elif freq >= 3e9 and freq < 3e12:
#     print("Microwaves")
# elif freq >= 3e12 and freq < 4.3e14:
#     print("Infrared light")
# elif freq >= 4.3e14 and freq < 7.5e14:
#     print("Visible light")
# elif freq >= 7.5e14 and freq < 3e17:
#     print("Ultraviolet light")
# elif freq >= 3e17 and freq < 3e19:
#     print("X-Rays")
# elif freq >= 3e19:
#     print("Gamma rays")




letter = 0
gpa = 0
counter = 0
while (letter != ""):
    letter = input("Please enter a letter: ")
    if letter == "A+" or letter == "A":
        gpa += 4.0
        counter += 1
    elif letter == "A-":
        gpa += 3.7
        counter += 1
    elif letter == "B+":
        gpa += 3.3
        counter += 1
    elif letter == "B":
        gpa += 3.0
        counter += 1    
    elif letter == "B-":
        gpa += 2.7
        counter += 1
    elif letter == "C+":
        gpa += 2.3
        counter += 1
    elif letter == "C":
        gpa += 2.0
        counter += 1
    elif letter == "C-":
        gpa += 1.7
        counter += 1
    elif letter == "D+":
        gpa += 1.3
        counter += 1
    elif letter == "D":
        gpa += 1.0
        counter += 1
    elif letter == "F":
        gpa += 0
        counter += 1

print("Your GPA is: "(gpa)/(counter))

