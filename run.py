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

score_tracker = SHEET.worksheet("ScoreTracker")
leader_board = SHEET.worksheet("LeaderBoard")

scores = score_tracker.get_all_values()
leaders = leader_board.get_all_values()

question_index = 0

# print(f"Score Tracker:\n{scores}")
# print(f"Leader Board:\n{leaders}")

QUESTIONS = [{
    "question": "Sample Question Text",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 1
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
        print("Your username must be between 2 and 8 letters.")
        print("Example: Tony\n")

        username = input("Enter your username here:\n")
                
        if validate_username_length(username):
            print("Username is correct length.")
            if validate_username_isalpha(username):
                print("Username is alphabetical.")
                display_instructions(username)
                break

    return username


def validate_username_length(username):
    """
    Validate username input.
    """
    try:
        if len(username) > 8 or len(username) < 2:
            raise ValueError(
                f"Username must be between 2 & 8 characters, you provided {len(username)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_username_isalpha(username):
    try:
        if username.isalpha() == False:
            raise ValueError(
            f"Username may only include alphabetic letters"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def display_instructions(username):
    """
    Displays validated username and instructions.
    Calls function to show next question.
    """
    print(f"Hi {username}, your username is valid.\nPlease select your answer by entering the corrosponding option number, example: 1\n")
    display_question(question_index)
    pass

def display_question(question_index):
    """
    Display question, options and input box for user.
    """
    current_question = QUESTIONS[question_index]
    print(f"{current_question['question']}\n")
    options = current_question['options']
    for option in options:
        print(f"{option}\n")

    answer = input("Please enter option number for your answer here: ")

    if int(answer) == current_question["answer"]:
        print("You answered correctly")
    else:
        print(f"Your answer was incorrect, the correct answer was: {current_question['answer']}")


def main():
    """
    Run all functions
    """
    get_username()
    

main()