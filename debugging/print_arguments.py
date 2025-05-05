#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)
        f = factorial(n)
        print(f)
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
