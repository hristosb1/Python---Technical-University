# Напишете програма , в която потребителя въвежда цяло число (да се валидира)
# а програмата формира два кортежа , състоящи се от цифрите, влизащи в това число.
# Единият с цифрите на числото в прав ред и втори, в който цифрите цифрите са в обратен ред.
# Да се хванат грешките на компилатора (OutofRange и подобни).
from math import floor
from random import random, randint


def num_to_tuples(num):
    try:
        num = int(num)
    except:
        exit('Enter an integer')
    digits = []
    while num != 0:
        digits.append(num % 10)
        num /= 10
    return {
        'normal_tuple': tuple(digits),
        'reversed_tuple': tuple(reversed(digits))
    }


# Напишете програма , в която се създава числов списък. Той се запълва
# със случайни числа. След това между всяка двойка елементи от
# този списък се вмъква нов, равен на сумата от стoйностите на съседните елементи.

def random_list_el_sum(nums: list):
    # sum neighbour elements and put the sum between them
    i = 0
    while i < (len(nums) - 1):
        s = nums[i] + nums[i + 1]
        nums.insert(i + 1, s)
        i += 2

l = []
for i in range(5):
    l.append(randint(1,10))


# Напишете програма, в която потребителя въвежда текст (валидирай)
# и на негова база се създава речник. За ключове на речника служат символите
# от текста, а стойността на елементите се определя от броя на
# съответните символи в текста.

def text_to_dict(text):
    text = str(text)
    if ' ' in text: exit('Invalid format - enter only text')
    d = dict()
    for c in text:
        if c not in d.keys():
            d[c] = 1
        else:
            d[c] += 1
    return d


# Напишете програма, в която потребителя въвежда цяло число. От него се създава
# списък състоящ се от числата от 1 до това число. Въз основа на този списък се създава речник,
# в който елементите
# на списъка служат за ключове на елементите в речника, а стойностите на тези
# елементи в речника са елементите на списъка но в обратен ред.

def num_to_dict(num):
    try:
        num = int(num)
    except:
        exit('Please enter a number')

    nums = []
    for i in range(num):
        nums.append(i + 1)

    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = nums[::-1][i]

    return d

#Напишете софтуер за ресторанти който ще управлява поръчките. Софтуера трябва да може да :
# Събира поръчки
# Складира поръчките в лист. Формат на поръчките : <НомерНаПоръчка> : <ИмеНаКлиент> : <КаквоЕПоръчал>
# Да принтира колко уникални поръчки са направени до момента
# Да връща имена на клиенти , направили конкретна поръчка
# Когато се връща името на клиентите, списъкът да бъде подреден по азбучен ред.

class RestaurantManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_unique_orders(self):
        return len(set(self.orders))

    def get_clients(self):
        clients = []
        for order in self.orders:
            clients.append(order.split(':')[1])
        return sorted(set(clients))
