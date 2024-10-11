# a = 2
# b = 3
# h = 1
# print(f'The area is {(a+b)/2*h}')
import math

# str1 = str.format('This is the number %s: %d', ('two', 2))
# str2 = f'This is the number {'one'}": {1}'

# r = float(input())
# area = str.format('The area of the circle is %.3f', math.pi*r**2)
# print(area)

# wage = float(input())
# hours = float(input())
# print(f'Total payment is {round(wage*hours, 1)}')

# def convertDegrees (inp, unit):
#     try:
#         float(inp)
#     except:
#         print('enter a num')
#         exit(0)
#     if unit == 'C':
#         return float(inp) *1.8 + 32
#     elif unit == 'F':
#         return float(inp - 32) / 1.8
#     print('invalid format') 


# print(convertDegrees(0, 'C'))
# print(convertDegrees(32, 'F'))
# print(convertDegrees('51hello', 'F'))

# fn = input('First name ')
# ln = input('Last name ')
# age = input('Age ')
# country = input('Country ')

# print(f'My name is {fn} {ln}. I\'m {age} years old. I\'m born in {country.capitalize()}')

fn = input('First name: ')
ln = input('Last name: ')
email = input('e-mail: ')
phone_num = input('phone num: ')

if('@' not in email):
    print('invalid email')

for char in phone_num:
    try:
        int(char)
    except:
        print('phone num should only contain digits')
        exit(0)
        

    
print(f'First name: {fn}')
print('\n========\n')
print(f'Last name: {ln}')
print('\n========\n')
print(f'e-mail: {email}')
print('\n========\n')
print(f'phone: {phone_num}')