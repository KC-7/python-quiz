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

# print(f"Score Tracker:\n{scores}")
# print(f"Leader Board:\n{leaders}")

def get_username():
    """
    Get username input from user. 
    Run a while loop to ensure username is submited correctly, 
    must be a string between 2 and 8 letters. Loop will repeat
    until the username is valid.
    """
    while True:
        print("Please enter your username.")
        print("Your username must be between 2 and 10 characters.")
        print("Example: Tony55\n")

        username = input("Enter your username here:\n")
                
        if validate_username_length(username):
            print("Username is correct length.")
            break

    return username

def validate_username_length(username):
    """
    Validate username input.
    """
    try:
        if len(username) > 10 or len(username) < 2:
            raise ValueError(
                f"Username must be between 2 & 8 characters, you provided {len(username)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

"""
def validate_username_isalpha(username):
    try:
        if isalpha(username) == False:
            raise ValueError(
            f"Username may only include alphabetic letters."
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True
"""

get_username()