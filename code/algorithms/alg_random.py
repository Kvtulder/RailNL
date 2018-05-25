import objects as obj
import random

def random1(data, num_of_lines=None, max_duration=None):
    """
    Creates random lines with a maximum duration

    :param data: the data object containing information about the environment
    :param num_of_lines: the amount of lines to be created
    :param max_duration: the maximum duration of a single lines

    :return: a set of lines
    """
    if not num_of_lines:
        num_of_lines = data.num_of_lines

    if not max_duration:
        max_duration = data.max_duration

    solution = obj.Solution(data)

    for i in range(num_of_lines):
        start = random.choice(list(data.stations))
        a = obj.Line([data.stations[start]])

        while a.total_time < max_duration:
            connections = a.stations[-1].connections
            track = data.tracks[random.choice(list(connections))]
            a.add_station_by_track(track)

        a.remove_last_station()
        solution.add_line(a)

    # create random line
    return solution


# same as random1 but with a extra constraint: A line can't go backwards over
# the same track.
def random2(data, num_of_lines=None, max_duration=None):
    """
    Creates random lines with a maximum duration with a extra constraint:
    trains can't go back to their previous station

    :param data: the data object containing information about the environment
    :param num_of_lines: the amount of lines to be created
    :param max_duration: the maximum duration of a single lines

    :return: a set of lines
    """
    if not num_of_lines:
        num_of_lines = data.num_of_lines

    if not max_duration:
        max_duration = data.max_duration

    solution = obj.Solution(data)

    for i in range(num_of_lines):
        used_tracks = {}
        # choose a random start position
        start = random.choice(list(data.stations))
        a = obj.Line([data.stations[start]])


        while a.total_time < max_duration:
            station = a.stations[-1]

            # create copy of dict to edit it without editing the original
            destinations = {**station.connections}

            while True:
                # choose a random destination
                destination = random.choice(list(destinations))

                # add track to list
                track = data.tracks[destination]
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
        solution.add_line(a)

    # create random line
    return solution
