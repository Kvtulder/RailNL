import score
import helper
import alg_greedy
import environment


def recalculating_greedy():
    stations = environment.get_stations()

    num_of_lines = environment.num_of_lines
    num_crit_tracks = environment.get_num_of_tracks()

    used_tracks = []
    best_lines = []

    # create lookup table for tracks with their score
    lookup_table_tracks_score = helper.lookup_score()

    while len(used_tracks) < num_crit_tracks and len(best_lines) != num_of_lines:
        lines = []

        # create a line from each station
        for key, station in stations.items():
            lines.append(alg_greedy.greedy_search(station, lookup_table_tracks_score))

        best_line = helper.select_best_lines(lines, used_tracks, 1)
        used_tracks = helper.update_used(best_line, used_tracks, lookup_table_tracks_score)

        best_lines.append(best_line)

    return score.get_score(best_lines), best_lines




