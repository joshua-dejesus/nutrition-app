import calculations.calculation_file
import data_files.daily_intakes
from models.user import User
from user_input.user_input_handler import (get_sex, get_age, get_weight, get_height, get_activity_level)

sex = get_sex("Enter your sex (male or female): ")
age_in_years = get_age("Enter your age in years: ")
weight_in_lbs = get_weight("Enter your weight in pounds: ")
height_in_inches = get_height("Enter your height in inches: ")
activity_level = get_activity_level("Enter the number correspodning to your activity level from the options below: \n 1. Sedentary \n 2. Lightly Active \n 3. Moderately Active \n 4. Active \n 5. Very Active \n")

new_user = User(sex, age_in_years, weight_in_lbs, height_in_inches, activity_level)

calories = calculations.calculation_file.calculate_daily_calories(new_user.weight_in_lbs, new_user.height_in_inches, new_user.sex, new_user.age_in_years, new_user.activity_level)
print("\nYour calculated daily caloric expenditure is: " + str(calories))

print("\nYour recommended daily nutrients intake is: ")
nutrients = data_files.daily_intakes.get_nutrition_recommendation(new_user.age_in_years, new_user.sex)
print (nutrients)