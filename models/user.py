class User:
    def __init__(self, sex: str, age_in_years: int, weight_in_lbs: float, height_in_inches: int, activity_level: str):
        self._sex = sex
        self._age_in_years = age_in_years
        self._weight_in_lbs = weight_in_lbs
        self._height_in_inches = height_in_inches
        self._activity_level = activity_level
    
    @property
    def sex (self) -> str:
        return self._sex

    @property
    def age_in_years (self) -> int:
        return self._age_in_years
    
    @property
    def weight_in_lbs (self) -> float:
        return self._weight_in_lbs
    
    @property
    def height_in_inches (self) -> int:
        return self._height_in_inches
    
    @property
    def activity_level (self) -> str:
        return self._activity_level