import incident_builder
import json
import os
import pandas as pd

from incident import Incident
from unit import Unit


def main():
    json_path = 'data'
    json_list = []
    incidents_raw = []

    for file in os.listdir(json_path):
        if file.endswith('.json'):
            json_list.append(file)

    for i, j in enumerate(json_list):
        with open(os.path.join(json_path, j)) as json_file:
            incident_json = json.load(json_file)

        incidents_raw.append(incident_json)

    incidents_transformed = incident_builder.create_incidents(incidents_raw)


if __name__ == "__main__":
    main()
