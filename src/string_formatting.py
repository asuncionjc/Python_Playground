# How to format the string

my_name = "Asun"
print("My name is %s. What's yours?" % my_name)

# How to format more than one argument

my_favourite_colour = "red"
my_favourite_number = 2

print("My name is %s. My favourite number and colour are %d and %s, respectively" % (my_name, my_favourite_number, my_favourite_colour))

# Any object which is not a string can be also formatted with %s
my_list = [my_name, my_favourite_colour, my_favourite_number]
print("The list is %s" % my_list)

# EXERCISE 1: Let us practice with the different formats:

# a) %s - String (or any object with a string representation, like numbers)
# b) %d - Integers
# c) %f - Floating point numbers
# d) %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# e) %x/%X - Integers in hex representation (lowercase/uppercase)

# a)
print("%s is a nice name" % my_name)

# b)
print("February is the month number %d" % my_favourite_number)

# c)
float_number = 5/3.0
print("Divide 5 and 3 gives %f as result" % float_number)

# d)

print("Divide 5 and 3 gives %.2f as result (with two decimal numbers)" % float_number) #IMPORTANT: Please note that
# Python round by default

# e)
print("February is the month number %X" % my_favourite_number)
