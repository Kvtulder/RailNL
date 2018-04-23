import score
from objects.Line import Line
import random
import matplotlib.pyplot as plt


# creates a random solution with two constrains: n tracks with a max duration of
# n minutes and all the stations need to be connected. Returns the score and
# the generated lines
def random1(stations, tracks, num_of_lines, max_duration, num_of_critital_tracks=None):
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
    return score.get_score(lines, tracks, num_of_critital_tracks), lines


# same as random1 but with a extra constraint: A line can't go backwards over
# the same track.
def random2(stations, tracks, num_of_lines, max_duration, num_of_critical_tracks=None):
    lines = []
    used_tracks = {}

    for i in range(num_of_lines):
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
    return score.get_score(lines, tracks, num_of_critical_tracks), lines


def hist(NUM):

    best_score = 0
    best_solution = None

    num_of_critical_tracks = score.get_num_of_critical_tracks(tracks)
    scores = []
    for i in range(NUM):
        test, lines = random2(7, 120, num_of_critical_tracks)
        scores.append(test)
        if test > best_score:
            best_solution = lines
    plt.hist(scores, 30, normed=1)
    plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(f"Random algorithm; N={NUM:d}")

    print("Random algorithm repeated {} times. Average score: {}."
          " Best score: {}".format(NUM, sum(scores) / len(scores), max(scores)))
    for line in best_solution:
        print("{}".format(line))
    plt.show()
