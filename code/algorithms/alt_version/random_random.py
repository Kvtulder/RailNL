# version of random that is completely random so, tracks can be ridden multiple times
# this in contrast with the main version, where this constraint was added

import score
import Line
import random


# creates a random solution with two constrains: n tracks with a max duration of
# n minutes and all the stations need to be connected. Returns the score and
# the generated lines
def random_random(stations, tracks, num_of_lines, max_duration):
    lines = []

    for i in range(num_of_lines):
        start = random.choice(list(stations))
        a = Line([stations[start]])

        while a.total_time < max_duration:
            connections = a.stations[-1].connections
            destination = random.choice(list(connections))

            a.add_station(stations[destination])

        a.remove_last_station()
        lines.append(a)

    # create random line
    return score.get_score(lines, tracks), lines
