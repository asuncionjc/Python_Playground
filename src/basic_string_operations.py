# How to print a string

my_string = "This is a string because it is written between double quotes. They can be also written between single" \
            " quotes"
print(my_string)

# Length of a string

print("The length of the string is %d" % len(my_string))

# How to know the first time a letter appears?
random_character = "T"
print("The first time that letter %s appears is %d" % (random_character, my_string.index(random_character)))
# Remember that the indexes in Python start at zero instead of one.

# What about the first time a substring appears?
# With the very same function used in the previous example, we can know which is the index such that the first letter of
# a substring appears

my_substring = "because"
print("The letter 'b' of the word %s first appears at index %d" % (my_substring, my_string.index(my_substring)))

# If a letter or a substring is not in the main string, the function .index returns an error.
# print(my_string.index("z"))  # Uncomment this line to see the error.
# print(my_string.index("hello"))  # Uncomment this line to see the error.

# Count the number of times a letter appears

my_letter = "a"
print("The letter '%s' appears %d times" % (my_letter, my_string.count(my_letter)))

# The same function can be use with substring
second_substring = "is"
print("The substring '%s' appears %d times" % (second_substring, my_string.count(second_substring)))

# How to extract some substrings of the main string
start_index = 1
end_index = 5
print("The substring between the index %d and %d is '%s'" % (start_index, end_index, my_string[start_index:(end_index +
                                                                                                            1)]))
# IMPORTANT: Note that the lower bound coincides with the index where we want to start. Nevertheless, the upper bound is
# one unit more than the index at which we want to finish.

# Other examples

print("This substring goes from index %d to the end: '%s'" % (start_index, my_string[start_index:]))
print("This substring goes from the beginning to the index %d: '%s'" % (end_index, my_string[:(end_index + 1)]))
print("This substring is extracted from the end of the sentence because minus sign , -, is used: '%s'. It goes from "
      "index %d until %d" % (my_string[-end_index:-start_index], -end_index, -start_index))

# We can also extract some substrings separated by a fixed step. For instance:
step = 2
print("This substring begins at index %d, finishes at index %d and has a jump step of %d: '%s" %(start_index, end_index,
                                                                                               step,
                                                                                                 my_string[
                                                                                                 start_index:
                                                                                                 (end_index + 1):step]))
# Reverse a string.
# To do this, the tools previously mentioned are used.

print("The reverse string is '%s'" % my_string[::-1])

# Upper and lower case
# The whole string can be converted in upper and lower case:
print("Upper case string: %s" % my_string.upper())
print("Lower case string: %s" % my_string.lower())

# How to know if a string begins or ends with a substring
print("It is %s that the string begins with the word 'This'" % my_string.startswith("This"))
print("It is %s that the string ends with the word 'goodbye'" % my_string.endswith("goodbye"))

# How to split a string

# We can split the string in different substrings separated as desired. The output is a list whose elements are
# substrings. Some examples:

# Separated by spaces
string_split_by_spaces = my_string.split(" ")
print("The list of substrings separated by spaces %s" % string_split_by_spaces)

# Separated by dots
string_split_by_dots = my_string.split(".")
print("The list of substrings separated by dots %s" % string_split_by_dots)

# EXERCISE 1: Summarize all the information learnt in this script

string_exercise = "Strings are nice! =)"
print("The length of the string is %d" % len(string_exercise))
letter_a = "a"
print("The first occurrence of %s is at index %d" % (letter_a, string_exercise.index(letter_a)))
print("%s occurs %d times" % (letter_a, string_exercise.count(letter_a)))
print("The first 5 characters of the string are '%s'" % string_exercise[:5])
print("The next five characters are '%s'" % string_exercise[5:10])
print("The characters with odd indexes are '%s" % string_exercise[1::2])
print("The last five characters are '%s'" % string_exercise[-5:])
print("The string into uppercase is %s" % string_exercise.upper())
if string_exercise.startswith("Strings"):
    print("This exercise is spectacular! =)")

print("The string split by spaces is the list %s" % string_exercise.split(" "))

