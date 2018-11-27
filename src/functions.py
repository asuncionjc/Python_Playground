# Write a function
def my_function():
    print("This is the first function I write")


# Execute a function
my_function()


# Function with arguments

def function_with_arguments(name, greetings):
    print("%s! My name is %s" % (greetings, name))


function_with_arguments("Asun", "Hi")
function_with_arguments("Andrea", "Hello")


# Functions with a return value

def multiply_two_numbers(number_1, number_2):
    return number_1 * number_2


a = multiply_two_numbers(2, 3)
print("The result value is %f" % float(a))


# EXERCISE 1: Fizz Buzz Test. Write a program that prints the numbers from 1 to 100. But for multiples of three print
# "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both
# three and five print "FizzBuzz"

def fizz_buzz_test(value):
    if isinstance(value, list):
        fizz_buzz_list(value)
    elif isinstance(value, int):
        fizz_buzz_list(range(value, value + 1))
    else:
        print("The input value you've passed is not allowed")


def fizz_buzz_list(range_numbers):
    for number in range_numbers:
        if is_multiple_of_3(number) and is_multiple_of_5(number):
            print("FizzBuzz")
        elif is_multiple_of_3(number):
            print("Fizz")
        elif is_multiple_of_5(number):
            print("Buzz")
        else:
            print(number)


def is_multiple_of_5(value):
    return is_multiple_of(value, 5)


def is_multiple_of_3(value):
    return is_multiple_of(value, 3)


def is_multiple_of(value, number):
    return value % number == 0


fizz_buzz_test(range(1, 101))
fizz_buzz_test(11)

# EXERCISE 2: In this exercise you'll use an existing function, and while adding your own to create a fully functional
# program from the commented information.
# 1) Add a function named list_benefits() that returns the following list of strings: "More organized code", "More
# readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# 2) Add a function named build_sentence(info) which receives a single argument containing a string and returns a
# sentence starting with the given string and ending with the string " is a benefit of functions!"
#
# 3) Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
# def list_benefits():
#     pass
#
# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     pass
#
# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#
# name_the_benefits_of_functions()


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and " \
                                                                               "connect code together"


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()





