import score
from objects.Line import Line
import random
import bin.environment
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy



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
    return score.get_score(lines, tracks), lines


def hist(NUM, algorithm):
    best_score = 0
    best_solution = None
    scores = []

    for i in range(NUM):
        test, lines = algorithm(7, 120)
        scores.append(test)
        if test > best_score:
            best_solution = lines

    standard_deviation = numpy.std(scores)
    average = sum(scores) / len(scores)

    n, bins, patches = plt.hist(scores, 30, normed=1)
    normalfit = mlab.normpdf(bins, average, standard_deviation)
    plt.plot(bins, normalfit, 'r')
    plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(
        f"Random algorithm; N={NUM:d}; $\mu$={average:f} $\sigma$={standard_deviation:f}")

    print("Random algorithm repeated {} times. Average score: {}."
          " Best score: {}".format(NUM, average, max(scores)))
    for line in best_solution:
        print("{}".format(line))
    plt.show()
