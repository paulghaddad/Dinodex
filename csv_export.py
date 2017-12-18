import csv

def export_csv(fields, data):
    dict_writer = csv.DictWriter(open("dinosaur_data.csv", "w"), fieldnames=fields)
    dict_writer.writeheader()
    dict_writer.writerows(data)
    del dict_writer
