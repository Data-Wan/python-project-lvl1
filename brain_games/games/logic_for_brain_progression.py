# -*- coding: utf-8 -*-
"""Module with logic for game brain_gcd.

brain_gcd - game with random numbers
User must answer what the greatest divisor of  number1 and number2.
"""

import random

import prompt


def prog():
    """Return True or False, user input and right answer.

    True - correct answer, user win.
    False - wrong answer, stop game, computer win

    Returns:
        dict
    """
    progression.clear()
    random_skip = random.randint(1, 9)
    increase = random.randint(1, 10)
    progression.insert(0, random.randint(1, 30))
    random_skip = random.randint(1, 9)
    increase = random.randint(1, 10)
    index = 1
    while index < 10:
        progression.insert(index, progression[index - 1] + increase)
        index += 1

    answer = progression.pop(random_skip)
    progression.insert(random_skip, '..')

    user_input = prompt.string(question.format(progression))

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


question = 'Question: {0}\nYour answer: '
game_rules = 'What number is missing in the progression?'

progression = []
