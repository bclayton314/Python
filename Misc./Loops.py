
#C.ACAD:
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))


#MINE:
def divisible_by_ten(nums):
  nums_ten = []
  for num in nums:
    if (num % 10 == 0):
      nums_ten.append(num)
  print(len(nums_ten))
    

#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))



#MINE:
#Write your function here

def add_greetings(names):
  hello = []
  for name in names:
    hello.append("Hello, " + name)
  return hello

  

#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))


#MINE:
#Write your function here

def delete_starting_evens(lst):
  for lst2 in lst:
    if len(lst) > 1:
      continue
    if lst2[0] % 2 == 0:
        del(lst2[0])
    else:
        return lst2


#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

#Code Acad
#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))


#Code Acad
#Write your function here
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))


#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
#print(over_nine_thousand([8000, 900, 120, 5000]))


#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
#print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


#test why this didn't work
lst1 = list(range(0, 21))

def even_num(lst1):
	evenlst = []
	for i in lst1:
		if lst1[i] % 2 == 0:
			evenlst.append(i)
		return evenlst

print(even_num(lst1))





