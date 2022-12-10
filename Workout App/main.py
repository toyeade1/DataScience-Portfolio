import requests
from flask import Flask, redirect, request, render_template
from datetime import datetime
from os import environ as env
import sqlite3

app = Flask(__name__)

SHEETY_API = "https://api.sheety.co/952ea927b5ee42228ec81e7a704646d6/toye'sWorkouts/workouts"
today = datetime.now().strftime('%d/%m/%Y')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def save_workout():

    # Get the workout data from the form
    workout_name = request.form['workout_name']
    sett = request.form['sett']
    reps = request.form['reps']
    weight = request.form['weight']

    if workout_name == 'Bp' or 'bp':
        workout_name = 'Bench Press'
    elif workout_name == 'Dp' or 'dp':
        workout_name = 'Dumbell Bench Press'

    # Connect to the Sheety API and enter information
    sheet_input = {
        'workout': {
            'date': today,
            'exercise': workout_name.title(),
            'set': int(sett),
            'weight': int(weight),
            'reps': int(reps)
        }
    }

    sheet_response = requests.post(url=SHEETY_API, json=sheet_input)
    print(sheet_response.text)

    # Redirect the user to the homepage

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
