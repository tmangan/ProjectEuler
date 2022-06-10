#!/usr/bin/env python3


def solve(largest_n):
    """
        returns the sum of even valued fibonacci numbers up to largest_n
    """
    
    running_total = 0  # Initialization of variables
    nth_fib = 1
    n_plus_one_fib = 2

    while nth_fib <= largest_n:
        
        if nth_fib % 2 == 0:
            running_total += nth_fib
        
        # Cycle the Fibonacci Sequence one term
        nth_fib, n_plus_one_fib = n_plus_one_fib, n_plus_one_fib + nth_fib

    return running_total


if __name__ == "__main__":
    print(solve(4000000))
