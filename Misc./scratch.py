



book = {"apple": 0.67, "milk": 1.49, "avocado": 1.49}

voted = {"tom", "mike", "dan"}

def check_voter(name):
	if voted.get(name):
		print("kick them out!")
	else:
		voted[name] = True
		print("let em vote")

check_voter("mike")






