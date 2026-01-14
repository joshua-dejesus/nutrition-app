import camelot

tables = camelot.read_pdf('data_files/amdr_table.pdf', flavor='stream')
#daily_intake_table.export('daily_intake.json', f='json')

daily_intake_table_df = tables[0].df

print(daily_intake_table_df)