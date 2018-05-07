import score
import Line
import random
import histogram


# creates a random solution with three constrains: n tracks with a max duration of
# n minutes, all the stations need to be connected and a line can't go backwards over
# # the same track.
# Returns the score and the generated lines
def random1(stations, tracks, num_of_lines, max_duration):
    lines = []
    used_tracks = {}

    for i in range(num_of_lines):
        # choose a random start position
        start = random.choice(list(stations))
        a = Line.Line([stations[start]])

        while a.total_time < max_duration:
            station = a.stations[-1]

            # create copy of dict to edit it without editing the original
            destinations = {**station.connections}

            while True:
                # choose a random destination
                destination = random.choice(list(destinations))

                # add track to list
                key1 = "{}-{}".format(station.name, destination)
                key2 = "{}-{}".format(destination, station.name)

                if key1 not in used_tracks and key2 not in used_tracks:
                    # track to the destination isnt already used: ready to go!
                    used_tracks.update({key1: 0})
                    break
                elif len(destinations) == 1:
                    # track is already used but no other possibility
                    break
                else:
                    # track is already used: try again
                    del(destinations[destination])

            a.add_station(stations[destination])

        # total time is over max: remove the last one to fulfill the constraints
        a.remove_last_station()
        lines.append(a)

    # create random line
    return score.get_score(lines, tracks), lines


