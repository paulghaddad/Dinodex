import csv

dinosaurs = [dinosaurs for dinosaurs in csv.DictReader(open("dinodex.csv"))]

print(dinosaurs[0])
