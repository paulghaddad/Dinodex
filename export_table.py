from prettytable import PrettyTable

def export_table(fields, data):
    table = PrettyTable(fields)
    table.align = "l"

    for dinosaur in data:
        table.add_row(dinosaur.values())

    print("\n\n")
    print(table)
    print("\n\n")
