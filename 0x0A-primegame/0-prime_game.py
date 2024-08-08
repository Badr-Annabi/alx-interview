#!/usr/bin/python3
"""Module for prime game"""


def isWinner(x, nums):
    """Function to check who will win the game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None

    def is_prime(n):
        """Returns True if n is prime, else False"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes = [n for n in range(2, num + 1) if is_prime(n)]
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
