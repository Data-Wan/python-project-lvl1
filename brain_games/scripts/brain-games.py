#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main execution file."""

from brain_games.cli import welcome_user


def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games')
    name = welcome_user()
    print('Hello, {}!'.format(name))


if __name__ == '__main__':
    main()
