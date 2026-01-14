import data_files.daily_intakes

def calculate_daily_calories(weight_in_lbs: float, height_in_inches: int, sex: str, age_in_years: int, activity_level: str):
    bmr = 0
    
    # uses the Mifflin-St Jeor Equation
    if sex == 'male':
        bmr = (4.536 * weight_in_lbs) + (15.88 * height_in_inches) - (5 * age_in_years) + 5
    else:
        bmr = (4.536 * weight_in_lbs) + (15.88 * height_in_inches) - (5 * age_in_years) - 161

    total_calories_expenditure = bmr

    if activity_level == 'sedentary':
        total_calories_expenditure *= 1.2
    elif activity_level == 'lightly acitve':
        total_calories_expenditure *= 1.375
    elif activity_level == 'moderately active':
        total_calories_expenditure *= 1.55
    elif activity_level == 'active':
        total_calories_expenditure *= 1.725
    else:
        total_calories_expenditure *= 1.9

    return int(total_calories_expenditure)


    
