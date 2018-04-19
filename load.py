# import libraties
import csv
import objects

# define constants
FILE_NAME_STATIONS = "data/StationsHolland.csv"
FILE_NAME_TRACKS = "data/ConnectiesHolland.csv"


# loads all the stations form the data in the csv file
def load_stations():

    stations = []

    with open(FILE_NAME_STATIONS) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                stations.append(objects.Station(row[0], row[1], row[2],
                                     row[3] == 'Kritiek'))
            else:
                stations.append(objects.Station(row[0], row[1], row[2], False))
    return stations


# loads all the tracks form the data in the csv file
def load_tracks(stations):

    tracks = []
    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)
        for row in reader:
                tracks.append(
                    objects.Track(get_station_by_name(stations, row[0]),
                                  get_station_by_name(stations, row[1]),
                                  row[2]))
    return tracks


# searches a station in a list of stations
def get_station_by_name(stations, name):
    # TODO better algorithm? list is sorted -> binary sort
    for station in stations:
        if station.name == name:
            return station
