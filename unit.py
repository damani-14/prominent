

class Unit:

    def __init__(self, **kwargs):

        self.car_id = kwargs.get('car_id', '')
        self.extended_data = kwargs.get('extended_data', {})
        self.geohash = kwargs.get('geohash', '')
        self.personnel = kwargs.get('personnel', [])
        self.shift = kwargs.get('shift', '')
        self.station = kwargs.get('station', '')
        self.unit_id = kwargs.get('unit_id', '')
        self.unit_status = kwargs.get('unit_status', {})
        self.unit_type = kwargs.get('unit_type', '')

    def get_car_id(self):
        return self.car_id

    def set_car_id(self, car_id):
        self.car_id = car_id

    def get_extended_data(self):
        return self.extended_data

    def set_extended_data(self, extended_data):
        self.extended_data = extended_data

    def get_geohash(self):
        return self.geohash

    def set_geohash(self, geohash):
        self.geohash = geohash

    def get_personnel(self):
        return self.personnel

    def set_personnel(self, personnel):
        self.personnel = personnel

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift

    def get_station(self):
        return self.station

    def set_station(self, station):
        self.station = station

    def get_unit_id(self):
        return self.unit_id

    def set_unit_id(self, unit_id):
        self.unit_id = unit_id

    def get_unit_status(self):
        return self.unit_status

    def set_unit_status(self, unit_status):
        self.unit_status = unit_status

    def get_unit_type(self):
        return self.unit_type

    def set_unit_type(self, unit_type):
        self.unit_type = unit_type
