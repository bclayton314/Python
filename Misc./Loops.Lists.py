
#C.ACAD:
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


#MINE:
def divisible_by_ten(nums):
  nums_ten = []
  for num in nums:
    if (num % 10 == 0):
      nums_ten.append(num)
  print(len(nums_ten))
    

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))



#MINE:
#Write your function here

def add_greetings(names):
  hello = []
  for name in names:
    hello.append("Hello, " + name)
  return hello

  

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


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
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Code Acad
#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))