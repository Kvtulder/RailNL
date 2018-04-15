# import libraties
import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# define constants

FILE_NAME_STATIONS = "data/StationsNationaal.csv"
FILE_NAME_TRACKS = "data/ConnectiesNationaal.csv"

MAP_TOP_BOUNDARY = 53.7
MAP_BOTTOM_BOUNDARY = 50.7
MAP_LEFT_BOUNDARY = 3.2130
MAP_RIGHT_BOUNDARY = 7.3


# define objects
class Station:
    def __init__(self, name, latitude, longitude, critical):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.critical = critical


class Track:
    def __init__(self, stationA, stationB, time):
        self.stationA = stationA
        self.stationB = stationB
        self.time = time


# loads all the stations form the data in the csv file
def load_stations():

    stations = []

    with open(FILE_NAME_STATIONS) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                stations.append(Station(row[0], row[1], row[2],
                                     row[3] == 'Kritiek'))
            else:
                stations.append(Station(row[0], row[1], row[2], False))
    return stations


# loads all the tracks form the data in the csv file
def load_tracks():

    tracks = []
    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)
        for row in reader:
                tracks.append(Track(row[0], row[1], row[2]))
    return tracks


# searches a station in a list of stations
def get_station_by_name(stations, name):
    for station in stations:
        if station.name == name:
            return station


# Draws a map of the Netherslands with all stations and tracks
def visualise(stations, tracks):

    lat = []
    long = []
    latcritical = []
    longcritical = []

    # sort stations in two lists: critical and non-critical
    for station in stations:
        if station.critical:
            latcritical.append(float(station.latitude))
            longcritical.append(float(station.longitude))
        else:
            lat.append(float(station.latitude))
            long.append(float(station.longitude))

    # draw a map of the netherlands
    my_map = Basemap(projection='merc', resolution='h', area_thresh=30,
                     llcrnrlon=MAP_LEFT_BOUNDARY, llcrnrlat=MAP_BOTTOM_BOUNDARY,
                     urcrnrlon=MAP_RIGHT_BOUNDARY, urcrnrlat=MAP_TOP_BOUNDARY)

    # fill the map
    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='moccasin')

    # draw the lines between the stations
    for track in tracks:
        station_a = get_station_by_name(stations, track.stationA)
        station_b = get_station_by_name(stations, track.stationB)

        x1, y1 = my_map(float(station_a.longitude),
                        float(station_a.latitude))
        x2, y2 = my_map(float(station_b.longitude),
                        float(station_b.latitude))

        plt.plot([x1, x2], [y1, y2], 'grey')

    # plot the stations as points
    x, y = my_map(long, lat)
    plt.plot(x, y, 'ro', markersize=4, label="Kritieke stations")
    x, y = my_map(longcritical, latcritical)
    plt.plot(x, y, 'bo', markersize=4, label="Niet-kritieke stations")
    plt.show()


visualise(load_stations(), load_tracks())
