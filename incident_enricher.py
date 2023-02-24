from datetime import datetime
from dateutil import parser
from meteostat import Point, Hourly


def enrich(incident_list):
    for incident in incident_list:
        start = parser.parse(incident.get_description()['event_opened'])
        start = datetime(start.year, start.month, start.day, start.hour, start.minute)
        end = parser.parse(incident.get_description()['event_closed'])
        end = datetime(end.year, end.month, end.day, end.hour, end.minute)

        location = Point(incident.get_address()['latitude'], incident.get_address()['longitude'], None)

        data = Hourly(location, start, end)
        data = data.fetch()

        incident.set_weather(data)
    return incident_list

