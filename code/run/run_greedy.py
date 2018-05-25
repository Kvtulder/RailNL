import visualise as vis
import helper as helper


def run_greedy(algorithm, data, times=10000, lookup_function=helper.lookup_score,
               invalid_functie=helper.invalid, print_lines=True, map=False, line=False, hist=False):

    # set possible heuristics
    data.lookup_table_function = lookup_function
    data.invalid_function = invalid_functie

    if algorithm.__name__ == "recalculating_greedy" and\
            lookup_function.__name__ != "lookup_score_random":
        times = 1

    best_solution = None

    best_solutions_scores = []
    new_solutions_scores = []

    for i in range(times):
        new_solution = algorithm(data)

        if not best_solution:
            best_solution = new_solution
        elif new_solution.score > best_solution.score:
            best_solution = new_solution

        new_solutions_scores.append(new_solution.score)
        best_solutions_scores.append(best_solution.score)

    if print_lines:
        vis.print_results(algorithm, best_solution, data)

    if map:
        vis.draw_map(data, best_solution.lines)

    if hist:
        vis.hist(new_solutions_scores, best_solution.lines)

    if line:
        vis.plot_line(best_solutions_scores)

    return best_solution
