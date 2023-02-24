

class Incident:

    def __init__(self, **kwargs):

        self.address = kwargs.get('address', {})
        self.apparatus = kwargs.get('apparatus', [])
        self.description = kwargs.get('description', {})
        self.fire_department = kwargs.get('fire_department', {})
        self.version = kwargs.get('version', {})
        self.units = None

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_apparatus(self):
        return self.apparatus

    def set_apparatus(self, apparatus):
        self.apparatus = apparatus

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_fire_department(self):
        return self.fire_department

    def set_fire_department(self, fire_department):
        self.fire_department = fire_department

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def get_units(self):
        return self.units

    def set_units(self, units):
        self.units = units
