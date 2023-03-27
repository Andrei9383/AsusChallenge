from flask import Flask, render_template, request, session
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pwd = os.getcwd()
        options = ['a', 'b', 'c', 'd']
        dataset = pd.read_csv(pwd + '/editedEtapa2.csv')

        # get every row from the second column and put it in a list
        list = dataset.iloc[:, 1].values

        # get every column from the third to the sixth, inclusive and put them grouped by 4 in a list
        list2 = dataset.iloc[:, 2:6].values

        # get every row from the last column and put it in a list
        list3 = dataset.iloc[:, -1].values

        # initialize session variables
        if 'index' not in session:
            session['index'] = 0
            session['rightAnswers'] = 0
            session['wrongAnswers'] = 0

        index = session['index']
        if index == len(list):
            return render_template('result.html', rightAnswers=session['rightAnswers'], wrongAnswers=session['wrongAnswers'])
        # check if answer is correct and update session variables
        # list2[index][options.index(answer)] == list3[index]
        

                
        # if session index is 0 , skip this part
        if index != 0:
            # check if answer is correct
            if list2[index][options.index(request.form.get('answer'))] == list3[index]:
                session['rightAnswers'] += 1
            else:
                session['wrongAnswers'] += 1


        # update index
        session['index'] += 1

        # check if all questions have been answered
        

        # get question and answers for current index
        question_text = str(index + 1) + "/" + str(len(list)) + ") " + list[index]
        answers_text = []
        for optionIndex, option in enumerate(options):
            # check for nan
            if not pd.isnull(list2[index][optionIndex]):
                # print the answers in bold text, without the a, b, c or d in normal text
                answers_text.append(option + ") " + list2[index][optionIndex])

        # pass the question and answer options to the template
        return render_template('quiz.html', question_text=question_text, answers_text=answers_text)

    # initialize session variables
    session.pop('index', None)
    session.pop('rightAnswers', None)
    session.pop('wrongAnswers', None)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
