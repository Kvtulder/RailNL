class Line:
    def __init__(self, stations=[]):
        self.stations = stations
        self.total_time = self.get_total_time()

    def __format__(self, format_spec):
        if isinstance(format_spec, str):
            message = "Track: : "
            for station in self.stations:
                message += "{}, ".format(station.name)
            message += "duration: {}".format(self.total_time)
            return message

    # Adds a new station to the list
    def add_station(self, station):
        # check if first station, if not: check if they're connected
        if not self.stations:
            self.stations.append(station)
        elif station in self.stations[-1].connections:
            self.stations.append(station)
            self.total_time += self.stations[-1].connections.duration
        else:
            raise StationNotConnectedError(
                "{} is not connected to {}".format(self.stations[-1].name,
                                                   station.name))

    # calculates the total duration of the line
    def get_total_time(self):
        total = 0
        for i in range(0, len(self.stations) - 1):
            current_station = self.stations[i]
            destination = self.stations[i + 1]
            total += float(current_station.connections[destination].duration)

        return total


class StationNotConnectedError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)