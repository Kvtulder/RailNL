import objects as obj
import helper as helper


# pure greedy search algorithm that searches best route from given station
# it looks to both ends
# constraints: cant return on itself
def greedy_search(station, data, lookup_table):
    """ Searches for the best route from given station. It does this be choosing the connection
    with the highest given score, which are located in the lookup table.

    :argument station:      station to start route from
    :argument data:         overall information
    :argument lookup_table: a dict holding within it each track and its corresponding score


    :returns a line containing its track, station and duration
    """

    ends = [station]
    new_line = obj.Line([station])
    line_completed = False

    while not line_completed:
        new_connections = {}

        # find both end of route and collect all connections
        for end in ends:
            new_connections.update({**end.connections})

        best_connection = helper.select_best_scoring_connection(new_connections, lookup_table)

        # check if adding connection would be allowed in constraint
        while data.invalid_function(new_line, best_connection, data):
            del new_connections[best_connection.key]

            if len(new_connections) == 0:
                line_completed = True
                break
            else:
                best_connection = helper.select_best_scoring_connection(new_connections, lookup_table)

        if line_completed:
            continue
        elif best_connection.key in new_line.stations[0].connections:
            new_line.add_station_by_track(best_connection, "first")
        else:
            new_line.add_station_by_track(best_connection, "last")

        ends = [new_line.stations[0], new_line.stations[-1]]

    return trim_line(new_line, data, lookup_table)


# trims line so non-scoring tracks on the front or end of track are removed
def trim_line(line, data, lookup_table):
    front_done = False
    end_done = False

    if len(line.stations) < 2:
        return line

    while not end_done or not front_done:
        track_front = data.get_track(line.stations[0], line.stations[1])
        track_end = data.get_track(line.stations[-1], line.stations[-2])

        if not end_done:
            if lookup_table[track_end.key] < 0:
                line.stations.pop()
            else:
                end_done = True

        if not front_done:
            if lookup_table[track_front.key] < 0:
                line.stations.remove(line.stations[0])
            else:
                front_done = True

        if len(line.stations) < 2:
            break

    line.total_time = line.get_total_time()
    return line


