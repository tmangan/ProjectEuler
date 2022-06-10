#!/usr/bin/env python3


"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve():
    """
        Adds the numbers divisible by those in div_set
        up to (not including) high_val
    """

    divisible_numbers = [3, 5]
    highest_value = 1000
    running_total = 0

    for i in range(highest_value):

        truth_table = []
        for j in divisible_numbers:
            if i % j == 0:
                truth_table.append(True)
            else:
                truth_table.append(False)
        if any(truth_table):
            running_total += i

    return running_total


if __name__ == "__main__":
    print(solve())
