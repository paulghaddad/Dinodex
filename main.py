import csv

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

print(dinosaurs)
