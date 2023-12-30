from flask import Flask, render_template, redirect, request
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

@app.route('/questions/<number>')
def show_question(number):
    """Show the appropriately number question and answer options"""
    number = int(number)
    return render_template("question.html", current_survey = satisfaction_survey, number = number)

@app.route('/answer', methods=["POST"])
def collect_answer():
    """Add the answer to the responses list"""
    answer = request.form['response']
    responses.append(answer)
    next_number = len(responses)
    if next_number >= len(satisfaction_survey.questions):
        return redirect('/thankyou')
    else: 
        return redirect(f'/questions/{next_number}')

@app.route('/thankyou')
def show_thank_you():
    """Show thank you message upon survey completion"""
    return render_template("thankyou.html", current_survey = satisfaction_survey)



# 4 create thank you page and style it
# 3 change view function to check that it is the right quuestion page and redirect as necessary
# 2 when all questions have been answered, any page should redirect to thank you page
# 1 use flash message to tell user they are trying to access an invalid question when they try to go out of order

# 10 store the answers in a session
# 9 make the system able to handle more than one survey
# 8 make a new survey so that there are three
# 7 allow comments for some questions
# 6 create nicer thank you page with answers & comments shown
# 5 prevent resubmission of a survey with a cookie
# 4 add Bootstrap to the site
# 3 allow users to skip questions
# 2 allow users to go back to previously answered questions and change the answer
# 1 make a web interface to allow users to create surveys through the web and add them to the system

# December 30th, 2023 - 