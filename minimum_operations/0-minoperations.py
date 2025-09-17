#!/usr/bin/python3

"""Calculates the minimum number of operations to reach n 'A's starting from one 'A'. With only two operations
allowed: Copy All and Paste."""


def minOperations(n):
    ops = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                ops += i
                break
    return ops
