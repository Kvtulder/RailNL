class Track:
    def __init__(self, start, destination, duration, critical, key):
        self.start = start
        self.destination = destination
        self.duration = float(duration)
        self.critical = critical
        self.key = key

