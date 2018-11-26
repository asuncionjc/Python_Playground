# "FOR" LOOPS

Fantastic_team = ["Ana", "Asun", "Bea", "Cristina", "Lorena", "Marina", "Mercedes"]
for girl in Fantastic_team:
    print(girl)

# Iterate over a sequence of numbers

# Prints out 0, 1, 2
for number in range(3):
    print(number)

# Prints out 3, 4, 5
for number in range(3, 6):
    print(number)

# Returns the odd numbers from 3 to 19
for number in range(3, 20, 2):
    print(number)

# We can replace range by xrange. The main difference is that the first function returns a new list with numbers of
# specified range, while the second function returns an iterator, which is more efficient, especially in the cases where
# we have to iterate a big list of numbers.
for number in xrange(3):
    print(number)

# "WHILE" LOOPS
number = 0
while number <= 10:
    print(number)
    number += 1

# "BREAK" AND "CONTINUE" STATEMENTS

# Break example
while True:
    print(number)
    if number >= 20:
        break
    if number % 2 == 0:
        print("The number is even")
    number = number + 1

# Continue example
for iterator in range(10):
    if iterator % 2 == 1:
        continue
    print(iterator)


# New examples to see the difference between break and continue

# Prints out s t r The end
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")

# Prints out s t r n g The end
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

# 'ELSE' CLAUSES IN LOOPS

# While
count = 0
while count <= 10:
    print(count)
    count += 1
else:
    print("The count reaches the number %d" % count)

# For
for count in range(1, 10):
    if count % 3 == 0:
        break
    print(count)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition")

# EXERCISE 1: Loop through and print out all even numbers from the numbers list in the same order they are received.
# Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number % 2 == 0:
        print(number)
        continue
    if number == 237:
        break
