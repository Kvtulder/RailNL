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
    def add_station_by_track(self, track):

        station = self.get_last_station()
        destination = track.get_other_station(station)

        # check if first station, if not: check if they're connected
        if not self.stations:
            self.stations.append(destination)
            return

        if track.key in station.connections:
            self.stations.append(destination)
            self.total_time += float(track.duration)
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

            key1 = "{}-{}".format(current_station.name, destination.name)
            key2 = "{}-{}".format(destination.name, current_station.name)

            if key1 in current_station.connections:
                track = current_station.connections[key1]
            elif key2 in current_station.connections:
                track = current_station.connections[key2]

            total += float(track.duration)

        return total

    def remove_last_station(self):

        last_station = self.stations[-1]
        second_last_station = self.stations[-2]

        key1 = "{}-{}".format(last_station.name, second_last_station.name)
        key2 = "{}-{}".format(second_last_station.name, last_station.name)

        if key1 in second_last_station.connections:
            track = second_last_station.connections[key1]
        elif key2 in second_last_station.connections:
            track = second_last_station.connections[key2]
        else:
            raise StationNotConnectedError(
                "{} is not connected to {}".format(last_station.name,
                                                   second_last_station.name))

        # calculate the duration to the last station and remove that
        self.total_time -= float(track.duration)

        # delete the station from the list
        del self.stations[-1]

    def get_last_station(self):
        return self.stations[-1]


class StationNotConnectedError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)