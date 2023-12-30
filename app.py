from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey, personality_quiz, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "requin"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_start():
    """Show simple start page for survey"""
    return render_template("start.html", current_survey = satisfaction_survey)




# 19 create start page and style it
# 18 create question route
# 17 create question page and style it
# 16 handle incoming form data (POST)
# 15 create thank you route 
# 14 redirect to thank you when questions are complete
# 13 create thank you page and style it
# 12 change view function to check that it is the right quuestion page and redirect as necessary
# 11 when all questions have been answered, any page should redirect to thank you page
# 10 use flash message to tell user they are trying to access an invalid question when they try to go out of order
# 9 make the system able to handle more than one survey
# 8 make a new survey so that there are three
# 7 allow comments for some questions
# 6 create nicer thank you page with answers & comments shown
# 5 prevent resubmission of a survey with a cookie
# 4 add Bootstrap to the site
# 3 allow users to skip questions
# 2 allow users to go back to previously answered questions and change the answer
# 1 make a web interface to allow users to create surveys through the web and adding them to the system

# December 30th, 2023 - 