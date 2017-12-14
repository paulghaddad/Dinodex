import csv
import json
from openpyxl import Workbook
from prettytable import PrettyTable

dinosaurs = []

def normalize_data(row):
    for attribute in row:
        if row[attribute] == '':
            row[attribute] = None
    return row

with open("dinodex.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dinosaur = normalize_data(row)
        dinosaurs.append(dinosaur)

fields = ['NAME', 'PERIOD', 'CONTINENT', 'DIET', 'WEIGHT_IN_LBS', 'WALKING',
          'DESCRIPTION']

# Output to a CSV
dict_writer = csv.DictWriter(open("dinosaur_data.csv", "w"), fieldnames=fields)

dict_writer.writeheader()
dict_writer.writerows(dinosaurs[1:])
del dict_writer

# Output to an Excel file
wb = Workbook()
ws = wb.active
ws.title = "Dinosaur Data"

ws.append(fields)

for row in dinosaurs:
    ws.append(list(row.values()))

wb.save("dinosaur_data.xlsx")

# Output to a JSON file
json_outfile = open("dinosaur_data.json", "w")
json.dump(dinosaurs, json_outfile)
json_outfile.close()

# Ouput to the command line
table = PrettyTable(fields)
table.align = "l"

for dinosaur in dinosaurs:
    table.add_row(dinosaur.values())

print("\n\n")
print(table)
print("\n\n")
