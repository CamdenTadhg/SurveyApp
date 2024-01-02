from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "requin"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def show_start():
    """Show simple start page for survey"""
    return render_template("start.html", current_survey = satisfaction_survey)

@app.route('/start-survey', methods=["POST"])
def start_survey():
    """reset responses list and route to first survey question"""
    session["responses"] = []
    return redirect('/questions/0')

@app.route('/questions/<number>')
def show_question(number):
    """Show the appropriately number question and answer options"""
    number = int(number)
    responses = session['responses']
    if len(responses) == len(satisfaction_survey.questions):
        flash("You have already completed this survey! Thank you.", 'error')
        return redirect('/thankyou')
    if number != len(responses):
        next_number = len(responses)
        flash("You are trying to access an invalid question. Please answer this question.", 'error')
        return redirect(f'/questions/{next_number}') 
    return render_template("question.html", current_survey = satisfaction_survey, number = number)

@app.route('/answer', methods=["POST"])
def collect_answer():
    """Add the answer to the responses list"""
    responses = session['responses']
    responses.append(request.form['response'])
    session['responses'] = responses
    print('*****************')
    print(session["responses"])
    print('*****************')
    next_number = len(responses)
    if next_number >= len(satisfaction_survey.questions):
        return redirect('/thankyou')
    else: 
        return redirect(f'/questions/{next_number}')

@app.route('/thankyou')
def show_thank_you():
    """Show thank you message upon survey completion"""
    print('*****************')
    print(session["responses"])
    print('*****************')
    return render_template("thankyou.html", current_survey = satisfaction_survey)

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