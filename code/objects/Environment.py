import csv
from objects.Station import Station
from objects.Track import Track

# define path files
station_file = "../../data/ConnectiesNationaal.csv"
track_file = "../../data/StationsNationaal.csv"

# create static variables:
tracks = {}
stations = {}


class Environment:
    @staticmethod
    def get_stations():
        if not stations:
            load()
        return stations

    @staticmethod
    def get_tracks():
        if not tracks:
            load()
        return tracks


def load():

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
