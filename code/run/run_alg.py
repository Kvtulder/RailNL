
import visualise as vis

def run_alg(algorithm, data, print_lines=True, map=False, line=False, hist=False):
    best_solution = algorithm(data)

    if print_lines:
        vis.print_results(algorithm, best_solution, data)

    if map:
        vis.draw_map(data, best_solution.lines)


    return best_solution