class Track:
    def __init__(self, destination, duration, critical, start=None):
        self.destination = destination
        self.duration = float(duration)
        self.critical = critical
        self.start = start
