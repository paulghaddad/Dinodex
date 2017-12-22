import csv

def export_csv(fields, data):
    dict_writer = csv.DictWriter(open("dinosaur_data.csv", "w"), fieldnames=fields)
    dict_writer.writeheader()

    attributes = []
    for dinosaur in data:
        row = {}
        for attribute in fields:
            row[attribute] = getattr(dinosaur, attribute)
        attributes.append(row)

    dict_writer.writerows(attributes)
    del dict_writer
