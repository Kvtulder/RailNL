# added folder structure
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "data"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from load import *
from alg_greedy import *
from alg_random import *
from alg_depth_first import *

# prints tracks and total time
def print_results(algorithm, results):
    print("\n")
    print(algorithm.__name__)
    for result in results[1]:
        print("{}".format(result))
    print("Score: :", results[0])

def run(algorithm, stations, tracks):
    num_of_lines = 7
    max_duration = 120

    results = algorithm(stations, tracks,num_of_lines, max_duration)

    print_results(algorithm, results)

# runs algorithms and logs results
def main():
    stations_file = "StationsHolland.csv"
    tracks_file = "ConnectiesHolland.csv"

    stations = load_stations(stations_file)
    tracks = load_tracks(tracks_file, stations)

    run(greedy2, stations, tracks)

    run(random2, stations, tracks)

    run(depth_first1, stations, tracks)


if __name__ == "__main__":
    main()


