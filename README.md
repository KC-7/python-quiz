![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# KC-7's Quiz (built using Python)

This terminal quiz app was built using Python to demonstrate a wide range of different functions.
The quiz takes the user's name, provides a series of questions and options and provides a final result at the end of the quiz.
Each user input is validated to ensure the data is in the correct format.
A google spreadsheet is linked to the app to keep track of the usernames and scores, the info is sent on completion of the quiz. 
The user will be given an option to print the high scores leaderboard to the terminal at the end of the game. The high scores are sorted in the google spreadsheet.


## Live Links: 

* Heroku App: https://kc-quiz.herokuapp.com/
* Google Spreadsheet: https://docs.google.com/spreadsheets/d/1gO0uQxTMf_DukHugL-Vmi94pZnGUBhMNTlDku29Pp5s/edit?usp=sharing


## Technologies: 🌐 🛠 

- **Python** - was used to program the quiz  app. 

- **The Code Institute Python Template** - was used to create the terminal web app. 

- **GitPod** - is the platform used to develop the site. 

- **GitHub** - is used to host the files. 

- **Heroku** - was used to deploy and host the web app.  

- **Markdown** - is used to format the readme file. 

- **Google Sheets** - is used to save the username and score & to display the leaderboard. 


## How to play: 🎲 🎮

- The quiz application is terminal based. 
- The user must input the required information (such as username, answer and yes or no) into the terminal when requested.
- The quiz will validate user inputs as to avoid issues. 

- The user will be asked to enter their username at the start of the quiz, this will be validated to ensure the input is the correct length and alphabetical. If the input is invalid, an error will be shown and the user will be asked to enter their username again. 
- The first question and corrosponding options will be displayed to the user.
- The user will be asked to input the number of the corrosponding option they would like to select as their answer. 
- The user will be given an option to view the high score leaderboard. 
- The user will be shown the leader board if they select yes, if not they will skip to the next step. If the user's input is not valid, the question will be repeated. 
- The user will be given an option to restart the quiz.
- The user will be sent back to the start of the quiz if they select yes, if not the quiz will be terminated. If the user's input is not valid, the question will be repeated. 

## Features: 💻

⏹ 🔄 🔤 ❓ 🖱 🎰 ✅ ❌

### Welcome Screen 👋 ⏯

### Question Screen ❓ 🖱

### Result Screen 🎰 ✅ ❌

### End Screen ⏹ 🔄


### Future Features: 🆕

- **Additional difficulty levels** could be set up asking the user an array of more difficult questions. 💬


## Planning & Design ✍ 🆒

- The site was designed using Python. 

- The site was intially designed using the below flowchart with the view of implementing additional features:

<img style="display: inline; margin: 25px 35%" src="assets/readme-images/flowchart1.png" alt="Initial Flowchart" width="30%" height="auto" title="Initial Flowchart">

- The app was adjusted and I created the below flowchart to reflect: 

<img style="display: inline; margin: 25px 35%" src="assets/readme-images/flowchart2.png" alt="Updated Flowchart" width="30%" height="auto" title="Updated Flowchart">

- Additional changes were made and the **Final Flowchart** was updated again to reflect this:

<img style="display: inline; margin: 25px 15%" src="assets/readme-images/flowchart3.png" alt="Final Flowchart" width="70%" height="auto" title="Final Flowchart">

## Testing: 

### Test Cases 🕵

- [X] Page loads correctly 🌐 and displays Engine Start button ⏯ and Quiz Container.
- [x] Find out more collapsible window ⏬ works as intended: 
  - [x] Changes colour when hovering. 
  - [x] Changes text when displaying content. 
  - [x] QR Code is displayed within the collapsible window when over the specified screen width and is removed on devices with a smaller screen width.

### Solved Bugs: 🕵 🕷

I made some of the following changes during development to improve how the app functions: 

- XXX

- XXX

### Remaining Bugs: 🕵 🕷

I was not able to identify any further bugs during final testing. &#10004; 🐛 🐞 🦗

### Validator Testing: 🏸

## Deployment: 🌐

### GitPod: 🔧 ⌨

- I developed the site using Python in GitPod. 

- I tested the site during development by entering the following command into the terminal: 
    - *python3 run.py*

- For version control, I regularly updated my work to **GitHub** by entering the below commands into the terminal: 
    - *git add .*
    - *git commit -m "Update message here"*
    - *git push*

### Creating the Heroku app: 🌐 🖱

- I depolyed the app to Heroku by doing the following: 
    - XXXX
    - XXXX

## Credits: 🥂 🙏

- The Code Institute's Gitpod Pyhton Terminal Window Template was used as the initial template for this project.

- The walk through project I completed with the Code Insitute, <a href="https://github.com/KC-7/love-sandwiches" target="_blank" rel="noopener" aria-label="Link to The Code Institute Walkthrough Project, Love Maths (opens in new tab)">Love Sandwiches</a>, was a good source to reference for information such as the main function. 

- I learned how to implement colours by reading pypi.org's guide to importing and using Colorama - https://pypi.org/project/colorama/