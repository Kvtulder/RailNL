import matplotlib.pyplot as plt
import numpy as np


def f(z):

    Z = []

    for i in range(3):
        Z.append(z)

    return Z


def plot_surface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [3,4,6,7]
    y = [1, 2, 3, 4]
    z = [10, 50, 11, 9]

    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z)

    plt.show()