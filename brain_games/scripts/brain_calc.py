#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script for brain_calc.

brain_calc - game with random numbers
User must answer what number equals number1 + number2.
"""


from brain_games.logic_for_brain_calc import calc
from brain_games.scripts.brain_games import main as welcome

game_rules = 'What is the result of the expression?'

wrong_answer_out = """
'{0}' is wrong answer ;(. Correct answer was '{1}'.
"Let's try again, {2}!'
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
    result_of_game = calc()

    while result_of_game['result']:
        correct_answer_count += 1
        print('Correct!')

        if correct_answer_count == 3:
            print('Congratulations, {0}!'.format(name))
            return 0

        result_of_game = calc()

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
