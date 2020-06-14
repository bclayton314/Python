

#Programming Python

"""def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high)
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 5, 7, 9]"""

#Python Projects - Binary Search

#setting up imports and generating a list of random numbers to work with
import random
nums = [random.randint(0, 20) for i in range(10)]	#create a list of ten numbers betweeen 0 and 20

#step 1: sort the list
def binarySearch(aList, num):
	aList.sort()
	#step 6: setup a loop to repeat steps 2 through 6 until list is empty
	while aList:
		mid = len(aList) // 2
		if aList[mid] == num:
			return True
		elif aList[mid] > num:
			aList = aList[:mid]
		elif aList[mid] < num:
			aList = aList[mid + 1 :]
	return False

print(sorted(nums))
print(binarySearch(nums, 10))

"""#step 2: find the middle index
	mid = len(aList) // 2	#two slashes means floor division - round down to the nearest whole num

	#step 3: check the value at middle index, if it is equal to num return True
	if aList[mid] == num:
		return True
	
	#step 4: check if value is greater, if so, cut off right half of list using slicing
	elif aList[mid] > num:
		aList = aList[:mid]
	
	#step 5: check if value is less, if so, cut off left half of list using slicing
	elif aList[mid] < num:
		aList = aList[mid + 1 :]

	#step 7: return False, if it makes it to this line it means the list was empty and num wasn't fouund
	return False"""





