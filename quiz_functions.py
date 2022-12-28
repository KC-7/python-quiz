""" Contains the Quiz Functions """

import os
import gspread
from google.oauth2.service_account import Credentials
from questions import QUESTIONS
from style import Sty
from ascii import Ascii


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz')


def welcome():
    """
    Welcome screen for user.
    Displays Ascii text with logo styling.
    """
    os.system("clear")
    print("Welcome To KC-7 Quiz:\n")
    print(Ascii.quiz)
    print("\nGet ready to start!\n")
    input("Press Enter to continue...")


def get_username():
    """
    Get username input from user.
    Prints ASCII header.
    Run a while loop to ensure username is submited correctly,
    must be a string between 2 and 8 letters. Loop will repeat
    until the username is valid.

    Returns:
        Returns the username if the user's input is valid.
    """
    os.system("clear")
    print(Ascii.username)
    while True:
        print("Please enter your username.")
        print("Your name must be between 2 and 8 letters. Example: Tony.\n")
        username = input("Enter your username here:\n")
        if validate_username(username):
            break
    return username


def validate_username(username):
    """
    Validates username input is correct length and loops if not.

    Args:
        username (str): This value is checked to ensure it is within the
        required length, between 2 & 8 letters and that all characters
        are alphabetical.

    Returns:
        Returns True if answer is valid, otherwise False.
    """
    name_len = len(username)
    while name_len > 8 or name_len < 2 or username.isalpha() is False:
        os.system("clear")
        print(Ascii.username)
        print(Sty.neg)
        print("Your username must be between 2 & 8 alabetical letters.")
        print(f'You entered: "{username}", this is {name_len} character(s).')
        print(Sty.clr)
        return False
    return True


def display_instructions(username):
    """
    Prints ASCII header.
    Displays validated username and instructions.

    Args:
        username (str): This value is displayed to the user in the
        instructions text to improve UX.
    """
    os.system("clear")
    print(Ascii.howToPlay)
    print(f"Hi {Sty.cus + username + Sty.clr},")
    print("Enter the corrosponding option's number, example: 1.")
    print("You will score 100 points for all correct answers.")
    print("Your final score will be added to the leaderboard.")
    print("You will be given an option to view the leaderboard at the end.\n")
    input("Press Enter to continue...")


def ask_questions(question_index, score):
    """
    Display next questions (if any left) using display question function.
    User get answer function to get the user input and to ensure it is valid.
    If answer is correct; points will be added, the user will be alerted &
    points will be displayed.
    If answer is wrong; the user will be altered and the correct answer &
    the user's score will be displayed.

    Args:
        - question_index (int): Is used to keep track of the questions asked &
        to display correct question and corrosponding options. It is used to
        check the answer to see if any additional questions are remaining.
        - score(int): The score is updated and displayed after each question.
    """
    while question_index < len(QUESTIONS):
        display_question(question_index)
        answer = get_answer(question_index)
        current_question = QUESTIONS[question_index]
        if int(answer) == current_question["answer"]:
            score += 100
            os.system("clear")
            print(Sty.pos)
            print(Ascii.wellDone)
            print("Well done, you answered correctly & scored 100 points!")
            print(f"Your current score is: {score}.")
        else:
            print(Sty.neg)
            print("Your answer was incorrect.")
            print(f"The correct answer was: {current_question['answer']}.")
            print("\nYou didn't score any points this round.")
            print(f"Your current score is: {score}.")
        question_index += 1
        print(Sty.clr)
        input("Press Enter to continue...")
    return score


def display_question(question_index):
    """
    Display question the question and each of the corrosponding options.

    Args:
        question_index (int): This value is used to determine what question
        should be displayed to the user.
    """
    current_question = QUESTIONS[question_index]
    os.system("clear")
    print(Sty.hdr +
          f"Question {1+question_index} of {len(QUESTIONS)}\n" + Sty.clr)
    print(Sty.que + f"{current_question['question']}\n")
    print("Please select your answer:")
    options = current_question['options']
    for option in options:
        print(f"    {option}")
    print(Sty.clr + "")


