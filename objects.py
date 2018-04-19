import helper


# define objects
class Station:
    def __init__(self, name, latitude, longitude, critical):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.critical = critical


class Track:
    def __init__(self, station_a, station_b, time):
        self.station_a = station_a
        self.station_b = station_b
        self.time = float(time)


class Line:
    def __init__(self, tracks, stations=[]):
        self.stations = stations
        self.tracks = tracks
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

        # check if first station
        if not self.stations:
            self.stations.append(station)

        if not helper.check_if_connected(
                self.tracks, self.stations[-1], station):
                print("Warning: {} not connected to {}".format(
                    self.stations[-1], station))
                return -1

        # valid connection, add to the list ands update the time
        self.stations.append(station)
        if len(self.stations) > 1:
            self.update_time()

        return 0

    # calculates the total duration of the line
    def get_total_time(self):
        total = 0
        for i in range(1, len(self.stations)):
            total += helper.get_time_between_stations(
                self.tracks, self.stations[i - 1], self.stations[i])

        return total

    # updates the time after a station is added to the list.
    def update_time(self):
        self.total_time += helper.get_time_between_stations(
            self.tracks, self.stations[-2], self.stations[-1])




