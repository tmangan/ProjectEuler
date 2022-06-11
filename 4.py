#!/usr/bin/env python3

"""
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solve(number_digits):

    """
        returns the largest palindrome composed of two n-digit numbers
    """

    palindrome = 0          # initialize variables
    range_min = 10**(number_digits - 1)
    range_max = 10**(number_digits)

    for i in range(range_min, range_max):
        for j in range(range_min, range_max):
            attempt = i * j

            # check if palindrome
            if str(attempt) == str(attempt)[::-1]:

                # check if new largest
                if attempt > palindrome:
                    palindrome = attempt

    return palindrome


if __name__ == "__main__":
    print(solve(3))
