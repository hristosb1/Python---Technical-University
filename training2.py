# Problem 1: Filter Even Numbers
# You are given a list of integers. Filter out all the even numbers from the list.

#Solution for problem 1:
numbers1 = [3, 4, 7, 10, 14, 23, 34, 50]
numbers1 = [num for num in numbers1 if num % 2 == 0]

# Given a list of integers, create a new list that contains
# the squares of only the odd numbers from the original list.

#Solution for problem 2:
numbers2 = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [num**2 for num in numbers2 if num %2 != 0]


# Given a list with some duplicate values, remove the
# duplicates and return the list sorted in ascending order.

numbers3 = [5, 3, 8, 3, 9, 1, 5, 7, 9]
numbers3 = list(set(numbers3))
numbers3.sort()

# Given a list of lists, flatten the nested lists into a single list.
list_of_lists = [[1, 2], [3, 4], [5, 6, 7], [8]]
list_of_lists = [item for sublist in list_of_lists for item in sublist]

# You are given a list of names.
# Filter out all the names that are shorter than 5 characters.
names1 = ["Jack", "Sophia", "Tom", "Isabella", "Chris"]
names1 = [name for name in names1 if len(name) > 5]

# You are given two lists of numbers.
# Find the common elements (intersection) between the two lists.
arr1 = [10, 20, 30, 40, 50]
arr2 = [20, 40, 60, 80]
intersection = [item for item in arr1 if item in arr2]

# Reverse Strings in a List
# Given a list of strings, return a new list where each string is reversed.

words = ["hello", "world", "python", "is", "fun"]
words = [word[::-1] for word in words]

# You are given a list of integers.
# Replace all negative numbers with 0, and
# keep the rest of the numbers unchanged.
nums = [-5, 3, -1, 8, -2, 0]
nums = [max(0, num) for num in nums]

# You are given a list of words. Find the word with the maximum length.
arr = ["cat", "elephant", "giraffe", "hippopotamus", "lion"]
longestWord = max(arr, key=len)