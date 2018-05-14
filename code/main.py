# added folder structure
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "data_load"))
sys.path.append(os.path.join(directory, "code", "score"))
sys.path.append(os.path.join(directory, "code", "visualise"))
sys.path.append(os.path.join(directory, "code", "bin"))
sys.path.append(os.path.join(directory, "code", "algorithms", "helper"))

import print_results
from alg_recalc_greedy import recalculating_greedy
from alg_random import random2
from alg_hill_climber import hill_climber_random


results = recalculating_greedy()

print_results.print_results(recalculating_greedy, results)
results = hill_climber_random(100)

print_results.print_results(random2, results[:2])
