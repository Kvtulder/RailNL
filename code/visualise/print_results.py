
def print_results(algorithm, solution, data):
    print("\n")
    print_stations(solution.lines)
    print("theoretical upperbound:", data.upperbound)
    print(algorithm.__name__, "score:", solution.score)


def print_stations(lines):

    for line in lines:
        print("{}".format(line))

