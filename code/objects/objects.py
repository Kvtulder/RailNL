def check_if_connected(tracks, station_a, station_b):
    for track in tracks:
        if track.station_a == station_a \
                and track.station_b == station_b \
                or track.station_a == station_b and track.station_b == station_a:

<<<<<<< HEAD
            return True
    # end of loop reached: no match
    return False

def get_time_between_stations(tracks, station_a, station_b):
    for track in tracks:
        if track.station_a == station_a and track.station_b == station_b \
               or track.station_a == station_b and track.station_b == station_a:
            return track.time
=======
# define objects
class Station:
    def __init__(self, name, latitude, longitude, critical):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.critical = critical
>>>>>>> 07e3f167d27a0a86e6e67edd52e888a4317aa0b9

    # no match found -> no valid connection between stations. Return 0
    return 0

<<<<<<< HEAD
=======
class Track:
    def __init__(self, id, station_a, station_b, time, critical):
        self.id = id
        self.station_a = station_a
        self.station_b = station_b
        self.time = float(time)
        self.critical = critical
>>>>>>> 07e3f167d27a0a86e6e67edd52e888a4317aa0b9








