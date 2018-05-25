import objects as obj
import algorithms as alg
import helper as helper
import run as run

def main():
    algorithm_family = ["hill_climber", "greedy"]

    algorithms = ["greedy_random", "recalculating_greedy", "hill_climber_random", "hill_climber_multi_greedy",
                  "random"]
    maps = {0:"Nationaal", 1:"Holland"}

    for i in range(len(algorithms)):
        print(i, algorithms[i])

    algorithm = algorithms[int(input("Wat wil je runnen?"))]

    for i in range(len(algorithms)):
        print(i, algorithms[i])

    map = maps[int(input["Welke kaart wil je gebruiken?"])]

    critical = (input("Is alles kritiek? (True/False)")

    times = int(input("Hoe vaak wil je hem runnen"))


    data = obj.Data("Nationaal", False)
    data.lookup_table_function = helper.lookup_score
    data.invalid_function = helper.invalid



if __name__ == "__main__":
    main()
