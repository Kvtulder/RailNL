from score import score
import algorithms.greedy_helper as gh
import algorithms.helper.helper as helper
import algorithms as alg
import objects as obj
import random

# supplies greedy algorithm with random start stations to form line
def greedy_random(data):

    # create lookup table for tracks with their score
    lookup_table = data.lookup_table_function(data)

    # create object to collect all routes and used_tracks in
    solution = obj.Solution(data, lookup_table)

    # create greedy lines from random start stations to complete set of lines (solution)
    while len(solution.used_tracks) < data.num_crit_tracks and len(solution.lines) != data.num_of_lines:
        start_station = data.stations[random.choice(list(data.stations))]

        station_line = alg.greedy_search(start_station, data, lookup_table)

        if len(station_line.stations) > 0:
            # adds line and updates lookup table and used_tracks
            solution.add_line(station_line)

            # update lookup table to resemble new reality
            lookup_table = helper.update_lookup(station_line, lookup_table)

    solution.lookup_table = lookup_table

    return solution
