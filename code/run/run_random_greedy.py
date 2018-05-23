import algorithms as alg
import visualise as vis

def run_random_greedy(data, times=10000, print=True, map=False, line=False, hist=False):
    best_solution = None

    best_solutions_scores = []
    new_solutions_scores = []


    for i in range(times):
        new_solution = alg.greedy_random(data)

        if not best_solution:
            best_solution = new_solution
        elif new_solution.score > best_solution.score:
            best_solution = new_solution

        new_solutions_scores.append(new_solution.score)
        best_solutions_scores.append(best_solution.score)

        print(i, best_solution.score)

    vis.print_results(alg.greedy_random, best_solution, data)

    if map:
        vis.draw_map(data, best_solution.lines)

    if hist:
        vis.hist(new_solutions_scores, best_solution.lines)

    if line:
        vis.plot_line(best_solutions_scores)