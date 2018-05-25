
import objects as obj
import algorithms as alg
import helper as helper
import run as run

data = obj.Data("Nationaal", False)
data.lookup_table_function = helper.lookup_score
data.invalid_function = helper.invalid

results = run.run_random_alg(alg.greedy_random, data, 100)
# run.run_random_alg(alg.greedy_random, data, 100, True, False, True, True)
run.run_hill_climber(alg.hill_climber_random, data, 10, 1000)
