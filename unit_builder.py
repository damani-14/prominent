from unit import Unit


def create_units(incident_list):

    l = []
    for i in incident_list:
        for j in i.get_apparatus():
            unit = Unit(
                car_id=j['car_id'],
                extended_data=j['extended_data'],
                geohash=j['geohash'],
                personnel=j['personnel'],
                shift=j['shift'],
                station=j['station'],
                unit_id=j['unit_id'],
                unit_status=j['unit_status'],
                unit_type=j['unit_type']
            )
            l.append(unit)
        i.set_units(l)

    return incident_list
