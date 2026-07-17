import json


def save_application(data):

    with open("db.json", "r") as file:
        database = json.load(file)

    database.append(data)

    with open("db.json", "w") as file:
        json.dump(database, file, indent=4)


def get_applications():

    with open("db.json", "r") as file:
        return json.load(file)