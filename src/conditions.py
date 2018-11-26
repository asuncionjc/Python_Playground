# Conditions

x = 2
print(x == 2)
print(x == 3)
print(x < 3)
print(x != 3)

# Boolean Operators
name = "Asun"
favourite_number = 2

if name == "Asun" and favourite_number == 2:
    print("My name is Asun and my favourite number is 2")

if name == "Asun" or name == "Andrea":
    print("My name is Asun")

# The 'in' operator

name_list = ["Andrea", "Asun"]
if name in name_list:
    print("Your name is either %s or %s" %(name_list[0], name_list[1]))

# General 'if' statement example

# x = 3  # Uncomment these lines to enter in each one of the choices in the 'if' statement
# x = "hello"

if x == 2:
    print("The value of x is %d" % x)
elif x == 3:
    print("The value of x is not 2")
else:
    print("Change the value of x")


# The 'is' operator

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Contrary to what happen with the "==" operator, the 'is' operator match the instances themselves.

print(x == y)  # Prints out True
print(x is y)  # Prints out False
print(x is z)  # Prints out True

# The 'not' operator

print(not False)

# EXERCISE 1: Change the variables in the commented first section, so that each if statement resolves as True.

# change this code
# number = 10
# second_number = 10
# first_array = []
# second_array = [1,2,3]
#
# if number > 15:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 2:
#     print("3")
#
# if len(first_array) + len(second_array) == 5:
#     print("4")
#
# if first_array and first_array[0] == 1:
#     print("5")
#
# if not second_number:
#     print("6")

number = 20
second_number = 0
first_array = [1, 1, 1]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print(first_array[0])
    print("5")

if not second_number:
    print("6")

# In this exercise we learn that the booleans True and False are associated respectively to the values 1 and 0.
