from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, personality_quiz, reading_survey, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "requin"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def show_survey_options():
    """Show survey options"""
    return render_template("options.html", surveys=surveys)

@app.route('/set-survey', methods=["POST"])
def set_survey():
    """set selected survey and route to survey start page"""
    session['choice'] = request.form['choice']
    if session.get(session['choice']):
        flash("You have already completed this survey! Thank you.", 'error')
        return redirect('/thankyou')
    return redirect('/survey-start')

@app.route('/survey-start')
def show_start():
    """Show simple start page for survey"""
    return render_template("start.html", current_survey =  surveys[session["choice"]])

@app.route('/reset-responses', methods=["POST"])
def start_survey():
    """reset responses list and route to first survey question"""
    session["responses"] = []
    session["comments"] = []
    return redirect('/questions/0')

@app.route('/questions/<number>')
def show_question(number):
    """Show the appropriately number question and answer options"""
    number = int(number)
    responses = session['responses']
    if len(responses) == len(surveys[session["choice"]].questions):
        flash("You have already completed this survey! Thank you.", 'error')
        return redirect('/thankyou')
    if number != len(responses):
        next_number = len(responses)
        flash("You are trying to access an invalid question. Please answer this question.", 'error')
        return redirect(f'/questions/{next_number}') 
    return render_template("question.html", current_survey = surveys[session["choice"]], number = number)

@app.route('/answer/<number>', methods=["POST"])
def collect_answer(number):
    """Add the answer to the responses list"""
    number = int(number)
    responses = session['responses']
    responses.append(request.form['response'])
    session['responses'] = responses
    comments = session['comments']
    if surveys[session["choice"]].questions[number].allow_text: 
        comments.append(request.form['comment'])
    else:
        comments.append('')
    session['comments'] = comments
    next_number = len(responses)
    if next_number >= len(surveys[session["choice"]].questions):
        return redirect('/thankyou')
    else: 
        return redirect(f'/questions/{next_number}')

@app.route('/thankyou')
def show_thank_you():
    """Show thank you message upon survey completion"""
    length = len(surveys[session["choice"]].questions)
    session[session['choice']] = True
    return render_template("thankyou.html", current_survey = surveys[session["choice"]], length = length)

# 3 allow users to skip questions
# 2 allow users to go back to previously answered questions and change the answer
# 1 make a web interface to allow users to create surveys through the web and add them to the system

# December 30th, 2023 - 