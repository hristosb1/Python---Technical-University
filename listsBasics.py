# List methods:

# append(item) - inserts an item at the end of the list
a = [1,2,3]
a.append(1)

# extend(iterable) - extends the list with the items of an iterable
a.extend([1,2])
a.extend((3,4))
a.extend(range(5,8))

# insert(index, item) - inserts an item at a given index
a.insert(0, "new element")

#! remove(item) - removes the fist occurrence of the element

# index(item, start?, end?) - returns the index of the first occurrence of the item,
# opt limit search
a.index(1,0,3)

# count(item) - returns the count of that item in the list
a.count(1)

#sort(key, reverse)
# a.sort() #ASC
# a.sort(reverse=True) #DESC
b = ['aaa','bbb','c']
b.sort(key=len)#sort by the lengths of the strings

# sorted(iterable, key, reverse) - like .sort, but returns a new reference
c = sorted(b, key=len, reverse=True)

# reverse() - reverses the elements of the list
a.reverse()

# copy() - creates a shallow copy of the list
d = a.copy()

# in - checks if the list includes an element
oneInA = 1 in a

#Problem
#You are given a list of dictionaries representing products in a store.
# Each product has a name, price, and a quantity_in_stock.

# Remove any product that is out of stock (quantity_in_stock is 0).
# Sort the remaining products by price in ascending order.
# Insert a new product in the sorted list while keeping the list sorted.
# Find the position of a specific product by its name.
# Create a string that lists all product names, separated by commas.

products = [
    {"name": "laptop", "price": 1000, "quantity_in_stock": 5},
    {"name": "phone", "price": 500, "quantity_in_stock": 0},
    {"name": "tablet", "price": 300, "quantity_in_stock": 2},
    {"name": "monitor", "price": 150, "quantity_in_stock": 10},
    {"name": "keyboard", "price": 20, "quantity_in_stock": 0},
]

# Remove any product that is out of stock (quantity_in_stock is 0).
products = [product for product in products if product["quantity_in_stock"] > 0]
products.sort(key=lambda product: product['price'])