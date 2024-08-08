#!/usr/bin/python3
"""Module for prime game"""


def isWinner(x, nums):
    """Function to check who will win the game"""
    maria = 0
    ben = 0
    for num in nums:
        rounds = list(range(1, num+1))
        primes = [n for n in range(2, num + 1) if is_prime(n)]

        if not primes:
            ben += 1
            continue

        mariasTurn = True

        while(True):
            if not primes:
                if mariasTurn:
                    ben += 1
                else:
                    maria += 1
                break
            smallestPrime = primes.pop(0)
            rounds.remove(smallestPrime)

            rounds = [x for x in rounds if x % smallestPrime != 0]

            mariasTurn = not mariasTurn

    if maria > ben:
        return "Maria"

    if maria < ben:
        return "Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True