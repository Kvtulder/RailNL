class Track:
    def __init__(self, destination, duration, critical,start=None):
        self.destination = destination
        self.duration = duration
        self.critical = critical
        self.start = start