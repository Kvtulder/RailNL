import copy
from alg_random import random2
import score
import environment


stations = environment.get_stations()
tracks = environment.get_tracks()
lines = []
used_tracks = {}


def hill_climber_random(steps):
    num_of_lines = environment.num_of_lines

    print("generating hill climber solution...", end='', flush=True)

    # generate random solution
    solution_score, solution = random2()

    score_evolution = []

    for step in range(steps):
        score_evolution.append(solution_score)

        # make mutation
        for i in range(num_of_lines):

            new_solution = copy.copy(solution)
            new_solution[i] = random2(1)[1][0]

            new_score = score.get_score(new_solution)

            if new_score > solution_score:
                solution = new_solution
                solution_score = new_score

    print("\t DONE")
    return solution_score, solution, score_evolution
