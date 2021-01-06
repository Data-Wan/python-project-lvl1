#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script for start brain_games."""

from brain_games.cli import welcome_user


def main():
    """Make a user intreface.

    Greet user + return name of user.

    Returns:
        str
    """
    print('Welcome to the Brain Games')
    name = welcome_user()
    print('Hello, {0}!'.format(name))
    return name


if __name__ == '__main__':
    main()
