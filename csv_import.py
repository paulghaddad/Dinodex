import csv
from dinosaur import *

dinosaurs = []

def normalize_data(row):
    row = {k.lower(): v for k, v in row.items()}
    for attribute in row:
        if row[attribute] == '':
            row[attribute] = None
    return row

def parse_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            normalized_data = normalize_data(row)
            dinosaur = Dinosaur(normalized_data)
            dinosaurs.append(dinosaur)
    return dinosaurs
