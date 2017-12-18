import json

def export_json(data):
    json_outfile = open("dinosaur_data.json", "w")
    json_data = [vars(row) for row in data]
    json.dump(json_data, json_outfile)
    json_outfile.close()
