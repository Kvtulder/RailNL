import csv
from objects.Station import Station
from objects.Track import Track

class Data:
    def __init__(self, scope="Nationaal"):

        if scope == "Nationaal":
            self.max_duration = 180
            self.num_of_lines = 20
        else:
            self.max_duration = 120
            self.num_of_lines = 7

        self.station_file = "./data/Stations" + scope + ".csv"
        self.track_file = "./data/Connecties" + scope + ".csv"
        self.stations, self.tracks = self.load(self.station_file, self.track_file)

        self.num_crit_tracks = self.get_num_of_critical_tracks()
        self.points_per_crit = 1/self.num_crit_tracks * 10000


    def load(self, station_file, track_file):
        stations = {}
        tracks = {}

        print("loading stations and tracks...")
        # add all stations
        with open(station_file) as file:
            reader = csv.reader(file)
            for row in reader:
                # check if there is a critical row
                if len(row) > 3:
                    stations.update({
                        row[0]: Station(row[0], row[1], row[2],
                                        row[3] == 'Kritiek')})
                else:
                    stations.update({
                        row[0]: Station(row[0], row[1], row[2], False)})

        # add all tracks
        with open(track_file) as file:
            reader = csv.reader(file)

            for row in reader:
                start = stations[row[0]]
                destination = stations[row[1]]
                critical = start.critical or destination.critical
                key = "{}-{}".format(row[0], row[1])
                track = Track(start, destination, row[2], critical, key)

                tracks.update({key: track})

                start.add_connection(track)
                destination.add_connection(track)

        return stations, tracks


    def get_num_of_tracks(self):
        if not self.num_of_critical:
            self.get_num_of_critical_tracks()
        return self.num_of_critical

    def get_track(self, station_a, station_b):

        key1 = "{}-{}".format(station_a.name, station_b.name)
        key2 = "{}-{}".format(station_b.name, station_a.name)

        if key1 in self.tracks:
            return self.tracks[key1]
        elif key2 in self.tracks:
            return self.tracks[key2]
        else:
            raise ValueError("No track found")

    # gets number of tracks that are critical
    def get_num_of_critical_tracks(self):
        num_of_critical = 0

        # separate critical from non-critical
        for key in self.tracks:
            if self.tracks[key].critical:
                num_of_critical += 1

        return num_of_critical

