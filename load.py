# import libraries
import csv
import objects

# define constants
FILE_NAME_STATIONS = "data/StationsHolland.csv"
FILE_NAME_TRACKS = "data/ConnectiesHolland.csv"


# loads all the stations form the data in the csv file
def load_stations():

    stations = {}

    with open(FILE_NAME_STATIONS) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 3:
                stations.update({row[0]:objects.Station(row[0], row[1], row[2],row[3] == 'Kritiek')})
            else:
                stations.update({row[0]: objects.Station(row[0], row[1], row[2], False)})

    file.close()

    return stations


# loads all the tracks form the data in the csv file
def load_tracks(stations):

    tracks = []
    with open(FILE_NAME_TRACKS) as file:
        reader = csv.reader(file)
        for row in reader:
                if stations[row[0]].critical != False:
                    tracks.append(
                        objects.Track(get_station_by_name(stations, row[0]),
                                      get_station_by_name(stations, row[1]),
                                      row[2], True))
                else:
                    tracks.append(
                        objects.Track(get_station_by_name(stations, row[0]),
                                      get_station_by_name(stations, row[1]),
                                      row[2], False))
    file.close()

    return tracks


# searches a station in a list of stations
def get_station_by_name(stations, name):
    if name in stations:
        return stations[name]
    else:
        return False


# # searches sorted list through binary search
# def search_binary(stations, name):
#     if len(stations) == 0:
#         return False
#     else:
#         midpoint = len(stations)// 2
#
#         if stations[midpoint].name == name:
#             return stations[midpoint]
#         elif name < stations[midpoint].name:
#             return search_binary(stations[:midpoint], name)
#         elif name > stations[midpoint].name:
#             return search_binary(stations[midpoint + 1:], name)
#         else:
#             return False
