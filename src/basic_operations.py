# ARITHMETIC OPERATIONS

# The basic operations addition, subtraction, multiplication and division are denoted with the symbols +, -, * and /,
# respectively.

operation = 1 + 2 - 3*4/5
print("The result of the operation is %d" % operation)

# IMPORTANT: Python follows the order of the operations, i.e., first multiplication and division, and then then addition
# and subtraction from left to right. However pay attention, because we are working with integer variables, and
# therefore the result is also an integer. For instance: 3*4/5 = 12/5 = 2, and not 2.4
# Let us see the very same example with float numbers. It is sufficient to write one of them as float

operation_with_float = 1 + 2 - 3*4/5.0
print("The result of the operation is %f" % operation_with_float)

# MODULO

# The modulo operator, i.e. the operation which returns the remainder of a division is denoted as %

modulo = 11 % 2
print("The remainder of dividing 11 and 2 is %f" % modulo)

# POWER

# Two consecutive * symbols are used to create the power of a number:
power = 11**2
print("The square of 11 is %d" % power)

# BASIC OPERATIONS WITH STRINGS

# Addition

my_name = "Asun"
what_is_your_name = "My name is"
say_your_name = what_is_your_name + " " + my_name
print(say_your_name)

# Multiplication

repeat_my_name = my_name*20
print(repeat_my_name)

# BASIC OPERATIONS WITH LISTS

# Addition

# Add two lists with the + symbol will concatenate them.

L2_team = ["Alba", "Asun", "Marina", "Vanesa"]
IMUS_team = ["Cristina", "Reme", "Sandra", "Tom"]

IO_team = L2_team + IMUS_team
print(IO_team)

# Multiplication

# Multiply one list times a number will concatenate the list as many times as the number indicates:
print(IMUS_team*2)

# EXERCISE 1: Create two lists with the same object repeated 10 times. Then, you have to create a new bigger list,
# concatenating the two previous lists. Finally, check that the three lists are well created and print a congrats
# message.

ying = "ying"
yang = "yang"

ying_list = [ying]
ying_list = ying_list*10
print(ying_list)

yang_list = [yang]
yang_list = yang_list*10
print(yang_list)

ying_yang_list = ying_list + yang_list
print(ying_yang_list)

# To check that the three lists are well created, we are going to learn a new function which tell us the length of an
# object. Particularly, the length of a list:

number_of_elements_ying_list = len(ying_list)
print("The number of elements of the ying list is %d" % number_of_elements_ying_list)
number_of_elements_yang_list = len(yang_list)
print("The number of elements of the yang list is %d" % number_of_elements_yang_list)
number_of_elements_ying_yang_list = len(ying_yang_list)
print("The number of elements of the ying-yang list is %d" % number_of_elements_ying_yang_list)

# Moreover, to check how many elements of each time there is in a list, let use the .count function. For instance:
number_of_ying_in_the_ying_list = ying_list.count(ying)
print("The number of yings in the ying list is %d" % number_of_ying_in_the_ying_list)
number_of_yang_in_the_ying_list = ying_list.count(yang)
print("The number of yangs in the ying list is %d" % number_of_yang_in_the_ying_list)

number_of_ying_in_the_ying_yang_list = ying_yang_list.count(ying)
number_of_yang_in_the_ying_yang_list = ying_yang_list.count(yang)
print("The number of yings and yangs in the ying yang list is %d" % number_of_ying_in_the_ying_yang_list)