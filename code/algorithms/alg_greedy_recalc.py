import helper as helper
import algorithms as alg
import objects as obj



def recalculating_greedy(data):
    """ Calculates solution by calculating a greedy route for each station and choosing the highest scoring
    Tracks of this route get there score removed and then calculates the best greedy route in this situation.
    It combines these until all critical tracks are ridden on.

    :argument data:   ata class with all important static information about run, such as max_duration

    :returns a solution containing lines, score and other board information
    """

    # create lookup table for tracks with their score
    lookup_table = data.lookup_table_function(data)

    solution = obj.Solution(data)

    while solution.num_of_crit < data.num_crit_tracks and len(solution.lines) != data.num_of_lines:
        possible_lines = []

        # create a line from each station
        for key, station in data.stations.items():
            best_station_line = alg.greedy_search(station, data, lookup_table)
            possible_lines.append(best_station_line)

        best_line = helper.select_best_lines(possible_lines, solution.used_tracks, data, 1)

        if len(best_line.stations):
            solution.add_line(best_line)
            helper.update_lookup(best_line, lookup_table)


    return solution














