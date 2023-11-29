from flask import render_template, request, redirect
from app import app


@app.route('/')
def index():
    # GET HIGHSCORE FROM DATABASE.
    pass
    return render_template('index.html')


@app.route('/highscore', methods=['GET', 'POST'])
def highscore():

    if request.method == 'GET':

        # GET HIGHSCORE FROM DATABASE.
        pass

    if request.method == 'POST':
        pass
