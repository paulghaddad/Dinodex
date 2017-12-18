import csv
from csv_import import parse_csv
from csv_export import export_csv
from excel_export import export_excel
from json_export import export_json
from export_table import export_table

dinosaurs = parse_csv("dinodex.csv")

fields = ['name', 'period', 'continent', 'diet', 'weight_in_lbs', 'walking',
          'description']

# Output to a CSV
export_csv(fields, dinosaurs)

# Output to an Excel file
export_excel(fields, dinosaurs)

# Output to a JSON file
export_json(dinosaurs)

# Ouput to the command line
export_table(fields, dinosaurs)
