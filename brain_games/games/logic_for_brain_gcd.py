# -*- coding: utf-8 -*-
"""Module with logic for game brain_gcd.

brain_gcd - game with random numbers
User must answer what the greatest divisor of  number1 and number2.
"""

import random
from math import gcd

import prompt


def find_gcd():
    """Return True or False, user input and right answer.

    True - correct answer, user win.
    False - wrong answer, stop game, computer win

    Returns:
        dict
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)

    divisor = gcd(random_number1, random_number2)

    user_input = prompt.string(question.format(random_number1, random_number2))

    if user_input == str(divisor):

        return {
            'result': True,
            'user_input': user_input,
            'right_answer': divisor,
            'game_rules': game_rules,
        }

    return {
        'result': False,
        'user_input': user_input,
        'right_answer': divisor,
        'game_rules': game_rules,
    }


question = 'Question: {0} {1}\nYour answer: '
game_rules = 'Find the greatest common divisor of given numbers.'
