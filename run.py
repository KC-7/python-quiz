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
# current_question = question_index

# print(f"Score Tracker:\n{scores}")
# print(f"Leader Board:\n{leaders}")

QUESTIONS = [{
    "question": "Sample Question Text 1",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 1
},
{
    "question": "Sample Question Text 2",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 2
},
{
    "question": "Sample Question Text 3",
    "options": ["Option 1: QWERTY", "Option 2: QWERTY", "Option 3: QWERTY", "Option 4: QWERTY"],
    "answer": 3
},
{
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
        print("Get ready to start the Quiz!\nPlease enter your username.")
        print("Your username must be between 2 and 8 letters.\nExample: Tony\n")

        username = input("Enter your username here:\n")
                
        if validate_username_length(username):
            print("\nUsername is correct length.")
            if validate_username_isalpha(username):
                print("Username is alphabetical.\n")
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
    Call validate answer function once provided input by user. 
    """
    current_question = QUESTIONS[question_index]
    print(f"{current_question['question']}\n")
    options = current_question['options']
    for option in options:
        print(f"{option}\n")
    
    get_answer()



def get_answer():
    while True:
        answer = input("Please enter option number for your answer here: ")
        if validate_answer_in_range(answer):
            print("Your input has passed initial validation checks")
            if validate_answer_isnumeric(answer):
                print("Your input has passed final validation checks")
                check_answer(answer)
                break

    return answer

def validate_answer_in_range(answer):
    """
    Check user input for answer is in range, ie. between 1 and quantity of options.
    """
    try:
        if int(answer) > 4 or int(answer) < 1:
            raise ValueError(
            f"You must select a number between 1 and 4"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def validate_answer_isnumeric(answer):
    """
    Check user input for answer is numeric.
    """
    try:
        if answer.isnumeric() == False:
            raise ValueError(
            f"Your input was not a number, the answer must be a number"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True
    

def check_answer(answer):
    current_question = QUESTIONS[question_index]
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