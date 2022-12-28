""" Main Function to Run Quiz """

from quiz_functions import (welcome, get_username, display_instructions,
                            ask_questions, dispay_final_result,
                            update_spreadsheet, show_leaderboard)


def main():
    """
    Runs all of the functions for the quiz in the required sequence.
    """
    score = 0
    question_index = 0
    welcome()
    name = get_username()
    display_instructions(name)
    ask_questions(question_index, score)
    dispay_final_result(score)
    update_spreadsheet(score, name)
    show_leaderboard()


main()
