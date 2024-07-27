#!/usr/bin/python3
"""Make changes"""

def makeChange(coins, total):
    """
    this function determines the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    """
    table[row][col] = table[row-1][col] +
    table[row][col- coins[row-1]]
    """
    table = [float('inf')] * (total + 1)
    table[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            table[x] = min(table[x], table[x - coin] + 1)
    return table[total] if table[total] != float('inf') else -1
