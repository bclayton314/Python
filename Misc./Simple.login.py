


#Global Variables: Username / Password
#user_name == "clay314"
#password == "12345!"

correct = True
while correct:
  u_name = input("Username: ")
  if u_name == "Clay314":
    print("Welcome Back")
    break
  else:
    print("Incorrect. Re-enter Username")

while correct:
  pwd = input("Password: ")
  if pwd == "12345!":
    print("Correct!")
    break
  else:
    print("Error! Re-enter Password")