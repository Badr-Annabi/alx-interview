#!/usr/bin/python3
"""Module for prime game"""


def isPrime(n):
    """this function Return primes list"""
    prime = []
    seg_sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (seg_sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                seg_sieve[i] = False
    return prime


def isWinner(x, nums):
    """This function checks who will win maria or ben"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        primes = isPrime(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
