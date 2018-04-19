# import libraries
import csv
from objects.Station import Station
from objects.Track import Track


# define constants
FILE_NAME_STATIONS = "../data/StationsHolland.csv"
FILE_NAME_TRACKS = "../data/ConnectiesHolland.csv"


# loads all the stations form the data in the csv file
def load_stations():

    stations = {}

    with open(FILE_NAME_STATIONS) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2],row[3] == 'Kritiek')})
            else:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2], False)})
    return stations


# loads all the tracks form the data in the csv file
def load_tracks(stations):

    tracks = {}

    row_id = 0

    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)
        for row in reader:

            if stations[row[0]].critical != False:
                tracks.update({
                    row_id : Track(row_id, get_station_by_name(stations, row[0]),
                                   get_station_by_name(stations, row[1]), row[2],
                                   True)})
            else:
                tracks.update({
                    row_id : Track(row_id, get_station_by_name(stations, row[0]),
                                   get_station_by_name(stations, row[1]), row[2],
                                   False)})

            row_id += 1
    return tracks


# searches a station in a list of stations
def get_station_by_name(stations, name):
    if name in stations:
        return stations[name]
    else:
        return False
