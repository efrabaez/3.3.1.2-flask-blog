import json
import os

app_dir = os.path.dirname(__file__)  # <-- app directory


def get_profile_data(filename):
    filename = os.path.join(app_dir, filename)
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
        return data
