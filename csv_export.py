import csv

def export_csv(fields, data):
    dict_writer = csv.DictWriter(open("dinosaur_data.csv", "w"), fieldnames=fields)
    dict_writer.writeheader()
    attributes = [vars(dinosaur) for dinosaur in data]
    dict_writer.writerows(attributes)
    del dict_writer
