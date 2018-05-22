import copy
import algorithms as alg
from score import score
from random import randint

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


def hill_climber_mutation(steps, data, solution=None):

    print("generating hill climber solution...", end='', flush=True)

    if not solution:
        solution_score, solution, evolution = hill_climber_random(1000, data)

    solution_score = score.get_score(solution, data)

    score_evolution = []

    for step in range(steps):
        score_evolution.append(solution_score)

        # make mutation
        for i in range(len(solution)):

            new_solution = copy.copy(solution)

            length = randint(2, len(new_solution.stations))
            start = randint(0, len(new_solution.stations) - length)
            end = start + length

            start_station = new_solution.get_station(start)
            end_station = new_solution.get_station(end)

            route = alg.depth_first()


            new_solution[i] = alg.random2(data, 1)[1][0]
            new_score = score.get_score(new_solution, data)

            if new_score > solution_score:
                solution = new_solution
                solution_score = new_score

    print("\t DONE")
    return solution_score, solution, score_evolution