def get_answer(question_index):
    """
    Requests user input for answer to question.
    Calls the validate answer function to ensure that the
    user's input is numeric and within the required range.

    Args:
        question_index (int): This value is used to ensure that the quiz
        checks that the number input by the user is within the number of
        options that the corrosponding question has.

    Returns:
        Returns the user's answer if valid.
    """
    while True:
        answer = input("Please enter the corrosponding number here:\n")
        if validate_answer(answer, question_index):
            break
    return answer


def validate_answer(answer, question_index):
    """
    Check user input for answer is numeric.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        Returns True if answer is valid, otherwise False.
    """
    # top = 1+len(QUESTIONS(question_index[options])) THIS IS WRONG!!!
    # Update top and replace both 4 with top below.
    while answer.isnumeric() is False or int(answer) > 4 or int(answer) < 1:
        print(Sty.neg + f"\nYou input: {answer}.\n" + Sty.clr)
        print(f'You must enter a number between 1 and {4}, eg: "1".')
        return False
    return True


def dispay_final_result(score):
    """
    Prints ASCII header.
    Display user's result.
    Print different result message based on user's score.

    Args:
        score (int): The score is displayed to the user
        and used to calculate what result message is displayed.
    """
    os.system("clear")
    print(Ascii.theEnd)
    print("\nCongratulations on making it to the end of the quiz!\n")
    if score == len(QUESTIONS) * 100:
        print(Sty.pos +
              "Well done, you answered ALL of the questions correctly!!")
    elif score > len(QUESTIONS) * 50:
        print(Sty.pos +
              "Well done, you answered over half of the questions correctly!")
    elif score == len(QUESTIONS) * 50:
        print(Sty.neu + "You answered half of the questions correctly.")
    else:
        print(Sty.neg +
              "You didn't do very well... better luck next time!")
    print(Sty.clr)
    """
    def custom(value):
        print(Sty.cus + value + Sty.clr)

    print(f"\nYour final score is {custom(score)} out of {custom(total_qs)}.")
    """
    total_qs = len(QUESTIONS) * 100
    print(f"Your final score is {score} out of {total_qs}.\n")
    input("Press Enter to continue...")


def update_spreadsheet(score, name):
    """
    Update users name and final result to spreadsheet.
    Prints ASCII "Saved" header.
    Print name and score to verify.

    Args:
        score (int): The user's score is added to the sheet.
        name (str): The user's name is added to the sheet.

    """
    os.system("clear")
    score_tracker = SHEET.worksheet("ScoreTracker")
    result = [name, score]
    score_tracker.append_row(result)
    print(Ascii.saved)
    print(f"Your username: {name} and score: {score} has been saved.")


def get_show_leaders():
    """ Get user input to show leaderboard or terminate quiz """
    print("Would you like to see the high score leaderboard?")
    while True:
        show_leaders = input('Enter "y" to view leaders or "n" to end quiz:\n')
        if y_or_n(show_leaders):
            return show_leaders
        else:
            os.system("clear")
            print(Sty.neg +
                  f'You entered "{show_leaders}", you must enter: "y" or "n"'
                  + Sty.clr)


def y_or_n(value):
    """ Returns y or n value for user input """
    return value.lower() in ['y', 'n']


def show_leaderboard():
    """
    Prints ASCII "Leaderboard" header.
    Requests input from user to show leaderboard.
    Show leaderboard with header if requested by user,
    skip leaderboard if requested by user and end quiz with header text,
    or request valid input from user.
    """
    leader_board = SHEET.worksheet("LeaderBoard")
    leaders = leader_board.get_all_values()

    def ascii_leaderboard():
        print(Ascii.leaderboard)
    ascii_leaderboard()
    print("Would you like to see the high score leaderboard?")
    show_leaders = input('Enter "y" (yes) or "n" (no) here:\n')
    if show_leaders.lower() == "y":
        os.system("clear")
        ascii_leaderboard()
        for leader in leaders:
            print(f"{leader}")
        input("Press Enter to continue...")
        return True
    else:
        terminate_quiz()
        return True


def terminate_quiz():
    """ Displays a messeage with ascii art to alert the user that the quiz
    has been termininated """
    os.system("clear")
    print(Ascii.gameOver)
    print('\nYou can restart the quiz by clicking on the')
    print('"Run Program" button above the terminal.')
