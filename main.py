# added folder structure
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from load import *
from alg_greedy import *
from alg_random import *

# prints tracks and total time
def print_results(results):
    print("\n")
    for result in results[1]:
        print("{}".format(result))
    print("Score: :", results[0])

# runs algorithms and logs results
def main():

    stations = load_stations()
    tracks = load_tracks(stations)

    greedy1_results = greedy1(stations, tracks, 22, 120)
    print_results(greedy1_results)

    greedy2_results = greedy2(stations, tracks, 22, 120)
    print_results(greedy2_results)

if __name__ == "__main__":
    main()


