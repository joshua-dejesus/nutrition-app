from flask import Flask, render_template, request
from calculations.calculation_file import calculate_daily_calories
from data_files.daily_intakes import get_nutrition_recommendation
import user_input.user_input_handler

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('home.html')

@app.route('/analyze', methods=["POST"])
def analyze ():
    try:
        sex = user_input.user_input_handler.parse_sex(request.form["sex"])
        age = user_input.user_input_handler.parse_age(request.form["age"])
        weight = user_input.user_input_handler.parse_weight(request.form["weight"])
        height = user_input.user_input_handler.parse_height(request.form["height"])
        activity_level = user_input.user_input_handler.parse_activity_level(request.form["activity_level"])
    except ValueError as e:
        return render_template('home.html', error=str(e))
    
    calories = calculate_daily_calories(weight, height, sex, age, activity_level)
    nutrients = get_nutrition_recommendation(age, sex)

    return render_template('results.html', calories=calories, nutrients=nutrients) 

if __name__ == "__main__":
    app.run(port=8000, debug=True)