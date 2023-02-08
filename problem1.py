# Shared under Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license
# (link: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

# Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, by finding
# solutions to the Diophantine equation. You can solve this in your head, using paper and pencil,
# or writing a program. However you chose to solve this problem, list the combinations of 6, 9
# and 20 packs of McNuggets you need to buy in order to get each of the exact amounts.
# Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by combinations of 6,
# 9 and 20 packs, show that it is possible to buy 56, 57,…, 65 McNuggets. In other words, show
# how, given solutions for 50-55, one can derive solutions for 56-65.

def problem1(target):
    for a in range(int(target / 6) + 1):
        for b in range(int(target / 9) + 1):
            for c in range(int(target / 20) + 1):
                if (a * 6) + (b * 9) + (c * 20) == target:
                    return (a, b, c)


for i in range(50, 56):
    print(problem1(i))
