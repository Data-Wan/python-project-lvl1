# -*- coding: utf-8 -*-

"""Module with logic for game brain_calc.

brain_calc - game with random numbers
User must answer what number equals number1 + number2.
"""


import random

import prompt


def calc():
    """Return True or False, user input and right answer.

    True - correct answer, user win.
    False - wrong answer, stop game, computer win

    Returns:
        dict
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)

    calculation = random_number1 + random_number2
    user_input = prompt.string(question.format(random_number1, random_number2))

    if user_input == str(calculation):

        return {
            'result': True,
            'user_input': user_input,
            'right_answer': calculation,
        }

    return {
        'result': False,
        'user_input': user_input,
        'right_answer': calculation,
    }


question = 'Question: {0} + {1}\nYour answer: '
