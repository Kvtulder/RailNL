import copy
import random
from random import randint
import algorithms as alg
from score import score
import helper as helper


def hill_climber_random(steps, data, solution=None):
    """ Builds on a (random) starting route by replacing each existing line
    with a random new line, one by one

    :argument steps:        amount of times algorithm has to replace a line
    :argument data:         data class with all important static information about run, such as max_duration
    :argument solution:     a possible pre-existing solution, standard =None, then it will create

    :returns a solution containing lines, score and other board information
    """

    score_evolution = []

    print("generating hill climber solution...", end='', flush=True)

    # generate random solution
    if not solution:
        solution = alg.random2(data)

    for step in range(steps):
        score_evolution.append(solution.score)

        # make mutation
        for i in range(len(solution.lines)):
            new_solution = copy.copy(solution)
            new_solution.remove_line(new_solution.lines[i])
            new_solution.add_line(alg.random2(data, 1).lines[0])

            if new_solution.score > solution.score:
                solution = new_solution
                print("Improvement:", new_solution.score)

    print("\t DONE")
    return solution


def hill_climber_multi_greedy(steps, data, solution=None, change_amount=2):
    """ Builds on a starting route randomly deleting multiple routes and replacing them with new ones.


    :argument steps:        amount of times algorithm has to replace a line
    :argument data:         data class with all important static information about run, such as max_duration
    :argument change_amount:determines amount of lines swapped out
    :argument solution:     a possible pre-existing solution, standard =None, then it will create

    :returns a solution containing lines, score and other board information
    """

    # check if start solution was provided
    if not solution:
        solution = alg.greedy_random(data)

    initial_score = solution.score

    if not solution.lookup_table:
        start_lookup_table = data.lookup_table_function(data)
    else:
        start_lookup_table = solution.lookup_function(data)

    score_evolution = [initial_score]

    print("generating hill climber solution...", flush=True)

    print("start score:", initial_score)

    for step in range(steps):
        new_solution = copy.copy(solution)
        lookup_table = copy.copy(start_lookup_table)

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
            lookup_table = helper.update_lookup(new_line, lookup_table)

        # checks if new solution is better than old one
        if new_solution.score > solution.score:
            solution = new_solution
            print("Improvement:", new_solution.score)

        score_evolution.append(solution.score)

    if initial_score == solution.score:
        solution.score = 0
        print("No improvement found")

    print("\t DONE")

    return solution


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
