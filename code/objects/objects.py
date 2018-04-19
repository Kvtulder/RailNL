def check_if_connected(tracks, station_a, station_b):
    for track in tracks:
        if track.station_a == station_a \
                and track.station_b == station_b \
                or track.station_a == station_b and track.station_b == station_a:

            return True
    # end of loop reached: no match
    return False

def get_time_between_stations(tracks, station_a, station_b):
    for track in tracks:
        if track.station_a == station_a and track.station_b == station_b \
               or track.station_a == station_b and track.station_b == station_a:
            return track.time

    # no match found -> no valid connection between stations. Return 0
    return 0









