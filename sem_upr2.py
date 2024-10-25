# 1

# n = int(input())
#
# isDivBy3 = n % 3 == 0
# isDivBy5 = n % 5 == 0
#
# if isDivBy3 and isDivBy5:
#     print('The number is divisible by both 3 and 5')
# elif isDivBy3:
#     print('The number is divisible by 3')
# elif isDivBy5:
#     print('The number is divisible by 5')
# else:
#     print('The number is not divisible by 3 or 5')

# 2

# n = int(input())
# if n <= 0:
#     exit('Negative num')
#
# s = 0
# p = 1
# if n == 1: p = 0
#
# for i in range(1, n+1):
#     if i % 2 == 0:
#         p*=i
#     else:
#         s += i
#
#
# print(f'sum {s}')
# print(f'product {p}')

# 3

row_count = int(input())
sym = input()

for i in reversed(range(row_count)):
    for j in range(i+1):
        print(sym, end=' ')
    print()

print()
for i in reversed(range(row_count)):
    j_end = i+1
    for j in range(j_end):
        if j == 0 or j == j_end-1 or i == row_count-1:
            print(sym, end=' ')
        else:
            print(' ', end=' ')
    print()

# 4

start = int(input())
end = int(input())


def is_prime(num: int):
    if num == 0 or num == 1:
        return False
    for j in range(2, num // 2 + 1):
        if num % j == 0: return False

    return True


prime_nums = []
s = 0
for i in range(start, end + 1):
    if is_prime(i):
        prime_nums.append(i)
        s += i

print(f'Простите числа в диапазона {start} - {end} са {"".join(f"{num}, " for num in prime_nums)}')
print(f'Минималното просто число е {min(prime_nums)}')
print(f'Максималното просто число е {max(prime_nums)}')
avg = round(s / len(prime_nums), 2)
print(f'Средното аритметично на простите числа е {avg}')

# bonus

n = int(input())
s = 0

s += n % 10
n//= 10
s += n % 10
n//= 10
s += n % 10
n//= 10
s += n % 10

print(s)