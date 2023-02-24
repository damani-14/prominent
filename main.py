import geopandas as gpd
import incident_builder
import incident_enricher
import json
import os
import sys
import pandas as pd
import unit_builder

from geojson import MultiPoint, Point
from incident import Incident
from unit import Unit


def main():
    json_path = 'data'
    json_list = []
    incidents = []

    for file in os.listdir(json_path):
        if file.endswith('.json'):
            json_list.append(file)

    for i, j in enumerate(json_list):
        with open(os.path.join(json_path, j)) as json_file:
            incident_json = json.load(json_file)

        incidents.append(incident_json)

    incidents = incident_builder.create_incidents(incidents)
    # incidents = unit_builder.create_units(incidents)
    incidents = incident_enricher.enrich(incidents)

    for incident in incidents:
        sys.stdout.write(str(incident.__dict__))


if __name__ == "__main__":
    main()
