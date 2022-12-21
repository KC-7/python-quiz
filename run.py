""" Python Quiz """
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz')


QUESTIONS = [{
    "question": "What is largest of the below file sizes?",
    "options": [
        "Option 1: 1TB", "Option 2: 1MB",
        "Option 3: 1GB", "Option 4: 1KB"],
    "answer": 1
}, {
    "question": "How much did the first computer weigh?",
    "options": [
        "Option 1: 27 grams", "Option 2: 27 ton",
        "Option 3: 27 pounds", "Option 4: 27 stone"],
    "answer": 2
}, {
    "question": "The first known computer programmer was a:",
    "options": [
        "Option 1: dog", "Option 2: man",
        "Option 3: woman", "Option 4: teenager"],
    "answer": 3
}, {
    "question": "How much did the first 1GB hard drive cost?",
    "options": [
        "Option 1: $400", "Option 2: $4,000,000",
        "Option 3: $4,000", "Option 4: $40,000"],
    "answer": 4
}]


def get_username():
    """
    Get username input from user.
    Run a while loop to ensure username is submited correctly,
    must be a string between 2 and 8 letters. Loop will repeat
    until the username is valid.

    Returns:
        Returns the username if the user's input is valid.
    """
    os.system("clear")
    while True:
        print("Please enter your username.")
        print("Your username must be between 2 and 8 letters. Example: Tony\n")
        username = input("Enter your username here:\n")
        if validate_username(username):
            break
    return username


def validate_username(username):
    """
    Validate username input is correct length.

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
        print("Your username must be alabetical.")
        print("Your username must be between 2 & 8 letters in length.")
        print(f'You entered: "{username}", this is {name_len} character(s).\n')
        return False
    return True


def display_instructions(username):
    """
    Displays validated username and instructions.

    Args:
        username (str): This value is displayed to the user in the
        instructions text to improve UX.
    """
    os.system("clear")
    print(f"Hi {username},")
    print("Enter the corrosponding option's number, example: 1")
    print("You will score 100 points for all correct answers.")
    print("Your final score will be added to the leaderboard.")
    print("Note: When asked to choose y or n, y = yes & n = no.\n")
    input("Press Enter to continue...")


def display_question(question_index):
    """
    Display question the question and each of the corrosponding options.

    Args:
        question_index (int): This value is used to determine what question
        should be displayed to the user.
    """
    os.system("clear")
    current_question = QUESTIONS[question_index]
    print(f"Question {1+question_index} of {len(QUESTIONS)}\n")
    print(f"{current_question['question']}\n")
    print("Please select your answer:")
    options = current_question['options']
    for option in options:
        print(f"    {option}")
    print("")


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
    top = 1+len(QUESTIONS[question_index])
    while answer.isnumeric() is False or int(answer) > top or int(answer) < 1:
        print(f"\nYou input: ({answer}).")
        print(f'You must enter a number between 1 and {top}, eg: "1".\n')
        return False
    return True


def dispay_final_result(score):
    """
    Display user's result.
    Print different result message based on user's score.

    Args:
        score (int): The score is displayed to the user
        and used to calculate what result message is displayed.
    """
    os.system("clear")
    print("Congratulations on making it to the end of the quiz!")
    print(f"Your final score is {score} out of {len(QUESTIONS) * 100} \n")
    if score > len(QUESTIONS) * 50:
        print("Well done, you answered over half of the questions correctly!")
    elif score == len(QUESTIONS) * 50:
        print("You answered half of the questions correctly.")
    else:
        print("Over half of your answers were wrong, better luck next time!")
    print("")
    input("Press Enter to continue...")


def update_spreadsheet(score, name):
    """
    Update users name and final result to spreadsheet.
    Print name and score to verify.

    Args:
        score (int): The user's score is added to the sheet.
        name (str): The user's name is added to the sheet.

    """
    os.system("clear")
    score_tracker = SHEET.worksheet("ScoreTracker")
    result = [name, score]
    score_tracker.append_row(result)
    print(f"Your username: {name} and score: {score} has been saved.\n")


def show_leaderboard():
    """
    Request input from user to show leaderboard.
    Show leaderboard if requested by user,
    skip leaderboard if requested by user,
    or request valid input from user.
    """
    leader_board = SHEET.worksheet("LeaderBoard")
    leaders = leader_board.get_all_values()
    print("Would you like to see the high score leaderboard?")
    show_leaders = input('Enter "y" (yes) or "n" (no) here:\n')
    if show_leaders.lower() == "y":
        os.system("clear")
        print("The leader board is below:")
        for leader in leaders:
            print(f"{leader}")
        print('\nYou can restart by clicking on the "Run Program" button.\n')
        return True
    elif show_leaders.lower() == "n":
        os.system("clear")
        print("OK, you have chosen to terminate the quiz.")
        print('\nYou can restart the quiz by clicking on the')
        print('"Run Program" button above the terminal.\n')
        return True
    else:
        print(f'\nYou entered "{show_leaders}", you must enter: "y" or "n"')
        show_leaderboard()
        return False


def main():
    """
    Run all functions for quiz.
    ..continue to ask the next question until there are no more questions left.
    Update score and question index after each answer.
    """
    score = 0
    question_index = 0
    print("Get ready to start the quiz!\n")
    name = get_username()
    display_instructions(name)
    while question_index < len(QUESTIONS):
        display_question(question_index)
        answer = get_answer(question_index)
        current_question = QUESTIONS[question_index]
        if int(answer) == current_question["answer"]:
            score += 100
            os.system("clear")
            print("Well done, you answered correctly & scored 100 points!")
            print(f"Your current score is: {score}.\n")
        else:
            print("\nYour answer was incorrect.")
            print(f"The correct answer was: {current_question['answer']}.")
            print("\nYou didn't score any points this round.")
            print(f"Your current score is: {score}.\n")
        input("Press Enter to continue...")
        question_index += 1
    dispay_final_result(score)
    update_spreadsheet(score, name)
    show_leaderboard()


main()
