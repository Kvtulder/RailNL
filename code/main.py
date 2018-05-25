import objects as obj
import algorithms as alg
import helper as helper
import run as run
'''
Callable algorithms:
alg.random2
alg.greedy_random
alg.recalculating_greedy
alg.hill_climber_random
alg.hill_climber_multi_greedy
alg.hill_climber_mutation
'''

def main():
    map = "Nationaal"
    critical = False

    data = obj.Data(map, critical)
    solution = run.run_random(alg.random2, data, 10)

    run.run_greedy(alg.greedy_random, data, 100, helper.lookup_score, helper.invalid)

    run.run_hill_climber(alg.hill_climber_random, data, 1, 100, solution)


if __name__ == "__main__":
    main()
