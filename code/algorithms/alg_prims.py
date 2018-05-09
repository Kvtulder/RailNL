import score
import helper
from Line import Line


def prim(data):
    used_tracks = []
    best_lines = []

    lookup_table_tracks_score = helper.lookup_score(data)

    while len(used_tracks) < data.num_crit_tracks and len(best_lines) != data.num_of_lines:
        lines = greedy_search(data, lookup_table_tracks_score)

        best_line = helper.select_best_lines(lines, data, used_tracks, 1)
        used_tracks = helper.update_used(best_line, used_tracks, data, lookup_table_tracks_score)


        best_lines.append(best_line)

    return score.get_score(best_lines, data), best_lines


def greedy_search(data, lookup_table_tracks_score):
    lines = []

    for key, station in data.stations.items():
        used_connections = []
        ends = [station]

        new_line = Line([station])

        line_completed = False
        while not line_completed:
            best_connections_ends = {}

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

        lines.append(trim_line(new_line, lookup_table_tracks_score, data))

    return lines


def trim_line(line, lookup_table_tracks_score, data):
    front_done = False
    end_done = False

    i = 0

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
                line.stations.remove(line.stations[i])
            else:
                front_done = True

        if len(line.stations) < 2:
            break

    line.total_time = line.get_total_time()
    return line

def best_connection_ends(ends, lookup_table, line, used_connections, data, invalid):
    best_connections_ends = {}

    for end in ends:
        connections = {**end.connections}

        best_connection_end = select_best_scoring_connection(connections, lookup_table)

        if invalid(line, best_connection_end, used_connections, data):
            del connections[best_connection_end.key]
            select_best_scoring_connection(connections, lookup_table)
        else:
            best_connections_ends.update({end.key: best_connection_end})

    best_connection = select_best_scoring_connection(best_connections_ends)

    return best_connection





def invalid(line, connection, used_connections, data):
    if connection.key in used_connections or line.total_time + connection.duration > data.max_duration:
        return True
    else:
        return False


