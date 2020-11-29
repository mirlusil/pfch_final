# A big thank you to https://github.com/nithinmurali/pygsheets

import json
import pygsheets

# make sure to do this before running other things, will create new json file with credentials
gc = pygsheets.authorize()

passwords = json.load(open('passwords.json'))

file = gc.open_by_key(passwords['sheet_key'])
sheet = file.worksheet('index', 0)

# open json data file
with open('data/clean_data.json', 'r') as open_file:
    data = json.load(open_file)

    # starting with Row 3. Row 1 is the headings provided by KnightLab, Row 2 is the title info which I entered manually on Google Sheets
    row = 3

    for object in data:
        sheet.update_values(crange=f'A{row}:R{row}', values=[data[object]])
        row += 1
