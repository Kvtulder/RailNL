from score.score import get_score
from objects.Line import Line
import random
import bin.environment


# creates a random solution with two constrains: n tracks with a max duration of
# n minutes and all the stations need to be connected. Returns the score and
# the generated lines
def random1(num_of_lines, max_duration):
    stations = bin.environment.get_stations()
    tracks = bin.environment.get_tracks()

    lines = []

    for i in range(num_of_lines):
        start = random.choice(list(stations))
        a = Line([stations[start]])

        while a.total_time < max_duration:
            connections = a.stations[-1].connections
            track = tracks[random.choice(list(connections))]
            a.add_station_by_track(track)

        a.remove_last_station()
        lines.append(a)

    # create random line
    return score.get_score(lines, tracks), lines


# same as random1 but with a extra constraint: A line can't go backwards over
# the same track.
def random2(num_of_lines, max_duration):

    stations = bin.environment.get_stations()
    tracks = bin.environment.get_tracks()
    lines = []

    for i in range(num_of_lines):
        used_tracks = {}
        # choose a random start position
        start = random.choice(list(stations))
        a = Line([stations[start]])

        while a.total_time < max_duration:
            station = a.stations[-1]

            # create copy of dict to edit it without editing the original
            destinations = {**station.connections}

            while True:
                # choose a random destination
                destination = random.choice(list(destinations))

                # add track to list
                track = tracks[destination]
                key = track.key

                if key not in used_tracks:
                    # track to the destination isnt already used: ready to go!
                    used_tracks.update({key: 0})
                    break
                elif len(destinations) == 1:
                    # track is already used but no other possibility
                    break
                else:
                    # track is already used: try again
                    del(destinations[destination])

            a.add_station_by_track(track)

        # total time is over max: remove the last one to fulfill the constraints
        a.remove_last_station()
        lines.append(a)

    # create random line
    return get_score(lines), lines
