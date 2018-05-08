import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy


# draws histogram based on num(ber) of runs
def hist(NUM, algorithm):
    best_score = 0
    best_solution = None
    scores = []

    for i in range(NUM):
        test, lines = algorithm(7, 120)
        scores.append(test)
        if test > best_score:
            best_solution = lines

    standard_deviation = numpy.std(scores)
    average = sum(scores) / len(scores)

    n, bins, patches = plt.hist(scores, 30, normed=1)
    normalfit = mlab.normpdf(bins, average, standard_deviation)
    plt.plot(bins, normalfit, 'r')
    plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(
        f"Random algorithm; N={NUM:d}; $\mu$={average:f} $\sigma$={standard_deviation:f}")

    print("Random algorithm repeated {} times. Average score: {}."
          " Best score: {}".format(NUM, average, max(scores)))
    for line in best_solution:
        print("{}".format(line))
    plt.show()
