#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script for brain_even.

brain_even - game with random numbers
User must answer is number even  or not.
"""


from brain_games.games.logic_for_brain_even import is_even
from brain_games.scripts.brain_games import main as welcome

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'

wrong_answer_out = """
'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!'
    """


def main():
    """
    Describe game rules and ask a question.

    User need 3 correct answer in a row for win.
    One lose = game over

    Returns:
        str
    """
    name = welcome()
    print(game_rules)
    correct_answer_count = 0
    result_of_game = is_even()

    while result_of_game['result']:
        correct_answer_count += 1
        print('Correct!')

        if correct_answer_count == 3:
            print('Congratulations, {0}!'.format(name))
            return 0

        result_of_game = is_even()

    print(
        wrong_answer_out.
        format(
            result_of_game['user_input'],
            result_of_game['right_answer'],
            name,
        ),
    )


if __name__ == '__main__':
    main()
