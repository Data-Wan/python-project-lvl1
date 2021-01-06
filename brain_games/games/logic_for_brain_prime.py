# -*- coding: utf-8 -*-
"""Module with logic for game brain_gcd.

brain_prime - game with random numbers
User must answer is number prime or not.
"""

import random

import prompt

from brain_games.games.is_prime import is_prime


def prog():  # noqa: WPS210
    """Return True or False, user input and right answer.

    True - correct answer, user win.
    False - wrong answer, stop game, computer win

    Returns:
        dict
    """
    comp_input = random.randint(1, 100)
    answer = 'yes' if is_prime(comp_input) else 'no'
    user_input = prompt.string(question.format(comp_input))

    if user_input == str(answer):

        return {
            'result': True,
            'user_input': user_input,
            'right_answer': answer,
        }

    return {
        'result': False,
        'user_input': user_input,
        'right_answer': answer,
    }


question = 'Question: {0} \nYour answer: '
game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
