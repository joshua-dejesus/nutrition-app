import camelot

tables = camelot.read_pdf('data_files/amdr_table.pdf', flavor='stream')
df = tables[0].df

def get_nutrition_recommendation(age_in_years: int, sex: str=None):

    if sex == None and age_in_years in range(1, 4):
        return str(df[0] + "            " + df[2])
    
    if sex == 'male':
        if age_in_years in range(4, 9):
            return str(df[0] + "            " + df[4])
        elif age_in_years in range(9, 14):
            return str(df[0] + "            " + df[6])
        elif age_in_years in range(14, 19):
            return str(df[0] + "            " + df[8])
        elif age_in_years in range (19, 31):
            return str(df[0] + "            " + df[10])
        elif age_in_years in range(31, 50):
            return str(df[0] + "            " + df[12])
        else:
            return str(df[0] + "            " + df[14])
    else:
        if age_in_years in range(4, 9):
            return str(df[0] + "            " + df[3])
        elif age_in_years in range(9, 14):
            return str(df[0] + "            " + df[5])
        elif age_in_years in range(14, 19):
            return str(df[0] + "            " + df[7])
        elif age_in_years in range (19, 31):
            return str(df[0] + "            " + df[9])
        elif age_in_years in range(31, 50):
            return str(df[0] + "            " + df[11])
        else:
            return str(df[0] + "            " + df[13])