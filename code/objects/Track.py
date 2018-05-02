class Track:
    def __init__(self, destination, duration, critical, id, start=None):
        self.destination = destination
        self.duration = float(duration)
        self.critical = critical
        self.start = start
        self.id = id

