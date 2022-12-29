""" Run Quiz """

from quiz_functions import (welcome, get_username, display_instructions,
                            ask_questions, dispay_final_result,
                            update_spreadsheet, show_leaderboard,
                            terminate_quiz)


def main():
    """
    Runs all of the functions for the quiz in the required sequence.

    The score is used to keep tally of the points awarded for correct answers.
    The question_index keeps track of the questions asked.
    """
    score = 0
    question_index = 0
    welcome()
    name = get_username()
    display_instructions(name)
    final_score = ask_questions(question_index, score)
    dispay_final_result(final_score)
    update_spreadsheet(final_score, name)
    show_leaderboard()
    terminate_quiz()


if __name__ == '__main__':
    main()
