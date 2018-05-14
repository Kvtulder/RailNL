# added folder structure

import objects as obj
import algorithms as alg
import test_tools as tt
import visualise as vis


data = obj.Data()

vis.print_results(alg.hill_climber_random, alg.hill_climber_random(10 ,data))

tt.multiple_runs(100, alg.recalculating_greedy, data)
tt.multiple_runs(100, alg.random2, data)


