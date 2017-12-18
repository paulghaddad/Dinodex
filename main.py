import argparse
from csv_import import parse_csv
from csv_export import export_csv
from excel_export import export_excel
from json_export import export_json
from export_table import export_table

parser = argparse.ArgumentParser(description='Filter some dinosaurs')
parser.add_argument('filename', help='Input filename containing dinosaur data')
parser.add_argument('--export', nargs='*', default='csv',
                    choices=['csv', 'xlsx', 'json'], help='Export file type (csv, xlsx, json)')
args = parser.parse_args()

input_filename = args.filename
export_types = args.export

dinosaurs = parse_csv(input_filename)

fields = ['name', 'period', 'continent', 'diet', 'weight_in_lbs', 'walking',
          'description']

# Output to a CSV
if 'csv' in export_types:
    export_csv(fields, dinosaurs)

# Output to an Excel file
if 'xlsx' in export_types:
    export_excel(fields, dinosaurs)

# Output to a JSON file
if 'json' in export_types:
    export_json(dinosaurs)

# Ouput to the command line
export_table(fields, dinosaurs)
