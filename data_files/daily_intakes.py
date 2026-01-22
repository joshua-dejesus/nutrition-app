from typing import Any, OrderedDict
import camelot

tables = camelot.read_pdf('data_files/amdr_table.pdf', flavor='stream')
df = tables[0].df

def get_nutrition_recommendation(age_in_years: int, sex: str=None):

    col1, col2 = df[0], None

    if sex == None and age_in_years in range(1, 4):
        col2 = df[2]
    
    if sex == 'male':
        if age_in_years in range(4, 9):
            col2 = df[4]
        elif age_in_years in range(9, 14):
            col2 = df[6]
        elif age_in_years in range(14, 19):
            col2 = df[8]
        elif age_in_years in range (19, 31):
            col2 = df[10]
        elif age_in_years in range(31, 50):
            col2 = df[12]
        else:
            col2 = df[14]
    else:
        if age_in_years in range(4, 9):
            col2 = df[3]
        elif age_in_years in range(9, 14):
            col2 = df[5]
        elif age_in_years in range(14, 19):
            col2 = df[7]
        elif age_in_years in range (19, 31):
            col2 = df[9]
        elif age_in_years in range(31, 50):
            col2 = df[11]
        else:
            col2 = df[13]

    if col2 is not None:
        nutrients_dict = OrderedDict[Any, Any]()
        for i in range (len(col1)):
            nutrient_name = str(col1.iloc[i]).strip()
            nutrient_value = str(col2.iloc[i]).strip()
            nutrients_dict[nutrient_name] = nutrient_value

    return nutrients_dict