from score import score
import algorithms.helper.helper as helper
import algorithms as alg


def recalculating_greedy(data, num_of_lines=None):

    if not num_of_lines:
        num_of_lines = data.num_of_lines

    num_crit_tracks = data.num_crit_tracks

    used_tracks = []
    best_lines = []

    # create lookup table for tracks with their score
    lookup_table_tracks_score = helper.lookup_score2(data)

    while len(used_tracks) < num_crit_tracks and len(best_lines) != num_of_lines:
        lines = []

        # create a line from each station
        for key, station in data.stations.items():
            lines.append(alg.greedy_search(station, data, lookup_table_tracks_score))

        best_line = helper.select_best_lines(lines, used_tracks, data, 1)
        used_tracks = helper.update_used(best_line, used_tracks, data, lookup_table_tracks_score)

        best_lines.append(best_line)

    return score.get_score(best_lines, data), best_lines




