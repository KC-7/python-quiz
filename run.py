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

print(f"Score Tracker:\n{scores}")
print(f"Leader Board:\n{leaders}")