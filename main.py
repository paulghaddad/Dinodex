import argparse
from csv_import import parse_csv
from csv_export import export_csv
from excel_export import export_excel
from json_export import export_json
from export_table import export_table
from filters import biped, carnivore, in_period, of_size

parser = argparse.ArgumentParser(description='Filter some dinosaurs')
parser.add_argument('filename', help='Input filename containing dinosaur data')
parser.add_argument('--export', nargs='*', default='csv',
                    choices=['csv', 'xlsx', 'json'], help='Export file type (csv, xlsx, json)')
parser.add_argument('--biped', action='store_true', help='Filter for bipeds')
parser.add_argument('--carnivore', action='store_true', help='Filter by carnivores')
parser.add_argument('--period', nargs='*', choices=['cretaceous', 'permian', 'jurassic', 'oxfordian'], help='Filter by period')
parser.add_argument('--size', choices=['big', 'small'], help='Filter for size (big or small)')
parser.add_argument('--print_dino', help='Print information on a single dinosaur')
args = parser.parse_args()

input_filename = args.filename
export_types = args.export
periods = args.period
size_filter = args.size
print_dino = args.print_dino

dinosaurs = parse_csv(input_filename)

# Filter dinosaurs
filtered_dinosaurs = dinosaurs

if args.biped:
    filtered_dinosaurs = [dinosaur for dinosaur in filtered_dinosaurs if biped(dinosaur)]
if args.carnivore:
    filtered_dinosaurs = [dinosaur for dinosaur in filtered_dinosaurs if carnivore(dinosaur)]
if args.period:
    filtered_dinosaurs = [dinosaur for dinosaur in filtered_dinosaurs if in_period(dinosaur, periods)]
if size_filter:
    filtered_dinosaurs = [dinosaur for dinosaur in filtered_dinosaurs if of_size(dinosaur, size_filter)]

if print_dino:
    dinosaur_to_print = set(filter(lambda dinosaur: dinosaur.name.lower() ==
                                   print_dino.lower(), dinosaurs))

FIELDS = ['name', 'period', 'continent', 'diet', 'weight', 'walking_mode',
          'description']

# Output to a CSV
if 'csv' in export_types:
    export_csv(FIELDS, filtered_dinosaurs)

# Output to an Excel file
if 'xlsx' in export_types:
    export_excel(FIELDS, filtered_dinosaurs)

# Output to a JSON file
if 'json' in export_types:
    export_json(filtered_dinosaurs)

# Ouput to the command line
export_table(FIELDS, filtered_dinosaurs)

# Print out single dinosaur if option provided

def print_attribute(attribute):
    if not attribute: return 'N/A'

    if isinstance(attribute, set):
        return ', '.join(attribute).capitalize()
    else:
        return attribute


if print_dino and dinosaur_to_print:
    dinosaur = dinosaur_to_print.pop()
    dinosaur_information = f"""
        Information on {print_attribute(dinosaur.name)}:
            Period: {print_attribute(dinosaur.period)}
            Continent: {print_attribute(dinosaur.continent)}
            Diet: {print_attribute(dinosaur.diet)}
            Weight (lbs): {print_attribute(dinosaur.weight)}
            Mode of Walking: {print_attribute(dinosaur.walking_mode)}
            Description: {print_attribute(dinosaur.description)}

    """

    print(dinosaur_information)
