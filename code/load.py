# import libraries
import csv
from objects.Station import Station
from objects.Track import Track


# define constants
FILE_NAME_STATIONS = "./data/StationsHolland.csv"
FILE_NAME_TRACKS = "./data/ConnectiesHolland.csv"


# loads all the stations form the data in the csv file
def load_stations(station_file):
    station_file = "./data/" + station_file

    stations = {}

    # add all stations
    with open(station_file) as file:
        reader = csv.reader(file)
        for row in reader:
            # check if there is a critical row
            if len(row) > 3:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2],row[3] == 'Kritiek')})
            else:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2], False)})

    # add all the connections to the stations
    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)
        for row in reader:

            station = stations.get(row[0])
            destination = stations.get(row[1])
            critical = station.critical or destination.critical
            station.add_connection(Track(destination, row[2], critical))
            destination.add_connection(Track(station, row[2], critical))

    return stations


# loads all the tracks form the data in the csv file
def load_tracks(track_file, stations):
    track_file = "./data/" + track_file

    tracks = {}

    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)

        for row in reader:
            station = stations[row[0]]
            destination = stations[row[1]]
            critical = station.critical or destination.critical
            key = "{}-{}".format(row[0], row[1])

            tracks.update({key : Track(destination, row[2], critical, station)})

    return tracks
