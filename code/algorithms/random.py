import random


def create_random_lines(stations, lines, max_time):

    for line in lines:
        print("{}".format(line))
        start = random.choice(list(stations))
        line.add_station(stations[start])

        while line.total_time < max_time:

            connections = line.stations[-1].connections
            destination = random.choice(list(connections))
            line.add_station(stations[destination])

        line.remove_last_station()
        print("{}".format(line))

    return lines