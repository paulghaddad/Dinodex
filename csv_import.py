import csv

dinosaurs = []

def normalize_data(row):
    for attribute in row:
        if row[attribute] == '':
            row[attribute] = None
    return row

def parse_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dinosaur = normalize_data(row)
            dinosaurs.append(dinosaur)
    return dinosaurs
