import visualise as vis

def run_hill_climber(algorithm, data, times=10, steps=10000, start_solution=[], change_amount=2,
                     print_lines=True, map=False, line=False, hist=False):
    """ runs a hill-climber algorithm multiple times

    :argument algorithm:        the algorithm that is to be used, in this case of the greedy family
    :argument data:             a class with all important static information about run, such as max_duration
    :argument times:            times the algorithm is run
    :argument steps:            amount of steps the hill-climber takes
    :argument start_solution:   an already created solution serving as start point for the hill climber
    :argument change_amount:    amount of tracks that will be swapped in hill_climber_multi
    :argument print_lines:      determines if lines will be printed
    :argument map:              determines if map will be printed
    :argument line:             determines if line graph will be printed
    :argument hist:             determines if histogram will be printed

    :returns best solution with the score and the generated lines.
    """

    best_solution = None

    best_solutions_scores = []
    new_solutions_scores = []

    for i in range(times):
        if algorithm.__name__[-8:-12] == "multi":
            new_solution = algorithm(steps, data, start_solution, change_amount)
        else:
            new_solution = algorithm(steps, data, start_solution)

        if not best_solution:
            best_solution = new_solution
        elif new_solution.score > best_solution.score:
            best_solution = new_solution

        new_solutions_scores.append(new_solution.score)
        best_solutions_scores.append(best_solution.score)

        print("run:", i, best_solution.score)

    if print_lines:
        vis.print_results(algorithm, best_solution, data)

    if map:
        vis.draw_map(data, best_solution.lines)

    if hist:
        vis.hist(new_solutions_scores, best_solution.lines)

    if line:
        vis.plot_line(best_solutions_scores)


    return best_solution