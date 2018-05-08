import csv
from objects.Station import Station
from objects.Track import Track

# define default path files
station_file = "../data/StationsNationaal.csv"
track_file = "../data/ConnectiesNationaal.csv"

# create variables:
tracks = {}
stations = {}
num_of_critical = None


def set_holland(all_critical=False):
    set_custom_data("../data/StationsHolland.csv",
                    "../data/ConnectiesHolland.csv", all_critical)


def set_national(all_critical=False):
    set_custom_data("../data/StationsNationaal.csv",
                    "../data/ConnectiesNationaal.csv", all_critical)


def set_custom_data(station, track, all_critical=False):
    global station_file
    global track_file
    global tracks
    global stations

    # reset all stations
    stations = {}
    tracks = {}

    # reload with new data
    station_file = station
    track_file = track
    load(all_critical)


def get_stations():
    if not stations:
        load()
    return stations


def get_tracks():
    if not tracks:
        load()
    return tracks


def get_num_of_tracks():
    if not num_of_critical:
        get_num_of_critical_tracks()
    return num_of_critical


def get_track(station_a, station_b):

    if not tracks:
        load()

    key1 = "{}-{}".format(station_a.name, station_b.name)
    key2 = "{}-{}".format(station_b.name, station_a.name)

    if key1 in tracks:
        return tracks[key1]
    elif key2 in tracks:
        return tracks[key2]
    else:
        raise ValueError("No track found")


def load(all_critical=False):
    print("loading stations and tracks...", end='', flush=True)
    # add all stations
    with open(station_file) as file:
        reader = csv.reader(file)
        for row in reader:
            # check if there is a critical row
            if len(row) > 3:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2],
                                    row[3] == 'Kritiek' or all_critical)})
            else:
                stations.update({
                    row[0]: Station(row[0], row[1], row[2], all_critical)})

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

    print("\t\t DONE")


# gets number of tracks that are critical
def get_num_of_critical_tracks():

    global num_of_critical
    num_of_critical = 0

    # separate critical from non-critical
    for key in tracks:
        if tracks[key].critical:
            num_of_critical += 1

    return num_of_critical

