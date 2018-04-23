# define objects
class Station:
    def __init__(self, name, latitude, longitude, critical):
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.critical = critical
        self.connections = {}

    def __format__(self, format_spec):
        if isinstance(format_spec, str):
            return self.name

    def add_connection(self, track):
        self.connections.update({track.destination.name: track})