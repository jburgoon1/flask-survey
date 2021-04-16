from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']= 'hello'
debug = DebugToolbarExtension(app)




@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/start', methods = ['POST'])
def start_survey():
    session['response'] = []
    return redirect('/questions/1')

@app.route('/questions/1')
def question1():
    questions = satisfaction_survey.questions
    return render_template('question1.html', questions=questions)

@app.route('/questions/add1', methods=['GET','POST'])
def add_answer1():
    answer_yes = request.form.get('yes')
    answer_no = request.form.get('no')
    if answer_yes:
        response_list = session['response']
        response_list.append(answer_yes)
        session['response'] = response_list
    elif answer_no:
        response_list = session['response']
        response_list.append(answer_no)
        session['response'] = response_list
    
    return redirect('/questions/2')


@app.route('/questions/2')
def question2():
    questions = satisfaction_survey.questions
    
    return render_template('question2.html', questions=questions)

@app.route('/questions/add2', methods=['POST'])
def add_answer2():
    answer_yes = request.form.get('yes')
    answer_no = request.form.get('no')
    if answer_yes:
        response_list = session['response']
        response_list.append(answer_yes)
        session['response'] = response_list
    elif answer_no:
        response_list = session['response']
        response_list.append(answer_no)
        session['response'] = response_list
    return redirect('/questions/3')

@app.route('/questions/3')
def question3():
    questions = satisfaction_survey.questions
    
    return render_template('question3.html', questions=questions)

@app.route('/questions/add3', methods=['POST'])
def add_answer3():
    answer_yes = request.form.get('yes')
    answer_no = request.form.get('no')
    if answer_yes:
        response_list = session['response']
        response_list.append(answer_yes)
        session['response'] = response_list
    elif answer_no:
        response_list = session['response']
        response_list.append(answer_no)
        session['response'] = response_list
    return redirect('/questions/4')

@app.route('/questions/4')
def question4():
    questions = satisfaction_survey.questions
    
    return render_template('question4.html', questions=questions)

@app.route('/questions/add4', methods=['POST'])
def add_answer4():
    answer_yes = request.form.get('yes')
    answer_no = request.form.get('no')
    if answer_yes:
        response_list = session['response']
        response_list.append(answer_yes)
        session['response'] = response_list
    elif answer_no:
        response_list = session['response']
        response_list.append(answer_no)
        session['response'] = response_list
    return redirect('/thankyou')


@app.route('/thankyou')
def thank_you():
    return render_template('thank_you.html', response_list=session['response'])
    


   
