#!/usr/bin/python3
"""
Prime Game: Determine the winner of a game involving prime numbers.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of boolean values indicating if numbers up to n are prime.
    Args:
        n (int): The maximum number to check for primes.

    Returns:
        list: A list where index i is True if i is prime, otherwise False.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes


def play_game(n, primes):
    """
    Simulate a single round of the prime game.

    Args:
        n (int): The maximum number in the range for the game.
        primes (list): Precomputed list of boolean values for prime numbers.

    Returns:
        bool: True if Maria wins, False if Ben wins.
    """
    moves = 0
    is_prime = primes[:]

    for num in range(2, n + 1):
        if is_prime[num]:
            moves += 1
            for multiple in range(num, n + 1, num):
                is_prime[multiple] = False

    return moves % 2 == 1  # Maria wins if odd number of moves


def isWinner(x, nums):
    """
    Determine the overall winner of the prime game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n values for each round.

    Returns:
        str or None: The name of the player with the most wins /
        ("Maria" or "Ben"),
                     or None if there is a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
