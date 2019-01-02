# EXERCISE:
# The aim of this code is to generate the first 5 numbers of the Fibonacci succession, and then compute the mean and the
# variance of such list of numbers without using the Python libraries.

# WHICH IS THE STRUCTURE OF THE CODE?
# This code has two main parts The first one is formed by all the functions necessary to execute the code. The second
# part is just such execution.

# FUNCTIONS

def get_fibonacci_list(range_number_fibonacci):
    fibonacci_list = []
    for number in range_number_fibonacci:
        fibonacci_list.append(fibonacci(number))
    return fibonacci_list


# Recursive function
def fibonacci(number):
    if number == 0:
        fibonacci_number = 0
    elif number == 1:
        fibonacci_number = 1
    else:
        fibonacci_number = fibonacci(number - 1) + fibonacci(number - 2)
    return fibonacci_number


def print_fibonacci_list(range_fibonacci_numbers):
    fibonacci_list = get_fibonacci_list(range_fibonacci_numbers)
    print(fibonacci_list)


def squared_numeric_list(list_of_numbers):
    squared_list = []
    for i in list_of_numbers:
        squared_list.append(i ** 2)
    return squared_list


# EXECUTION
lower_bound_range = 0
upper_bound_range = 5
range_fibonacci_list = range(lower_bound_range, upper_bound_range + 1)

fibonacci_list = get_fibonacci_list(range_fibonacci_list)
print_fibonacci_list(range_fibonacci_list)

# Mean Fibonacci list
length_fibonacci_list = len(fibonacci_list)
mean_fibonacci_list = float(sum(fibonacci_list) / length_fibonacci_list)
print("The mean of the selected Fibonacci list from %d to %d is %.2f" % (lower_bound_range, upper_bound_range,
                                                                         mean_fibonacci_list))

# Variance Fibonacci list
squared_list_fibonacci = squared_numeric_list(fibonacci_list)

print(squared_list_fibonacci)
variance_fibonacci_list = (1.0 / (length_fibonacci_list - 1)) * sum(squared_list_fibonacci) - mean_fibonacci_list ** 2
print("The standard deviation of the selected Fibonacci list from %d to %d is %.2f" % (lower_bound_range,
                                                                                       upper_bound_range,
                                                                                       variance_fibonacci_list))
