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
        self.connections.update({track.key: track})

    def get_shortest_connection(self, forbidden_tracks=[]):
        shortest = None
        connections = self.connections

        for key in connections:
            track = connections[key]

            if track not in forbidden_tracks:
                if not shortest or track.duration < shortest.duration:
                    shortest = track

        return shortest
