# -*- coding: utf-8 -*-
"""Function check 1 number prime or not."""


def is_prime(number):
    """Check number for prime.

    Args:
        number: integer

    Returns:
        boolean: True if number is prime, else False.
    """
    index = number // 2
    while index > 1:
        if number % index == 0:
            return False
        index -= 1
    return True
