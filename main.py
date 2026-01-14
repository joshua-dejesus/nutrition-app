import calculations.calculation_file
import data_files.daily_intakes

def get_sex (prompt) -> str:
    while True:
        user_sex = str(input(prompt)).strip().lower()
        if user_sex == 'male' or user_sex == 'female':
            return user_sex
        else:
            print("Invalid input. Sex must be male or female: ")

def get_age (prompt) -> int:
    while True:
        try:
            user_age = int(input(prompt))
            if user_age >= 1 and user_age <= 120:
                return user_age
            else:
                print("Invalid input. Enter an age between 1 and 120: ")
        except ValueError:
            print("Invalid input. You must enter an integer")

def get_weight (prompt) -> float:
    while True:
        try:
            user_weight = float(input(prompt))
            if user_weight >= 30.0 and user_weight <= 500.0:
                return user_weight
            else:
                print("Invalid input. Enter a weight between 30.0lbs and 500.0lbs: ")
        except ValueError:
            print("Invalid input. You must enter a number")

def get_height (prompt) -> int:
    while True:
        try:
            user_height = int(input(prompt))
            if user_height >= 21 and user_height <= 100:
                return user_height
            else:
                print("Invalid input. Enter a height between 21 and 100 inches: ")
        except ValueError:
            print("Invlaid input. You must enter an integer")

def get_activity_level (prompt) -> str:
    while True:
        try:
            user_activity = int(input(prompt))
            if user_activity == 1:
                return 'sedentary'
            elif user_activity == 2:
                return 'lightly active'
            elif user_activity == 3:
                return 'moderately active'
            elif user_activity == 4:
                return 'active'
            elif user_activity == 5:
                return 'very active'
            else:
                print("Invalid input. Enter a number corresponding to your activity level")
        except ValueError:
            print("Invalid input. Enter an integer")
    


sex = get_sex("Enter your sex (male or female): ")
age_in_years = get_age("Enter your age in years: ")
weight_in_lbs = get_weight("Enter your weight in pounds: ")
height_in_inches = get_height("Enter your height in inches: ")
activity_level = get_activity_level("Enter the number correspodning to your activity level from the options below: \n 1. Sedentary \n 2. Lightly Active \n 3. Moderately Active \n 4. Active \n 5. Very Active \n")

calories = calculations.calculation_file.calculate_daily_calories(weight_in_lbs, height_in_inches, sex, age_in_years, activity_level)
print("\nYour calculated daily caloric expenditure is: " + str(calories))

print("\nYour recommended daily nutrients intake is: ")
nutrients = data_files.daily_intakes.get_nutrition_recommendation(age_in_years, sex)