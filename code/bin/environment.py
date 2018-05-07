import csv
from objects.Station import Station
from objects.Track import Track

# define path files
station_file = "../data/StationsNationaal.csv"
track_file = "../data/ConnectiesNationaal.csv"

# create static variables:
tracks = {}
stations = {}

num_of_critical = None


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


def load():
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


# gets number of tracks that are critical
def get_num_of_critical_tracks():

    global num_of_critical
    num_of_critical = 0

    # separate critical from non-critical
    for key in tracks:
        if tracks[key].critical:
            num_of_critical += 1

    return num_of_critical

