import json
import os
import pandas as pd

from incident import Incident
from unit import Unit


def main():
    json_path = 'data'
    json_list = []
    incident_list = []

    for file in os.listdir(json_path):
        if file.endswith('.json'):
            json_list.append(file)

    for i, j in enumerate(json_list):
        with open(os.path.join(json_path, j)) as json_file:
            incident_json = json.load(json_file)

        incident_list.append(incident_json)


if __name__ == "__main__":
    main()
