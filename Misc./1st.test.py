


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

num = range(11)

#value = []
#for squares in num:
	#value.append(squares**2)
#print(value)

#squares = [square**2 for square in range(0, 11)]
#print(squares)

#nums_20 = [nums for nums in range(1, 21)]
#print(nums_20)

#million = [(i + 1) for i in range(1001)]
#print(million)

#odd_num = [i for i in range(1, 21, 2)]
#print(odd_num)

#three_num = [i for i in range(3, 31, 3)]
#print(three_num)

#cube_num = [(i**3) for i in range(1, 11)]
#print(cube_num)

#print("the first three items in the list are " + str(#lst1[:3]))

#print("The last three items are " + str(lst1[-3:]))

#friend_pizza = ["cheese", "meat", "plain"]
#my_pizza = ["anchovie", "sausage", "provolone"]



def age(age):
	if age < 4:
		price = 10
	elif age < 18:
		price = 25
	else:
		price = 40
	return price

#print(age(22))


def age_life(age):
	if age < 2:
		stage = 'baby'
	elif age >= 2 and age < 4:
		stage = 'toddler'
	elif age >= 4 and age < 13:
		stage = 'kid'
	elif age >= 13 and age < 20:
		stage = 'teenager'
	elif age >= 20 and age < 65:
		stage = 'adult'
	elif age >= 65:
		stage = 'elder'
	return 'This person is ' + str(stage)

#print(age_life(5))












current_users = ['bob', 'jack', 'gwen', 'jil', 'stacy']

current_users2 = ['Bob', 'Jack', 'Gwen', 'Jill', 'Stacy']


new_users = ['tom', 'ed', 'jack', 'jil', 'john']


#for new_user in new_users:
	#if new_user in current_users:
		#print(str(new_user) + ", u need a new name!")
	#elif new_user in current_users2:
		#print("Case matters")
	#else:
		#print("Welcome!")


lst1 = list(range(1, 10))
print(lst1)

for num in lst1:
	if num == 1:
		print(str(num) + "st")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")
	

