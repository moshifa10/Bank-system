import json

def add_to_json(new_data, filename="data.json"):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data["users_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
