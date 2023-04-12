# ----------------------------------------------
#  math operations
# import math
# pi = 3.14
# x = 3
# y = 12
# z= 5
#
# print(pow(2, 5)) # üssünü alma
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(-pi))
# print(math.sqrt(16))
# print(max(x,y,z))

# ----------------------------------------------
#  String Slicing
# slicing = create a substring by extracting elements from another string
# indexing[] or slice ))
# [start: stop: step]

# sentence = "Hello there obi wan"
# first_word = sentence[0:5] # first index is inclusive and the second is exclusive
# first_word = sentence[:5] # first index is inclusive and the second is exclusive
# # these two are the same
# second_word = sentence[6:11]
# write_third_and_fourth_word = sentence[11:] # include everything after 11. index. including 11. index
# funky_first_word = sentence[0:5:2] # the default continuing was 1 step at a time now it's 2 step
# funky_sentence = sentence[::2]
# print(first_word, second_word, write_third_and_fourth_word)
# print(funky_sentence)
# #  if you want to reverse a string you can do it like this
# print(sentence[::-1])

# ---------------------

# website1 = "http://google.com"
# website2 = "https:/youtube.com"

# slice = slice() # in here we can add up to 3 values (start, stop, step)

# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

# ---------------------
#  for loop

# for i in "this is the way":
#     print(i)

# import  time
# for seconds in range(5, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("happy new year.")

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="'") # this will prevent going o the next line after iteration

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
#

# phone_number = "123-456-789"
#
# for digit in phone_number:
#     if digit == "-":
#         continue
#     print(digit, end="")
# print("")
#
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(f"{i}-", end="")

# ---------------------------------------
# LISTs
# list = used to store multiple items in a single variable

# food = ["pizza"]  # this is a list now
# groups = ["radiohead", "black sabbath", "jeff buckley", "iron maiden"]
# # important concept with list is that you can always update and change the elements
# # found within a list later on in a program after you declare one
# print(groups)
# print(groups[-1])
#
# groups[-1] = "smashing pumpkins"
# print(groups[-1])
# print("--------------")
# # for items in groups:
# #     print(items)
#
# groups.append("led zeppelin")
# print(groups)
# groups.remove("radiohead")
# print(groups)
# groups.pop() # this will remove the last element
# print(groups)
# groups.insert(3, "led zeppelin")
# print(groups)
# groups.sort()
# print(groups)
# groups.clear()
# print(groups)

# ---------------------------------------
# 2D LISTs

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hot dogs"]
dessert = ["cake", "ice cream"]

food = [dinner, dessert, drinks]
print(food)
print(food[0][0])

# ---------------------------------------
# TUPLES
# tuple = collection which is ordered and unchangeable
# used to group together related data
# tupples are more performent than lists because it's immutable therefore have a smaller memory footprint


student = "duncan trussell", 41, "Male"

print(student.count("Male"))
print(student.count(41))

my_tupple = 1, 2, 3

a, b, c = student
print(a, b, c)


def my_function():
    return "duncan trussell", 41, "Male"


result = my_function()
print(type(result))

# Usage: Lists are generally used for collections of data
# that may need to be modified or extended, such as the elements
# in a shopping cart. Tuples are often used for collections of
# data that should not be modified, such as the coordinates of
# a point in space.

# ---------------------------------------
# SET
# set = collection which is unordered, unindexed. No duplicate values

my_set = {1, 2, 3}
print(my_set)
my_other_set = set([4, 5, 6])
print(f"my_other_set: {my_other_set}")

my_set.add(4)
my_set.update([5, 6, 7])
print(f"my_set: {my_set}")

my_set.remove(4)
my_set.discard(8)  # if there is 8 it will remove it if there is not it will do nothing
print(f"my_set: {my_set}")

print(f"my_set.union: {my_set.union(my_other_set)}")
print(f"my_set.intersection: {my_set.intersection(my_other_set)}")

# my_set.difference(my_other_set)  # returns a new set with elements that are in my_set but not in my_other_set
# my_set.symmetric_difference(my_other_set)  # returns a new set with elements that are in only one of the sets
# Membership testing
print(3 in my_set)

# ---------------------------------------
# DICTIONARY
# dictionary is a collection of key-value pairs, where each key is associated with a value.
# sometimes called "maps" or "hash tables".
# A changeable, unordered collection of unique key: value pairs
# Fast because they use hashing, allow us to access a value quickly

# Creating a dictionary
my_dict = {"apple": 2, "banana": 3, "orange": 4}

# Accessing values in a dictionary
print(my_dict["apple"])  # prints 2

# Adding or updating key-value pairs in a dictionary
my_dict["pear"] = 5
my_dict.update({"banana": 6})

# Removing key-value pairs from a dictionary
del my_dict["orange"]
my_dict.pop("banana")

# Looping over keys, values, or key-value pairs in a dictionary
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)

# Checking for membership
print("pear" in my_dict)  # prints True
print("grape" in my_dict)  # prints False

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(capitals.keys())

# ---------------------------------------
# INDEXING

# index operator [] = gives access to a sequence's element (str, list, tuples)

one_liner = "this is the way"

if one_liner[0].islower():
    one_liner = one_liner[0].upper() + one_liner[1:]

print(one_liner)


# ---------------------------------------
# Keyword arguments

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="Code", middle="Dude", first="Bro")

# ---------------------------------------
# Nested function calls

# print(round(abs(float(input("Enter a whole positive number: ")))))

# ---------------------------------------
# Variable scope
# scope = The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created

name = "Bro"  # global scope (available inside & outside functions)


def display_name():
    name = "Code"
    print(name)


# local scope (available only inside this function)
display_name()
print(name)


# ---------------------------------------
# ARGS
# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments


def add(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 0
    for arg in stuff:
        sum += arg
    return sum


print(add(1, 2, 3, 4, 5, 6))

hey = ["hello", "this", "is", "me"]
print(len(hey))


# ---------------------------------------
# kwargs
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello" + kwargs['first'] + " " + kwargs['last'])


hello(first="Bro", middle="Dude", last="Code")


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_function(name="Alice", age=30, city="New York")
