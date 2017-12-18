import json

def export_json(data):
    json_outfile = open("dinosaur_data.json", "w")
    json.dump(data, json_outfile)
    json_outfile.close()
