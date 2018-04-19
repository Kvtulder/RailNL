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

        # valid connection, add to the list ands update the time
        self.stations.append(station)


        return 0

    # calculates the total duration of the line
    def get_total_time(self):
        total = 0
        for i in range(1, len(self.stations)):
            total += helper.get_time_between_stations(
                self.tracks, self.stations[i - 1], self.stations[i])

        return total


