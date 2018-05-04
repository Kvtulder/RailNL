import matplotlib.pyplot as plt

# draws histogram based on num(ber) of runs
def hist(given_function, num, stations, tracks, num_of_lines, max_duration):

    best_score = 0
    best_solution = None

    scores = []
    for i in range(num):
        test, lines = given_function(stations, tracks, num_of_lines, max_duration)
        scores.append(test)
        if test > best_score:
            best_solution = lines

        print(len(scores))
    plt.hist(scores, 30, normed=1)
    plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(f"given_function.__name__ algorithm; N={num:d}")

    print("{} algorithm repeated {} times. Average score: {}."
          " Best score: {}".format(given_function.__name__, num, sum(scores) / len(scores), max(scores)))
    for line in best_solution:
        print("{}".format(line))
    plt.show()