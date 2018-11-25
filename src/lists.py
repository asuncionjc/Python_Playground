# HOW TO BUILD A LIST:

# First, we should initialize the list. Empty lists are denoted with squared brackets:

my_list = []

# One way to add elements to a list is to append them at the end of it one by one. Remember that
# a list can contain elements of different types:

my_list.append(1)
my_list.append("hello")
print(my_list)  # Observe that the list is printed between squared brackets

for element in my_list:
    print(element)

# This is the very first time we use a for loop. Note that it instructions must be also indented,
# as happens in the if conditional

# We cannot access to an element which does not exist. For instance:

# print(my_list[5])  # Uncomment this line to see the error.

# Another form to create a list is to initialize it with some elements between squared brackets. For example:

strings = ["hello", "world" "and" "goodbye" "world"]

# EXERCISE 1: Create a list with numbers 1, 2 and 3, and another one with the names Alba, Asun, Marina and Vanesa.
# Then you have to access to the second name of the list:

number_list = [1, 2, 3]
L2_team = ["Alba", "Asun", "Marina", "Vanesa"]

second_L2_team_member = L2_team[1]  # IMPORTANT: Note that Python is a zero-based-index language. Hence, to access to
# the second item you have to index it as 1.

print("One of the members of the L2 team is %s" % second_L2_team_member)
