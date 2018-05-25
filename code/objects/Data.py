import csv
import objects as obj
import helper as helper
import test_tools as tt

class Data:
    def __init__(self, scope="Nationaal", all_critical=False, invalid_function=helper.invalid,
                 lookup_table_function=helper.lookup_score):
        self.max_tracks = 12

        self.stations = {}
        self.tracks = {}

        self.station_file = None
        self.track_file = None

        # sets scale of board
        self.set_scope(scope, all_critical)

        # gets variable unique for this board
        self.num_crit_tracks = self.get_num_of_critical_tracks()
        self.points_per_crit = 1/self.num_crit_tracks * 10000
        self.upperbound = tt.upperboundz(self)

        # set parameters for greedy function
        self.invalid_function = invalid_function
        self.lookup_table_function = lookup_table_function

    def set_scope(self, scope, all_critical):
        if scope == "Nationaal":
            self.max_duration = 180
            self.num_of_lines = 20
        else:
            self.max_duration = 120
            self.num_of_lines = 7

        self.station_file = "./data/Stations" + scope + ".csv"
        self.track_file = "./data/Connecties" + scope + ".csv"

        self.load(all_critical)


    def load(self, all_critical=False):
        print("loading stations and tracks...", end='', flush=True)
        # add all stations
        with open(self.station_file) as file:
            reader = csv.reader(file)
            for row in reader:
                # check if there is a critical row
                if len(row) > 3:
                    self.stations.update({
                        row[0]: obj.Station(row[0], row[1], row[2],
                                        row[3] == 'Kritiek' or all_critical)})
                else:
                    self.stations.update({
                        row[0]: obj.Station(row[0], row[1], row[2], all_critical)})

        # add all tracks
        with open(self.track_file) as file:
            reader = csv.reader(file)

            for row in reader:
                start = self.stations[row[0]]
                destination = self.stations[row[1]]
                critical = start.critical or destination.critical
                key = "{}-{}".format(row[0], row[1])
                track = obj.Track(start, destination, row[2], critical, key)

                self.tracks.update({key: track})

                start.add_connection(track)
                destination.add_connection(track)

        print("\t\t DONE")


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

    # takes 2d list with variables and their name
    # creates variables in data
    def set_test_variables(self, variables):
        for var in variables:
            setattr(Data, var[1], var[0])




