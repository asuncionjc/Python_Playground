# INTEGER NUMBERS

first_integer = 7
print(first_integer)

# FLOAT NUMBERS
# To define a float number two different notations can be used.
# The first one:

first_float = 8.0
print(first_float)

# The second form:

second_float = float(8)
print(second_float)

# STRINGS

# Single or double quotes can be used to denote a string:

first_string = "hello"
second_string = 'hello'

print(first_string)
print(second_string)

# However if double quotes are used to denote a string, then it is easier to include apostrophes

third_string = "What's a sunny day =)"
print(third_string)

# SIMPLE OPERATIONS ON NUMBERS AND STRINGS

# Integer numbers
one = 1
two = 2
three = one + two
print(three)

# Float numbers

four = 4.0
five = float(5)
nine = four + five
print(nine)

# Strings

my_name = "My name's"
space = " "
asun = 'Asun'

say_your_name = my_name + space + asun
print(say_your_name)

# SIMULTANEOUS ASSIGNMENTS

# It is not necessary to write one variable per line. For instance:

a, b = "goodbye", 3
print(a, b)  # Observe that the output of this function is written between brackets

# Nevertheless basic operations between different type variables are not allowed. For instance,
# we cannot add a string and an integer.

# print(my_name + three)  # Please, uncomment this line if you want to check that a type error is produced.

# The same happens if we try to sum a string and a float

# print(my_name + four) # Remind again to uncomment this line to see the error.

# However, an integer and a float number can be added. The result is a float number.

print(three + four)


# EXERCISE 1: Define an string, a float and an integer number. Print them with an if condition using string
# interpolation:

my_string = "hello"
my_float = 10.0
my_integer = 20

if my_string == "hello":
    print("The string is %s" % my_string)

if isinstance(my_float, float) and my_float == 10.0:
    print("The float is %f" % my_float)

if isinstance(my_integer, int) and my_integer == 20:
    print("The integer is %d" % my_integer)

# EXERCISE 2: Repeat exercise 1 but checking what happens if we print an integer as a float and vice versa:

my_new_float = 10.4
if isinstance(my_new_float, float):
    print("The float is %d" % my_new_float)
if isinstance(my_integer, int):
    print("The integer is %f" % my_integer)

# Check that if a float is printed as an integer, then the fractional part is not written. Pay attention to this point.

