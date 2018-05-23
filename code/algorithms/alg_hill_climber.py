import copy
import algorithms as alg
import objects as obj
from score import score
import algorithms.helper.helper as helper
import run as run
import random


lines = []
used_tracks = {}


def hill_climber_random(steps, data, start_solution=None, change_amount=None):
    print("generating hill climber solution...", flush=True)

    if not start_solution:
        start_solution = alg.random2(data)

    solution = start_solution

    initial_score = solution.score
    start_lookup_table = solution.start_lookup_table

    score_evolution = []

    best_score = 0
    for step in range(steps):
        lookup_table = copy.copy(start_lookup_table)
        score_evolution.append(solution.score)

        new_solution = copy.copy(solution)

        # randomly choose two stations to remove
        for i in range(change_amount):
            new_solution.remove_line(random.choice(list(new_solution.lines)))

        # find new lines to complete the solution
        while len(new_solution.used_tracks) < data.num_crit_tracks and len(new_solution.lines) != data.num_of_lines:
            new_line = alg.random2(data, 1).lines[0]

            new_solution.add_line(new_line)

        # check if solution is better
        new_score = new_solution.score

        if new_score > best_score:
            best_score = new_score

            print("Improvement:", new_score)


    if initial_score == solution.score:
        solution.score = 0
        print("No improvement on orginal found")

    print("\t DONE")
    return solution

def hill_climber_greedy(steps, data, start_solution=None, change_amount=2):

    print("generating hill climber solution...", flush=True)

    if not start_solution:
        start_solution = alg.greedy_random(data)

    solution = start_solution

    print("start score:", solution.score)

    initial_score = solution.score
    start_lookup_table = solution.start_lookup_table

    score_evolution = []

    best_score = 0
    for step in range(steps):
        lookup_table = copy.copy(start_lookup_table)
        score_evolution.append(solution.score)

        new_solution = copy.copy(solution)

        # randomly choose two stations to remove
        for i in range(change_amount):
            new_solution.remove_line(random.choice(list(new_solution.lines)))

        # adapt lookup table to fit new situation
        for line in new_solution.lines:
            lookup_table = helper.update_lookup(line, lookup_table)

        # find new lines to complete the solution
        while len(new_solution.used_tracks) < data.num_crit_tracks and len(new_solution.lines) != data.num_of_lines:
            start_station = data.stations[random.choice(list(data.stations))]
            new_line = alg.greedy_search(start_station, data, lookup_table)

            new_solution.add_line(new_line)
            lookup_table = helper.update_lookup(line, lookup_table)

        # check if solution is better
        new_score = new_solution.score

        if new_score > best_score:
            best_score = new_score

            print("Improvement:", new_score)

    if initial_score == solution.score:
        solution.score = 0
        print("No improvement found")

    print("\t DONE")
    return solution
