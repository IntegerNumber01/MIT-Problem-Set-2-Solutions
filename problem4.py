# Assume that the variable packages is bound to a tuple of length 3, the values of which specify
# the sizes of the packages, ordered from smallest to largest. Write a program that uses
# exhaustive search to find the largest number (less than 200) of McNuggets that cannot be
# bought in exact quantity. We limit the number to be less than 200 (although this is an arbitrary
# choice) because in some cases there is no largest value that cannot be bought in exact quantity,
# and we don’t want to search forever. Please use ps2b_template.py to structure your code.
# Have your code print out its result in the following format:
# “Given package sizes <x>, <y>, and <z>, the largest number of McNuggets that
# cannot be bought in exact quantity is: <n>”
# Test your program on a variety of choices, by changing the value for packages. Include the
# case (6,9,20), as well as some other test cases of your own choosing.

def diophantine(x, y, z, target):
    storage = []
    for a in range(int(target / x) + 1):
        for b in range(int(target / y) + 1):
            for c in range(int(target / z) + 1):
                if (a * x) + (b * y) + (c * z) == target:
                    storage.append((a, b, c))

    return storage


def problem4(x, y, z):
    for i in range(200, 0, -1):
        if diophantine(x, y, z, i) == []:
            return 'Given package sizes ' + str(x) + ', ' + str(y) + ', and ' + str(z) + ', the largest number of McNuggets that cannot be bought in exact quantity is:  ' + str(i)


print(problem4(6, 9, 20))
