import copy
import algorithms as alg
from score import score
import random


lines = []
used_tracks = {}


def hill_climber_random(steps, data):

    print("generating hill climber solution...", end='', flush=True)

    # generate random solution
    solution_score, solution = alg.random2(data)

    score_evolution = []

    for step in range(steps):
        score_evolution.append(solution_score)

        # make mutation
        for i in range(len(solution)):

            new_solution = copy.copy(solution)
            new_solution[i] = alg.random2(data, 1)[1][0]

            new_score = score.get_score(new_solution, data)

            if new_score > solution_score:
                solution = new_solution
                solution_score = new_score

    print("\t DONE")
    return solution_score, solution, score_evolution

def hill_climber_greedy(steps, data, lookup_table_function, invalid_function):

    print("generating hill climber solution...", end='', flush=True)

    # generate random solution
    solution_score, solution = alg.recalculating_greedy(data, lookup_table_function)

    lookup_table = lookup_table_function(data)


    score_evolution = []

    for step in range(steps):
        score_evolution.append(solution_score)

        # make mutation
        for i in range(len(solution)):

            new_solution = copy.copy(solution)

            start_station = data.stations[random.choice(list(data.stations))]


            new_solution[i] = alg.random2(data, 1)[1][0]

            new_score = score.get_score(new_solution, data)

            if new_score > solution_score:
                solution = new_solution
                solution_score = new_score


    print("\t DONE")
    return solution_score, solution, score_evolution
