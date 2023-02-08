# Using this theorem, we can write an exhaustive search to find the largest number of McNuggets
# that cannot be bought in exact quantity. The format of the search should probably follow this
# outline:

# Hypothesize possible instances of numbers of McNuggets that cannot be purchased
# exactly, starting with 1
# For each possible instance, called n,
# Test if there exists non-negative integers a, b, and c, such that
# 6a+9b+20c = n. (This can be done by looking at all feasible
# combinations of a, b, and c)
# If not, n cannot be bought in exact quantity, save n
# When you have found six consecutive values of n that in fact pass the test of
# having an exact solution, the last answer that was saved (not the last value
# of n that had a solution) is the correct answer, since you know by the
# theorem that any amount larger can also be bought in exact quantity

# Write an iterative program that finds the largest number of McNuggets that cannot be bought in
# exact quantity. Your program should print the answer in the following format (where the correct
# number is provided in place of <n>):
# “Largest number of McNuggets that cannot be bought in exact quantity: <n>”
# Hint: your program should follow the outline above.
# Hint: think about what information you need to keep track of as you loop through possible ways
# of buying exactly n McNuggets. This will guide you in deciding what state variables you will need
# to utilize.

def diophantine(target):
    storage = []
    for a in range(int(target / 6) + 1):
        for b in range(int(target / 9) + 1):
            for c in range(int(target / 20) + 1):
                if (a * 6) + (b * 9) + (c * 20) == target:
                    storage.append((a, b, c))

    return storage


def problem3():
    i = 0
    check = 0
    storage = []

    while not check >= 6:
        if diophantine(i) == []:
            storage.append(i)
            check = 0
        else:
            check = check + 1

        i = i + 1

    return 'Largest number of McNuggets that cannot be bought in exact quantity: ' + str(storage[-1])


print(problem3())
print(diophantine(50))
