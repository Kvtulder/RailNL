def print_results(algorithm, results):
    print("\n")
    print(algorithm.__name__)
    for result in results[1]:
        print("{}".format(result))
    print("Score: :", results[0])