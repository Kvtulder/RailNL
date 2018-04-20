class Line:
    def __init__(self, stations=[]):
        self.stations = stations
        if len(stations) > 1:
            self.total_time = self.get_total_time()
        else:
            self.total_time = 0

    def __format__(self, format_spec):
        if isinstance(format_spec, str):
            message = "Track: : "
            for station in self.stations:
                message += "{}, ".format(station.name)
            message += "duration: {}".format(self.total_time)
            return message

    # Adds a new station to the list
    def add_station(self, destination):
        # check if first station, if not: check if they're connected
        if not self.stations:
            self.stations.append(destination)
            return

        station = self.get_last_station()
        if destination.name in station.connections:
            self.stations.append(destination)
            self.total_time += float(station.connections[destination.name].duration)
        else:
            raise StationNotConnectedError(
                "{} is not connected to {}".format(station.name,
                                                   destination.name))

    # calculates the total duration of the line
    def get_total_time(self):
        total = 0
        for i in range(0, len(self.stations) - 1):
            current_station = self.stations[i]
            destination = self.stations[i + 1]
            total += float(current_station.connections[destination.name].duration)

        return total

    def remove_last_station(self):
        # calculate the duration to the last station and remove that
        self.total_time -= float(self.stations[-2]
                                 .connections[self.stations[-1].name].duration)

        # delete the station from the list
        del self.stations[-1]

    def get_last_station(self):
        return self.stations[-1]


class StationNotConnectedError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)