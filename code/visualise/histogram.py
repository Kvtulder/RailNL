import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy


# draws histogram based on num(ber) of runs

def hist(results, best_solution):

    num = len(results)
    scores = results


    standard_deviation = numpy.std(scores)
    average = sum(scores) / len(scores)

    n, bins, patches = plt.hist(scores, 30)
    normalfit = mlab.normpdf(bins, average, standard_deviation)
    plt.plot(bins, normalfit, 'r')
    plt.xlabel("Score")
    plt.ylabel("Probability")
    plt.title(f"Random algorithm; N={num:d}; "
              f"$\mu$={average:f} $\sigma$={standard_deviation:f}")

    print("Random algorithm repeated {} times. Average score: {}."
          " Best score: {}".format(num, average, max(scores)))
    plt.show()
