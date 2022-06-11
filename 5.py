#!/usr/bin/env python3


"""
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""


def solve(upper_bound):

    primes = make_prime_list(upper_bound)
    prime_multiplicities = []
    answer = 1

    for p in primes:
        n = 1
        while p ** n <= upper_bound:
            n += 1
        prime_multiplicities.append(n - 1)

    if len(primes) != len(prime_multiplicities):
        raise ValueError("bases and multiplicities not aligned")

    for i in range(0, len(primes)):
        answer *= primes[i] ** prime_multiplicities[i]

    return answer


def make_prime_list(upper_bound):
    primes = [2]
    for i in range(3, upper_bound):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes 


if __name__ == "__main__":
    print(solve(20))
