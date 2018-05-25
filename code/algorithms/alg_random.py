import objects as obj
import random


def random1(data, num_of_lines=None, max_duration=None):
    """ creates a random solution with two constrains: n tracks with a max duration of
    n minutes and all the data.stations need to be connected.

    :argument data:         a class with all important static information about run, such as max_duration
    :argument num_of_lines  maximum number of lines that can be ridden
    :argument max_duration  maximum duration that lines can be

    :returns a solution with the score and the generated lines.
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


def random2(data, num_of_lines=None, max_duration=None):
    """ creates a random solution with two constrains: n tracks with a max duration of
    n minutes and all the data.stations need to be connected. Plus a line can't go backwards over
    the same track.

    :argument data:         a class with all important static information about run, such as max_duration
    :argument num_of_lines  maximum number of lines that can be ridden
    :argument max_duration  maximum duration that lines can be

    :returns a solution with the score and the generated lines.
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
