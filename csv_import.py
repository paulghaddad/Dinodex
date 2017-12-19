import csv
import re
from dinosaur import *

dinosaurs = []

valid_periods = re.compile('cretaceous|permian|jurassic|oxfordian', flags=re.IGNORECASE)

def normalize_data(row):
    row = {k.lower(): v for k, v in row.items()}
    for attribute in row:
        if row[attribute] == '':
            row[attribute] = None
        if attribute == 'period':
            periods = row[attribute].lower()
            row[attribute] = set(re.findall(valid_periods, periods))
    return row

def parse_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            normalized_data = normalize_data(row)
            dinosaur = Dinosaur(normalized_data)
            dinosaurs.append(dinosaur)
    return dinosaurs
