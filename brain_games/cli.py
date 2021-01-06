# -*- coding: utf-8 -*-
"""Module for greet users."""
import prompt


def welcome_user():
    """Ask for user`s name.

    Keep asking while no answer.
    Return the string, name of the user.
    """
    return prompt.string('May I have your name? ')
