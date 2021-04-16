from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey
response_list = 'responses'
app = Flask(__name__)
app.config['SECRET_KEY']= 'hello'
debug = DebugToolbarExtension(app)




@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/start', methods = ['POST'])
def start_survey():
    session[response_list] = []
    return redirect('/questions/0')

@app.route('/answer', methods = ['GET','POST'])
def answers():
    responses = session.get(response_list)
    answer_yes = request.form.get('yes')
    answer_no = request.form.get('no')
    if answer_yes:
        response = session[response_list]
        response.append(answer_yes)
        session[response_list] = response
    elif answer_no:
        response = session[response_list]
        response.append(answer_no)
        session[response_list] = response
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thankyou')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/questions/0')
def question1():
    questions = satisfaction_survey.questions
    return render_template('question1.html', questions=questions)


@app.route('/questions/1')
def question2():
    questions = satisfaction_survey.questions
    
    return render_template('question2.html', questions=questions)


@app.route('/questions/2')
def question3():
    questions = satisfaction_survey.questions
    
    return render_template('question3.html', questions=questions)



@app.route('/questions/3')
def question4():
    questions = satisfaction_survey.questions
    
    return render_template('question4.html', questions=questions)



@app.route('/thankyou')
def thank_you():
    responses = session.get(response_list)
    return render_template('thank_you.html', responses=responses)
    


   
