""" Python Quiz """
import os
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz')


class Sty:
    """
    Colorama commands are used to create style classes that can be
    applied to the terminal text in a short hand format to reduce
    line sizes.
    """
    clr = Style.RESET_ALL  # Clear
    pos = Fore.GREEN  # Positive - Bright Green Text
    neg = Fore.RED  # Negative - Red Text
    neu = Fore.YELLOW  # Neutral = Yellow Text
    log = Fore.MAGENTA + Back.CYAN  # Logo - Magenta Text, Cyan BG
    hdr = Fore.MAGENTA  # Header - Magenta Text
    que = Fore.CYAN  # Question - Cyan Text
    cus = Fore.MAGENTA  # Custom - Magenta Text
    inv = Fore.BLACK + Back.WHITE  # Inverted - Black Text, White BG


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
}, {
    "question": "How are computers powered?",
    "options": [
        "Option 1: Electricity", "Option 2: Potatos", "Option 3: Onions"],
    "answer": 1
}, {
    "question": "How many computer viruses are released each month?",
    "options": [
        "Option 1: 60", "Option 2: 600",
        "Option 3: 6,000", "Option 4: 60,000",
        "Option 5: 600,000", "Option 6: 6,000,000"],
    "answer": 3
}]


def welcome():
    """
    Welcome screen for user.
    Displays Ascii text with logo styling.
    """
    os.system("clear")
    print("Welcome To:\n")
    print(Sty.log + """                                       |
    ██╗  ██╗  ██████╗  ███████╗        |
    ██║ ██╔╝ ██╔════╝  ╚════██║        |
    █████╔╝  ██║   █████╗  ██╔╝        |
    ██╔═██╗  ██║   ╚════╝ ██╔╝         |
    ██║  ██╗ ╚██████╗     ██║          |
    ╚═╝  ╚═╝  ╚═════╝     ╚═╝          |
                                       |
    ██████╗   ██╗   ██╗ ██╗ ███████╗   |
    ██╔═══██╗ ██║   ██║ ██║ ╚══███╔╝   |
    ██║   ██║ ██║   ██║ ██║   ███╔╝    |
    ██║▄▄ ██║ ██║   ██║ ██║  ███╔╝     |
    ╚██████╔╝ ╚██████╔╝ ██║ ███████╗   |
     ╚══▀▀═╝   ╚═════╝  ╚═╝ ╚══════╝   |""" + Sty.clr)
    print("\nGet ready to start the quiz!\n")
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
    print(Sty.hdr + """     _____
    |  |  | ___  ___  ___  ___  ___  _____  ___
    |  |  ||_ -|| -_||  _||   || .'||     || -_|
    |_____||___||___||_|  |_|_||__,||_|_|_||___|
    """ + Sty.clr)
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
        print(Sty.hdr + """         _____
        |  |  | ___  ___  ___  ___  ___  _____  ___
        |  |  ||_ -|| -_||  _||   || .'||     || -_|
        |_____||___||___||_|  |_|_||__,||_|_|_||___|
        """ + Sty.clr)
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
    print(Sty.hdr + """     _____                _____         _____  _
    |  |  | ___  _ _ _   |_   _| ___   |  _  || | ___  _ _
    |     || . || | | |    | |  | . |  |   __|| || .'|| | |
    |__|__||___||_____|    |_|  |___|  |__|   |_||__,||_  |
                                                      |___|
    """ + Sty.clr)
    print(f"Hi {Sty.cus + username + Sty.clr},")
    print("Enter the corrosponding option's number, example: 1.")
    print("You will score 100 points for all correct answers.")
    print("Your final score will be added to the leaderboard.")
    print("You will be given an option to view the leaderboard at the end.\n")
    input("Press Enter to continue...")


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
    print(Sty.inv + """
            _____  _           _____         _              |
           |_   _|| |_  ___   |   __| ___  _| |             |
             | |  |   || -_|  |   __||   || . |             |
             |_|  |_|_||___|  |_____||_|_||___|             |
     __ __                   _____                      _   |
    |  |  | ___  _ _  ___   |   __| ___  ___  ___  ___ |_|  |
    |_   _|| . || | ||  _|  |__   ||  _|| . ||  _|| -_| _   |
      |_|  |___||___||_|    |_____||___||___||_|  |___||_|  |
                                                            |""" + Sty.clr)
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
    print(Sty.pos + """     _____                   _
    |   __| ___  _ _  ___  _| |
    |__   || .'|| | || -_|| . |
    |_____||__,| |_| |___||___|
    """ + Sty.clr)
    print(f"Your username: {name} and score: {score} has been saved.")


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
        print(Fore.YELLOW + """         __                 _            _
        |  |    ___  ___  _| | ___  ___ | |_  ___  ___  ___  _|"|  (|''|)
        |  |__ | -_|| .'|| . || -_||  _|| . || . || .'||  _|| . |   (  )
        |_____||___||__,||___||___||_|  |___||___||__,||_|  |___|   _)(_
        """ + Sty.clr)
    ascii_leaderboard()
    print("Would you like to see the high score leaderboard?")
    show_leaders = input('Enter "y" (yes) or "n" (no) here:\n')
    if show_leaders.lower() == "y":
        os.system("clear")
        ascii_leaderboard()
        for leader in leaders:
            print(f"{leader}")
        print('\nYou can restart by clicking on the "Run Program" button.')
        return True
    elif show_leaders.lower() == "n":
        os.system("clear")
        print("OK, you have chosen to terminate the app.")
        print(Sty.neg)
        print("""         _____                   _            _           _
        |_   _| ___  ___  _____ |_| ___  ___ | |_  ___  _| |
          | |  | -_||  _||     || ||   || .'||  _|| -_|| . |
          |_|  |___||_|  |_|_|_||_||_|_||__,||_|  |___||___|
            _____                     _____
           |   __| ___  _____  ___   |     | _ _  ___  ___
           |  |  || .'||     || -_|  |  |  || | || -_||  _|
           |_____||__,||_|_|_||___|  |_____| |_| |___||_|
        """ + Style.RESET_ALL)
        print('\nYou can restart the quiz by clicking on the')
        print('"Run Program" button above the terminal.')
        return True
    else:
        os.system("clear")
        print(Sty.neg +
              f'You entered "{show_leaders}", you must enter: "y" or "n"'
              + Sty.clr)
        show_leaderboard()
        return False


def main():
    """
    Run all functions for quiz in the below order.
    ..continue to ask the next question until there are no more questions left.
    Update score and question index after each answer and provide custom
    feedback with headers and class stlying.
    """
    score = 0
    question_index = 0
    welcome()
    name = get_username()
    display_instructions(name)
    while question_index < len(QUESTIONS):
        display_question(question_index)
        answer = get_answer(question_index)
        current_question = QUESTIONS[question_index]
        if int(answer) == current_question["answer"]:
            score += 100
            os.system("clear")
            print(Sty.pos)
            print("""            ██╗    ██╗███████╗██╗     ██╗
            ██║    ██║██╔════╝██║     ██║
            ██║ █╗ ██║█████╗  ██║     ██║
            ██║███╗██║██╔══╝  ██║     ██║
            ╚███╔███╔╝███████╗███████╗███████╗
            ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝

            ██████╗  ██████╗ ███╗   ██╗███████╗
            ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
            ██║  ██║██║   ██║██╔██╗ ██║█████╗
            ██║  ██║██║   ██║██║╚██╗██║██╔══╝
            ██████╔╝╚██████╔╝██║ ╚████║███████╗
            ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
            """)
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
    dispay_final_result(score)
    update_spreadsheet(score, name)
    show_leaderboard()


main()
