from incident import Incident


def create_incidents(incident_list):

    l = []
    for i in incident_list:
        incident = Incident(
            address=i['address'],
            apparatus=i['apparatus'],
            description=i['description'],
            fire_department=i['fire_department'],
            version=i['version']
        )
        l.append(incident)

    return l
