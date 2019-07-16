#!/usr/bin/python3
"""Factorial Algorithm

A simple implementation of the classic algorithm.
"""

def factorial(number):
    """Calculates the factorial of n"""
    accum = 1
    for i in range(number, 0, -1):
        accum *= i

    return accum


def main(number):
    """Runs the main algorithm and presents the result."""
    result = factorial(number)
    print(f"Factorial of {number} is {result}.")


if __name__ == '__main__':
    import sys
    main(int(sys.argv[1]))
