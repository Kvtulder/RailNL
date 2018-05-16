from visualise.visualise import draw_map

def print_results(algorithm, results, data):
    print("\n")
    print(algorithm.__name__, "score:", results[0])
    print_stations(results[1])

    draw_map(data, results[1])

def print_stations(lines):

    for line in lines:
        print(line.total_time, ":", end='')
        for station in line.stations:
            print(station.name + ", ", end='')

        print("")
