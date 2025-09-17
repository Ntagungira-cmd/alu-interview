#!/usr/bin/python3

def minOperations(n):
    ops = 0
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                ops += i
                break
    return ops


if __name__ == "__main__":
    print(minOperations(12))
