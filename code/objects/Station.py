# define objects
class Station:
    def __init__(self, name, latitude, longitude, critical):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.critical = critical
        self.surrounding = {}

    def __format__(self, format_spec):
        if isinstance(format_spec, str):
            return self.name

    def load_surrounding(self, tracks):
        for track in tracks:
            station_a = tracks[track].station_a.name
            station_b = tracks[track].station_a.name

            if station_a == self.name or station_b == self.name:
                self.surrounding.update({track : tracks[track]})