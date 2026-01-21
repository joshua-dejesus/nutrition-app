def parse_sex (raw: str) -> str:
    user_sex = str(raw.strip().lower())
    if user_sex == 'male' or user_sex == 'female':
        return user_sex
    else:
        raise ValueError("Sex must be 'male' or 'female'. Please try again.")

def parse_age (raw: str) -> int:
    try:
        user_age = int(raw)
        if user_age >= 1 and user_age <= 120:
            return user_age
        else:
            raise ValueError("Invalid input. Enter an age between 1 and 120: ")
    except ValueError:
        raise ValueError("Invalid input. You must enter an integer")

def parse_weight (raw: str) -> float:
    try:
        user_weight = float(raw)
        if user_weight >= 30.0 and user_weight <= 500.0:
            return user_weight
        else:
            raise ValueError("Invalid input. Enter a weight between 30.0lbs and 500.0lbs: ")
    except ValueError:
        raise ValueError("Invalid input. You must enter a number")

def parse_height (raw: str) -> int:
    try:
        user_height = int(raw)
        if user_height >= 21 and user_height <= 100:
            return user_height
        else:
            raise ValueError("Invalid input. Enter a height between 21 and 100 inches: ")
    except ValueError:
        raise ValueError("Invlaid input. You must enter an integer")

def parse_activity_level (raw: str) -> str:
    try:
        user_activity = int(raw)
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
            raise ValueError("Invalid input. Enter a number corresponding to your activity level")
    except ValueError:
        raise ValueError("Invalid input. Enter an integer")