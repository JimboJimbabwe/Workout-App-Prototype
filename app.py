from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Replace this with your actual data and logic
workouts = {
    'Back Circuit': {
        'Lat Pulldown': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 120,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,  # lbs per day
        },
        'Low Rows/Horizontal Row': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 100,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,
        },
        'Shrugs': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 60,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,
        },
        'Deadlifts': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 275,
            'sets': 4,
            'reps': 4,
            'increase_rate': 0.5,
        }
    },
    'Chest Circuit': {
        'Bench': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 185,
            'sets': 4,
            'reps': 4,
            'increase_rate': 0.5,
        },
        'Seated Jaunt': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 140,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,
        }
    },
    'Shoulders': {
        'Military Press': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 105,
            'sets': 4,
            'reps': 4,
            'increase_rate': 0.5,
        }
    },
    'Triceps': {
        'Dips machine': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 180,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,
        },
        'French Press': {
            'last_performed': datetime.now() - timedelta(days=1),
            'weight': 65,
            'sets': 3,
            'reps': 8,
            'increase_rate': 0.5,
        }
    }
}

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/workouts')
def get_workouts():
    for category, exercises in workouts.items():
        for exercise in exercises.values():
            days_since_last = (datetime.now() - exercise['last_performed']).days
            exercise['weight'] += days_since_last * exercise['increase_rate']
            exercise['last_performed'] = datetime.now()
    # Converting the nested dict structure to a list of dicts for each circuit
    formatted_workouts = {circuit: [{'name': name, 'weight': data['weight'], 'sets': data['sets'], 'reps': data['reps']} for name, data in exercises.items()] for circuit, exercises in workouts.items()}
    return jsonify(formatted_workouts)

if __name__ == '__main__':
    app.run(debug=True)
