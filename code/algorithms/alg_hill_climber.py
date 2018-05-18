import copy
from algorithms.alg_random import random2
from score.score import get_score
import random
import bin.environment


stations = bin.environment.get_stations()
tracks = bin.environment.get_tracks()
lines = []
used_tracks = {}

def random_number(a, b):
    if a > b:
        print("Invalid interval")
        return -1
    return (b - a) * random.random() + a


def hill_climber_random(num_of_lines, max_duration, steps):



    print("generating hill climber solution...", end='', flush=True)

    # generate random solution
    score, solution = random2(num_of_lines, max_duration)

    score_evolution = []

    for step in range(steps):
        score_evolution.append(score)

        # make mutation
        for i in range(num_of_lines):

            new_solution = copy.copy(solution)

            new_solution[i] = random2(1, random_number(0, max_duration))[1][0]

            new_score = get_score(new_solution)

            if new_score > score:
                solution = new_solution
                score = new_score



    print("\t DONE")
    return score, solution, score_evolution
