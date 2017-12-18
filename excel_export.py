from openpyxl import Workbook

def export_excel(fields, data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Dinosaur Data"

    ws.append(fields)

    for row in data:
        ws.append(list(row.values()))

    wb.save("dinosaur_data.xlsx")
