from score import score
import algorithms.greedy_helper as gh
import algorithms.helper.helper as helper
import algorithms as alg


# calculates best route for all station and selects best one
# removes score from used tracks and recalculates new best route
def recalculating_greedy(data, lookup_table=helper.lookup_score, invalid_function=gh.invalid):

    used_tracks = []
    best_lines = []

    # create lookup table for tracks with their score
    lookup_table_tracks_score = lookup_table(data)

    while len(used_tracks) < data.num_crit_tracks and len(best_lines) != data.num_of_lines:
        lines = []

        # create a line from each station
        for key, station in data.stations.items():
            best_station_line = alg.greedy_search(station, data, lookup_table_tracks_score, invalid_function)
            lines.append(best_station_line)

        best_line = helper.select_best_lines(lines, used_tracks, data, 1)

        if len(best_line.stations):
            used_tracks = helper.update_used(best_line, used_tracks, data, lookup_table_tracks_score)
            best_lines.append(best_line)

    return score.get_score(best_lines, data), best_lines














