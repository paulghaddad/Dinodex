import csv
import re
from dinosaur import *

dinosaurs = []

VALID_ATTRIBUTES = ('name', 'period', 'continent', 'diet', 'weight_in_lbs', 'walking_mode', 'description')

VALID_ATTRIBUTES_MAPPING = {'genus': 'name', 'carnivore': 'diet', 'weight':
                       'weight_in_lbs', 'walking': 'walking_mode'}

valid_periods = re.compile('cretaceous|permian|jurassic|oxfordian', flags=re.IGNORECASE)

def normalize_attribute(attribute):
    lowercase_attribute = attribute.lower()
    if lowercase_attribute in VALID_ATTRIBUTES:
        return lowercase_attribute
    elif lowercase_attribute in VALID_ATTRIBUTES_MAPPING:
        return VALID_ATTRIBUTES_MAPPING[lowercase_attribute]
    else:
        raise Exception('Invalid attribute!')


def normalize_data(row):
    # normalize all the attributes in the incoming row
    row_with_normalized_attributes = {}
    for attribute in row:
        normalized_attribute = normalize_attribute(attribute)
        row_with_normalized_attributes[normalized_attribute] = row[attribute]


    # import pdb; pdb.set_trace()
    # create an object with all the necessary attributes for a dinosaur
    for attribute in VALID_ATTRIBUTES:
        if attribute not in row_with_normalized_attributes:
            row_with_normalized_attributes[attribute] = None

    # import pdb; pdb.set_trace()
    # Normalize attribute values in each row
    normalized_row = {}
    for attribute in row_with_normalized_attributes:
        if row_with_normalized_attributes[attribute] == '':
            normalized_row[attribute] = None
        if attribute == 'period':
            periods = row_with_normalized_attributes[attribute].lower()
            normalized_row[attribute] = set(re.findall(valid_periods, periods))
        else:
            normalized_row[attribute] = row_with_normalized_attributes[attribute]

    # import pdb; pdb.set_trace()
    return normalized_row

def parse_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            normalized_data = normalize_data(row)

            dinosaur = Dinosaur(normalized_data)
            dinosaurs.append(dinosaur)
    return dinosaurs
