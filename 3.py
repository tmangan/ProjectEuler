#!/usr/bin/env python3

import numpy as np


def find_smallest_factor(composite):
    """
        returns the smallest factor (always prime) of n
    """
    biggest_attempt = int(np.sqrt(composite)) + 1
    for i in range(2, biggest_attempt):
        if composite % i == 0:
            return i
    return composite  # Not actually a composite, but a prime!


def solve(n):
    """
        takes a composite number and returns the largest prime factor
    """
    while True:
        attempt = find_smallest_factor(n)
        if attempt < n:
            n //= attempt
        else:
            return attempt


if __name__ == "__main__":
    print(solve(600851475143))
