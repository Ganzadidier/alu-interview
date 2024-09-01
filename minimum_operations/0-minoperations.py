#!/usr/bin/python3
""" Minimum operations to produce n Hs"""


def minOperations(n):
    """Minimum ops"""
    if n<=1:
        return 0

    i=2
    operation=0

    while n > 1:
        while n % i == 0:
            operation += i
            n //= i
        i += 1
    
    return operation
