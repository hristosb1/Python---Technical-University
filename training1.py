### 1.10.2024 https://www.codewars.com/


# def bool_to_word(boolean):
#     return 'Yes' if boolean else 'No'
# def string_to_number(s):
#     return float(s) if int(s) / 1 != 0 else int(s)
# def boolean_to_string(b):
#     return 'True' if b else 'False'
# def find_smallest_int(arr):
#     smallest = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#     return smallest
## return min(arr) or arr.sort() return arr[0]
# def find_needle(haystack):
#     for i in range(len(haystack)):
#         if haystack[i] == 'needle':
#             return f'found the needle at position {i}'
## arr.index() returns the index, throws ValueError if it doesn't exist
# def opposite(number):
#     return -number
# def count_positives_sum_negatives(arr: list):
#     p, n = 0,0
#     if not arr:
#         return []
#     for i in arr:
#         if i > 0:
#             p += 1
#         else:
#             n += i
#     return [p,n]
# def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int):
#     return (distance_to_pump - mpg * fuel_left) <= 0
# def sum_array(arr: list):
#     return sum(arr)
# def make_negative(n: int | float):
#     return -abs(n)
# def summation(num):
#     s = 0
#     for i in range(1, num+1):
#         s += i
#     return s
## return sum(range(1,num+1))
# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'
# def count_sheeps(sheep: list):
#     return sheep.count(True)
