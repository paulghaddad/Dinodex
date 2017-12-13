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

fields = ['NAME', 'PERIOD', 'CONTINENT', 'DIET', 'WEIGHT_IN_LBS', 'WALKING',
          'DESCRIPTION']

dict_writer = csv.DictWriter(open("dinosaur_output.csv", "w"), fieldnames=fields)

dict_writer.writeheader()
dict_writer.writerows(dinosaurs[1:])
del dict_writer
