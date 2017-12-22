from openpyxl import Workbook

def stringify_values(values):
    stringified_values = []
    for value in values:
        if isinstance(value, list):
            stringified_values.append(', '.join(value))
        else:
            stringified_values.append(value)
    return stringified_values

def export_excel(fields, data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Dinosaur Data"

    ws.append(fields)

    for row in data:
        cells = stringify_values(vars(row).values())
        ws.append(cells)

    wb.save("dinosaur_data.xlsx")
