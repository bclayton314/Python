favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
	}

language = favorite_languages['sarah'].title()
print("Sarah's favorite language is " + str(language) + ".")


glossary = {
	'print()' : 'prints to the terminal window',
	'for' : 'starts a for loop',
	'lens()' : 'calculates the length of a string',
}

#print("The meaning of print() is " + str(glossary['print()']))

user_one = {
	'name' : 'bob',
	'age' : '22',
	'sex' : 'male',
	'job' : 'cop',
	'rank' : 'det',
}

for key, value in user_one.items():
	print("\nKey: " + str(key))
	print("Value: " + str(value))


