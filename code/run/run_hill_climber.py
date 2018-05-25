import visualise as vis

def run_hill_climber(algorithm, data, times=10, steps=10000, start_solution=[], print_lines=True, map=False, line=False, hist=False):
    best_solution = None

    best_solutions_scores = []
    new_solutions_scores = []

    for i in range(times):
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