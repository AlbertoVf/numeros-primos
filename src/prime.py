import math


def is_prime(n) -> bool:
    """
    Check if a number is prime or not
    :param n: number to check
    :return: Boolean with the result (True or False)
    """
    divisors = 0
    if n < 2:
        return False

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 1
            if divisors > 1:
                return False
    return True


def prime_list(i, f) -> list:
    """
    Generate a list of prime numbers between i and f
    :param i: first number, included in the list
    :param f: last number, excluded from the list
    :return: list of prime numbers
    """
    list = []
    for n in range(i, f):
        list.append(n) if is_prime(n) else None
    return list
