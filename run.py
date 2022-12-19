""" Python Quiz """
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
    """
    while True:
        print("Please enter your username.")
        print("Your username must be between 2 and 8 letters. Example: Tony\n")
        username = input("Enter your username here:\n")
        if validate_username_length(username):
            if validate_username_isalpha(username):
                break
    return username


def validate_username_length(username):
    """
    Validate username input is correct length.
    """
    try:
        if len(username) > 8 or len(username) < 2:
            raise ValueError(
                f"""Username must be between 2 & 8 letters,
                you provided {len(username)} letter(s)""")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_username_isalpha(username):
    """
    Validate username input is alphabetical.
    """
    try:
        if username.isalpha() is False:
            raise ValueError("Username may only include alphabetic letters")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def display_instructions(username):
    """
    Displays validated username and instructions.
    """
    print(f"\nHi {username}, please select your answer.")
    print("Enter the corrosponding option's number, example: 1")
    print("You will score 100 points for all correct answers.")
    print("Your final score will be added to the leaderboard.")
    print("Note: When asked to choose y or n, y = yes & n = no.\n")


def display_question(question_index):
    """
    Display question, options and input box for user.
    """
    current_question = QUESTIONS[question_index]
    print(f"{current_question['question']}\n")
    options = current_question['options']
    for option in options:
        print(f"    {option}")
    print("")


def get_answer(question_index):
    """
    Requests user input for answer.
    Validates input is numeric and within the required range.
    """
    while True:
        answer = input("Please enter option number for your answer here:\n")
        if validate_answer_isnumeric(answer):
            if validate_answer_in_range(answer, question_index):
                break
    return answer


def validate_answer_isnumeric(answer):
    """
    Check user input for answer is numeric.
    """
    try:
        if answer.isnumeric() is False:
            raise ValueError(
                f"Your input ({answer}) was not a number, it must be a number")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_answer_in_range(answer, question_index):
    """
    Check user input for answer is in range,
    ie. between 1 and quantity of options.
    """
    try:
        if int(answer) > (1+len(QUESTIONS[question_index])) or int(answer) < 1:
            max_num = 1+len(QUESTIONS[question_index])
            raise ValueError(
                f"You must select a number between 1 and {max_num}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def dispay_final_result(score):
    """
    Display user's result.
    Print different result message based on user's score.
    """
    print("Congratulations on making it to the end of the quiz!")
    print(f"Your final score is {score} out of {len(QUESTIONS) * 100} \n")
    if score > len(QUESTIONS) * 50:
        print("Well done, you answered over half of the questions correctly!")
    elif score == len(QUESTIONS) * 50:
        print("You answered half of the questions correctly.")
    else:
        print("Over half of your answers were wrong, better luck next time!")


def update_spreadsheet(score, name):
    """
    Update users name and final result to spreadsheet.
    Print name and score to verify.
    """
    score_tracker = SHEET.worksheet("ScoreTracker")
    result = [name, score]
    score_tracker.append_row(result)
    print(f"\nYour username: {name} and score: {score} has been saved.\n")


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
    show_leaders = input("Enter y or n here:\n")
    if show_leaders.lower() == "y":
        print("\nThe leader board is below:")
        for leader in leaders:
            print(f"{leader}")
        print("")
        return True
    elif show_leaders.lower() == "n":
        print("\nOK, you have chosen not to view the leaderboard.\n")
        return True
    else:
        print(f'You entered "{show_leaders}", you must enter: "y" or "n"')
        show_leaderboard()
        return False


def restart_quiz():
    """
    Request input from user to restart quiz.
    Restart quiz if requested by user,
    end quiz if requested by user,
    or request valid input from user.
    """
    restart = input("Would you like to try again? Please enter y or n:\n")
    if restart.lower() == "y":
        main()
        return True
    elif restart.lower() == "n":
        print("\nOK, you have chosen to close the quiz, try again later!\n")
        return True
    else:
        print(f'You entered "{restart}", you must enter: "y" or "n"')
        restart_quiz()
        return False


def main():
    """
    Run all functions for quiz.
    ..continue to ask next question until there are no more questions left.
    Update score and question index after each answer.
    """
    score = 0
    question_index = 0
    print("Get ready to start the Quiz!\n")
    name = get_username()
    display_instructions(name)
    while question_index < len(QUESTIONS):
        display_question(question_index)
        answer = get_answer(question_index)
        current_question = QUESTIONS[question_index]
        if int(answer) == current_question["answer"]:
            score += 100
            print("\nWell done, you answered correctly & scored 100 points!")
            print(f"Your current score is: {score}.\n")
        else:
            print("\nYour answer was incorrect.")
            print(f"The correct answer was: {current_question['answer']}.")
            print("You didn't score any points this round. ")
            print(f"Your current score is: {score}.\n")
        question_index += 1
    dispay_final_result(score)
    update_spreadsheet(score, name)
    show_leaderboard()
    restart_quiz()


main()
