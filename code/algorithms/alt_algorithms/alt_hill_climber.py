import copy
import random
import algorithms as alg
import helper as helper


def alt_hill_climber_greedy(steps, data, solution=None):
    """ Builds on a starting route by replacing each existing line
    with a new greedy line, one by one. Is roughly equivalent to random function
    in main hill_climber file, but has been found to work less wel with greedy

    :argument steps:        amount of times algorithm has to replace a line
    :argument data:         data class with all important static information about run, such as max_duration
    :argument solution:     a possible pre-existing solution, standard =None, then it will create

    :returns a solution containing lines, score and other board information
    """

    print("generating hill climber solution...", end='', flush=True)

    if not solution:
        start_lookup_table = data.lookup_table_function(data)
        # generate random solution
        solution = alg.greedy_random(data)
    else:
        start_lookup_table = solution.lookup_function(data)

    for step in range(steps):
        lookup_table = copy.copy(start_lookup_table)

        # make mutation
        for i in range(len(solution.lines)):

            new_solution = copy.copy(solution)
            new_solution.remove_line(new_solution.lines[i])

            start_station = data.stations[random.choice(list(data.stations))]
            new_line = alg.greedy_search(start_station, data, lookup_table)

            new_solution.add_line(new_line)
            lookup_table = helper.update_lookup(new_line, lookup_table)

            if new_solution.score > solution.score:
                solution = new_solution
                print("Improvement:", new_solution.score)
            print(":", new_solution.score)

    print("\t DONE")
    return solution


def alt_hill_climber_multi_random(steps, data, solution=None, change_amount=2):
    """ Builds on a starting route randomly deleting multiple routes and replacing them with new ones.
    Is roughly equivalent to greedy function in main hill_climber file,
    but has been found to work less wel with random

    :argument steps:        amount of times algorithm has to replace a line
    :argument data:         data class with all important static information about run, such as max_duration
    :argument change_amount:determines amount of lines swapped out
    :argument solution:     a possible pre-existing solution, standard =None, then it will create

    :returns a solution containing lines, score and other board information
    """

    # check if start solution was provided
    if not solution:
        solution = alg.random2(data)

    initial_score = solution.score

    score_evolution = [initial_score]

    print("generating hill climber solution...", flush=True)
    print("start score:", initial_score)

    for step in range(steps):
        score_evolution.append(solution.score)

        new_solution = copy.copy(solution)

        # randomly choose two stations to remove
        for i in range(change_amount):
            new_solution.remove_line(random.choice(list(new_solution.lines)))

        # find new lines to complete the solution
        while len(new_solution.used_tracks) < data.num_crit_tracks and len(new_solution.lines) != data.num_of_lines:
            new_line = alg.random2(data, 1).lines[0]

            new_solution.add_line(new_line)

        # checks if new solution is better than old one
        if new_solution.score > solution.score:
            solution = new_solution
            print("Improvement:", new_solution.score)

        score_evolution.append(solution.score)

    if initial_score == solution.score:
        solution.score = 0
        print("No improvement found")

    print("\t DONE")

    return solution, score_evolution

