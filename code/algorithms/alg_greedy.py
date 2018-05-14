import objects as obj
import algorithms.helper.helper as helper


# pure greedy search algorithm that searches best route from given station
# it looks to both ends
# constraints: cant return on itself
def greedy_search(station, data, lookup_table_tracks_score):
    used_connections = []
    ends = [station]

    new_line = obj.Line([station])

    line_completed = False
    while not line_completed:
        best_connections_ends = {}

        # find best connection for each end of route and then select best one
        for end in ends:
            connections = {**end.connections}

            best_connection_end = helper.select_best_scoring_connection(connections, lookup_table_tracks_score)

            while invalid(new_line, best_connection_end, used_connections, data):
                del connections[best_connection_end.key]

                if len(connections) == 0:
                    best_connection_end = None
                    break
                else:
                    best_connection_end = helper.select_best_scoring_connection(connections, lookup_table_tracks_score)

            best_connections_ends.update({end.name: best_connection_end})

        best_connection = helper.select_best_scoring_connection(best_connections_ends, lookup_table_tracks_score)

        if not best_connection:
            line_completed = True
            continue

        if best_connection.key in new_line.stations[0].connections:
            insert_position = "first"
        else:
            insert_position = "last"
        new_line.add_station_by_track(best_connection, insert_position)

        used_connections.append(best_connection.key)

        ends = [new_line.stations[0], new_line.stations[-1]]

    return trim_line(new_line, data, lookup_table_tracks_score)


# trims line so non-scoring tracks on the front or end of track are removed
def trim_line(line, data, lookup_table_tracks_score):
    front_done = False
    end_done = False

    while not end_done or not front_done:
        track_front = data.get_track(line.stations[0], line.stations[1])
        track_end = data.get_track(line.stations[-1], line.stations[-2])

        if not end_done:
            if lookup_table_tracks_score[track_end.key] < 0:
                line.stations.pop()
            else:
                end_done = True

        if not front_done:
            if lookup_table_tracks_score[track_front.key] < 0:
                line.stations.remove(line.stations[0])
            else:
                front_done = True

        if len(line.stations) < 2:
            break

    line.total_time = line.get_total_time()
    return line


# checks if route is valid
def invalid(line, connection, used_connections, data):

    if connection.key in used_connections or line.total_time + connection.duration > data.max_duration:
        return True
    else:
        return False