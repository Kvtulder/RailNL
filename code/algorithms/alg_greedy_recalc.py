
import algorithms.helper.helper as helper
import algorithms as alg
import objects as obj


# calculates best route for all station and selects best one
# removes score from used tracks and recalculates new best route
def recalculating_greedy(data):
    used_tracks = []

    # create lookup table for tracks with their score
    lookup_table = data.lookup_table_function(data)

    solution = obj.Solution(data, lookup_table)

    while len(solution.used_tracks) < data.num_crit_tracks and len(solution.lines) != data.num_of_lines:
        possible_lines = []

        # create a line from each station
        for key, station in data.stations.items():
            best_station_line = alg.greedy_search(station, data, lookup_table)
            possible_lines.append(best_station_line)

        best_line = helper.select_best_lines(possible_lines, solution.used_tracks, data, 1)

        if len(best_line.stations):
            used_tracks = helper.update_used(best_line, used_tracks, lookup_table)
            solution.add_line(best_line)

    solution.lookup_table = lookup_table

    return solution














