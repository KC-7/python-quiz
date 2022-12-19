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
    "question": "Sample Question Text 1",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 1
}, {
    "question": "Sample Question Text 2",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 2
}, {
    "question": "Sample Question Text 3",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 3
}, {
    "question": "Sample Question Text 4",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 4
}]


def get_username():
    """
    Get username input from user.
    Run a while loop to ensure username is submited correctly,
    must be a string between 2 and 8 letters. Loop will repeat
    until the username is valid.
    Calls function to display instructions when input valid.
    """
    while True:
        print("Please enter your username.")
        print("Your username must be between 2 and 8 letters.\nExample: Tony\n")
        username = input("Enter your username here: ")
        if validate_username_length(username):
            # print("\nUsername is correct length.")
            if validate_username_isalpha(username):
                # print("Username is alphabetical.\n")
                break
    return username


def validate_username_length(username):
    """
    Validate username input is correct length.
    """
    try:
        if len(username) > 8 or len(username) < 2:
            raise ValueError(
                f"Username must be between 2 & 8 letters, you provided {len(username)} letter(s)")
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
    Calls function to show next question.
    """
    print(f'Hi {username}, please select your answer by entering the corrosponding option number, example: "1"')
    print("You will score 100 points for all correct answers. Your final score will be added to the leader board at the end of the quiz.\n")
    # pass


def display_question(question_index):
    """
    Display question, options and input box for user.
    Call validate answer function once provided input by user.
    """
    current_question = QUESTIONS[question_index]
    print(f"{current_question['question']}\n")
    options = current_question['options']
    for option in options:
        print(f"{option}\n")


def get_answer(question_index):
    """
    Requests user input for answer.
    Validates input is numeric and within the required range.
    """
    while True:
        answer = input("Please enter option number for your answer here: ")
        if validate_answer_isnumeric(answer):
            # print("Your input is a number as required.")
            if validate_answer_in_range(answer, question_index):
                # print("Your input is within the required range.")
                # check_answer(answer)
                break
    return answer


def validate_answer_isnumeric(answer):
    """
    Check user input for answer is numeric.
    """
    try:
        if answer.isnumeric() == False:
            raise ValueError(
            f"Your input ({answer}) was not a number, the answer must be a number"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_answer_in_range(answer, question_index):
    """
    Check user input for answer is in range, ie. between 1 and quantity of options.
    """
    try:
        if int(answer) > (1+len(QUESTIONS[question_index])) or int(answer) < 1:
            raise ValueError(
                f"You must select a number between 1 and {1+len(QUESTIONS[question_index])}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def dispay_final_result(score):
    """
    Display user's result.
    Print different result message based on user's score.
    """
    print("Congratulations on making it to the end, you have completed the quiz!")
    print(f"Your final score is {score} out of {len(QUESTIONS) * 100} \n")
    if score > len(QUESTIONS) * 50:
        print("Well done, you answered over half of the questions correctly!")
    if score == len(QUESTIONS) * 50:
        print("You got half of the answers correct, could be better, could be worse!")
    else:
        print("You answered under half of the questions correctly, better luck next time!")


def update_spreadsheet(score, name):
    """
    Update users name and final result to spreadsheet
    Print name and score to verify
    """
    score_tracker = SHEET.worksheet("ScoreTracker")
    # scores = score_tracker.get_all_values()
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
    show_leaders = input("Would you like to see the leaderboard? Enter y or n here: ")
    if show_leaders == "y":
        print("The leader board is below:")
        for leader in leaders:
            print(f"{leader}")
        print("")
        return True
    if show_leaders == "n":
        print("OK, you have chosen not to view the leaderboard.\n")
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
    restart = input("Try again? Please enter y or n: ")
    if restart == "y":
        main()
        return True
    if restart == "n":
        print("OK, you have chosen to close the quiz, feel free to try again later!\n")
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
            print("Well done, you answered correctly. You scored 100 points!")
            print(f"Your current score is: {score}.\n")
        else:
            print(f"Your answer was incorrect, the correct answer was: {current_question['answer']}.")
            print(f"You didn't score any points this round. Your current score is: {score}.\n")
        question_index += 1
    dispay_final_result(score)
    update_spreadsheet(score, name)
    show_leaderboard()
    restart_quiz()


main()
