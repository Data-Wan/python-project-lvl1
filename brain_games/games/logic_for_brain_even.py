# -*- coding: utf-8 -*-

"""Module with logic for game brain_even.

brain_even - game with random numbers
User must answer is number even  or not.
"""


import random

import prompt


def is_even():
    """Return True or False.

    True - correct answer, user win.
    False - wrong answer, stop game, computer win

    Returns:
        dict
    """
    random_number = random.randint(1, 100)
    is_random_even = 'yes' if random_number % 2 == 0 else 'no'
    user_input = prompt.string(question.format(random_number))

    if user_input == is_random_even:

        return {
            'result': True,
            'user_input': user_input,
            'random_number': random_number,
            'right_answer': is_random_even,
        }

    return {
        'result': False,
        'user_input': user_input,
        'random_number': random_number,
        'right_answer': is_random_even,
    }


question = 'Question: {0}\nYour answer: '
game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
