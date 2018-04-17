# calculates and returns the score of the current sollution
def get_score():
        # TODO: get the percentage of ridden critical tracks
        return 0


def check_if_connected(tracks, station_a, station_b):
    for track in tracks:
        if track.station_a == station_a \
                and track.station_b == station_b \
                or track.station_a == station_b and track.station_b == station_a:

            print("{} and {} are connected!".format(track.station_a.name, track.station_b.name))
            return True
    # end of loop reached: no match
    return False




