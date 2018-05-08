class Track:
    def __init__(self, start, destination, duration, critical, key):
        self.start = start
        self.destination = destination
        self.duration = float(duration)
        self.critical = critical
        self.key = key

    def get_other_station(self, station):
        if self.start == station:
            return self.destination
        elif self.destination == station:
            return self.start
        else:
            raise ValueError("Station does not match start or destination")


