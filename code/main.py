import objects as obj
import algorithms as alg
import helper as helper
import run as run
import visualise as vis

def main():
    data = obj.Data("Nationaal", False)

    vis.draw_map(data)

    solution = run.run_random(alg.random2, data, 10000)
    #
    # run.run_greedy(alg.greedy_random, data, 100, helper.lookup_score, helper.invalid)
    #
    # run.run_hill_climber(alg.hill_climber_random, data, 1, 100, solution)


if __name__ == "__main__":
    main()
