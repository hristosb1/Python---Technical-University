# a = input()
# b = a[::-1]
# if a == b:
#     print("a is a palindrome")
# else:
#     print("a isn't a palindrome")
# from numpy import random, floor
#
# random_num = floor(random.random() * 10)
# guess_count = 7
# guessed_nums = set()
# try:
#     while guess_count > 0:
#         chance = (guess_count / 10 - len(guessed_nums))*100
#         print(f'Your chance to guess in {chance}%')
#         guess = int(input('Guess a number: '))
#         if guess == random_num:
#             print('Correct guess')
#             break
#
#         elif guess in guessed_nums:
#             print('You already tried that')
#             continue
#
#         else:
#             guessed_nums.add(guess)
#             guess_count -= 1
# except:
#     print('Invalid input, enter a number')
#     exit(0)
from mathpy.numtheory import isprime

# #1
# nums = []
# for i in range(int(input('enter n '))):
#     nums.append(input("enter a num "))
#
# print(f'The max num is {max(nums)}')

#2
# s = 0
# for i in range(int(input('enter n' ))):
#     s+= input('enter a num ')
#
# print(f'The sum is {s}')

#3
n = int(input('enter n '))
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

# #4
# user_in = int(input('enter a num'))
# print(f'N is prime - {isprime(n)}')